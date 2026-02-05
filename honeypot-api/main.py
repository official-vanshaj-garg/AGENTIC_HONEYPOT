import os
import re
import random
import asyncio
import requests
from typing import List, Optional, Dict, Any, Union

import uvicorn
from groq import Groq
from fastapi import FastAPI, HTTPException, Security, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, Field, AliasChoices, ConfigDict
from dotenv import load_dotenv

# -------------------------------------------------
# 1. CONFIGURATION
# -------------------------------------------------

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found")

client = Groq(api_key=GROQ_API_KEY)

API_SECRET_TOKEN = "guvi-hackathon-secret-123"
CALLBACK_URL = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"
FINAL_TURN_THRESHOLD = 9

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

app = FastAPI(title="Agentic Honeypot API")

# Session-level memory
SCAM_CONFIRMED_SESSIONS = set()
REPORTED_SESSIONS = set()

# -------------------------------------------------
# 2. DATA MODELS
# -------------------------------------------------

class MessageItem(BaseModel):
    sender: Optional[str] = None
    text: Optional[str] = None
    timestamp: Optional[Union[str, int, float]] = None


class IncomingRequest(BaseModel):
    model_config = ConfigDict(extra="allow")
    session_id: Optional[str] = Field(None, validation_alias=AliasChoices("sessionId", "sessionld"))
    sender: Optional[str] = None
    text: Optional[str] = None
    message: Optional[Dict[str, Any]] = None
    conversation_history: List[MessageItem] = Field(default=[], validation_alias="conversationHistory")
    metadata: Optional[Dict[str, Any]] = None


class AgentResponse(BaseModel):
    status: str
    reply: str
    finalCallback: Optional[Dict[str, Any]] = None


# -------------------------------------------------
# 3. EXCEPTION HANDLER
# -------------------------------------------------

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"detail": exc.errors()})


# -------------------------------------------------
# 4. SCAM INTENT (PASSIVE, ROBUST)
# -------------------------------------------------

def is_scam_intent(text: str) -> bool:
    text_l = text.lower()

    keyword_triggers = [
        "otp", "blocked", "suspended", "verify", "kyc",
        "urgent", "account", "upi", "pay", "transfer",
        "bank manager", "security team", "fraud"
    ]

    pattern_triggers = [
        r"\b\d{9,18}\b",                # account numbers
        r"[a-zA-Z0-9.\-_]+@[a-zA-Z]+",  # UPI IDs
        r"(?:\+91|91)?[6-9]\d{9}",      # phone numbers
        r"https?://",                   # links
    ]

    if any(k in text_l for k in keyword_triggers):
        return True

    if any(re.search(p, text) for p in pattern_triggers):
        return True

    return False


# -------------------------------------------------
# 5. FINAL CALLBACK CONDITION
# -------------------------------------------------

def should_send_final_callback(history: List[MessageItem]) -> bool:
    scammer_msgs = [m for m in history if m.sender == "scammer"]
    return len(scammer_msgs) >= FINAL_TURN_THRESHOLD


# -------------------------------------------------
# 6. INTELLIGENCE EXTRACTION + CALLBACK
# -------------------------------------------------

def extract_and_report(session_id: str, history: List[MessageItem], latest_text: str):

    full_text = " ".join([m.text for m in history if m.text] + [latest_text])

    patterns = {
        "upiIds": r"[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,64}",
        "phoneNumbers": r"(?:\+91|91)?[6-9]\d{9}",
        "bankAccounts": r"\b\d{9,18}\b",
        "phishingLinks": r"https?://[^\s]+",
    }

    keywords = ["urgent", "verify", "block", "suspended", "kyc", "expire", "otp", "police", "jail"]

    extracted = {k: list(set(re.findall(p, full_text))) for k, p in patterns.items()}
    extracted["suspiciousKeywords"] = [k for k in keywords if k in full_text.lower()]

    payload = {
        "sessionId": session_id or "unknown",
        "scamDetected": True,
        "totalMessagesExchanged": len(history) + 1,
        "extractedIntelligence": extracted,
        "agentNotes": "Scammer used urgency, impersonation, and escalation tactics."
    }
    print("📡 FINAL CALLBACK DATA:", payload)
    try:
        requests.post(
            CALLBACK_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=4,
        )
        print("✅ FINAL CALLBACK SENT")
    except Exception as e:
        print("❌ CALLBACK FAILED:", e)

    return payload


# -------------------------------------------------
# 7. HONEYPOT RESPONSE (ALWAYS CALLED)
# -------------------------------------------------

def generate_honeypot_response(incoming_text: str, history: List[MessageItem]) -> str:
    system_prompt = """
You are an common man chatting naturally in English.

PRIMARY GOAL:
- Keep the conversation going
- Let the other person reveal details gradually

RULES:
- Never share OTPs, passwords, or money
- Never mention scams, AI, or detection
- Do not act like an investigator or authority

BEHAVIOR:
- Sound cautious, unsure, and mildly worried
- If asked to pay money, ask how to pay and request details naturally
  (for example: UPI ID, bank account number, or a link)
- If asked to act urgently, seek reassurance in a normal human way
- Occasionally delay or hesitate
- Ask at most ONE question per reply

NATURAL VERIFICATION STYLE:
- Instead of accusing, ask things like:
  - “How do I make the payment?”
  - “Is there a UPI ID or account number for this?”
  - “Can I check this somewhere before I do it?”
  - “Is there an official number or link I can see?”
  - “Would it be okay if I visit the bank instead?”

STYLE:
- 1–2 sentences only
- Simple, imperfect human tone
- No technical or investigative language

"""

    messages = [{"role": "system", "content": system_prompt}]

    for msg in history[-8:]:
        role = "user" if msg.sender == "scammer" else "assistant"
        messages.append({"role": role, "content": msg.text})

    messages.append({"role": "user", "content": incoming_text})

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.45,
        top_p=0.9,
        max_tokens=120,
        presence_penalty=0.4,
        frequency_penalty=0.6,
    )

    return completion.choices[0].message.content.strip()


# -------------------------------------------------
# 8. API ENDPOINT
# -------------------------------------------------

@app.post("/api/detect", response_model=AgentResponse)
async def detect_scam(payload: IncomingRequest, api_key_token: str = Security(api_key_header)):

    if api_key_token != API_SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    message = payload.message or {}

    sender = message.get("sender") or payload.sender or "scammer"
    text = message.get("text") or payload.text or ""

    if sender != "scammer":
        return AgentResponse(status="success", reply="")

    # 🔒 PASSIVE SCAM LATCH (INSPIRED BY OLD WORKING VERSION)
    if payload.session_id and is_scam_intent(text):
        SCAM_CONFIRMED_SESSIONS.add(payload.session_id)

    await asyncio.sleep(random.uniform(1.0, 2.0))

    reply = generate_honeypot_response(text, payload.conversation_history)

    final_payload = None
    if (
        payload.session_id
        and payload.session_id in SCAM_CONFIRMED_SESSIONS
        and payload.session_id not in REPORTED_SESSIONS
        and should_send_final_callback(payload.conversation_history)
    ):
        REPORTED_SESSIONS.add(payload.session_id)
        final_payload = extract_and_report(
            payload.session_id,
            payload.conversation_history,
            text
        )

    return AgentResponse(status="success", reply=reply, finalCallback=final_payload)


# -------------------------------------------------
# 9. RUN SERVER
# -------------------------------------------------

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
