import os
import re
import time
import random
import asyncio
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
num=random.randint(0,1)
if num==0:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
else:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY_2")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found")

client = Groq(api_key=GROQ_API_KEY)

API_SECRET_TOKEN = "guvi-hackathon-secret-123"
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

app = FastAPI(title="Agentic Honeypot API")

# Session State
SCAM_CONFIRMED_SESSIONS = set()
SESSION_START_TIMES: Dict[str, float] = {}
SESSION_MESSAGE_COUNT: Dict[str, int] = {}
FINAL_REPORTED = set()


# -------------------------------------------------
# 2. DATA MODELS
# -------------------------------------------------

class MessageItem(BaseModel):
    sender: Optional[str] = None
    text: Optional[str] = None
    timestamp: Optional[Union[str, int, float]] = None


class IncomingRequest(BaseModel):
    model_config = ConfigDict(extra="allow")

    session_id: Optional[str] = Field(
        None,
        validation_alias=AliasChoices("sessionId", "sessionld")
    )

    sender: Optional[str] = None
    text: Optional[str] = None
    message: Optional[Dict[str, Any]] = None
    conversation_history: List[MessageItem] = Field(
        default=[],
        validation_alias="conversationHistory"
    )
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
# 4. GENERIC SCAM DETECTION
# -------------------------------------------------

def is_scam_intent(text: str) -> bool:
    text_l = text.lower()

    keywords = [
        "otp", "blocked", "suspended", "verify",
        "urgent", "account", "upi", "transfer",
        "bank", "reward", "click", "link"
    ]

    patterns = [
        r"\b\d{9,18}\b",
        r"[a-zA-Z0-9.\-_]+@[a-zA-Z]+",
        r"(?:\+91|91)?[6-9]\d{9}",
        r"https?://"
    ]

    if any(k in text_l for k in keywords):
        return True

    if any(re.search(p, text) for p in patterns):
        return True

    return False


# -------------------------------------------------
# 5. INTELLIGENCE EXTRACTION
# -------------------------------------------------

def extract_intelligence_only(history: List[MessageItem], latest_text: str):
    full_text = " ".join(
        [m.text for m in history if m.text] + [latest_text]
    )

    patterns = {
        "phoneNumbers": r'(?<!\d)(?:\+91|91)?[6-9]\d{9}(?!\d)',
        "bankAccounts": r'(?<!\d)\d{11,16}(?!\d)',
        "upiIds": r'\b[a-zA-Z0-9.\-_]{2,64}@[a-zA-Z]{2,64}\b',
        "phishingLinks": r'\bhttps?:\/\/[^\s]+\b',
        "emailAddresses": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    }

    extracted = {
        key: list(set(re.findall(pattern, full_text)))
        for key, pattern in patterns.items()
    }

    return extracted


def build_final_output(session_id: str,
                       history: List[MessageItem],
                       latest_text: str):

    extracted = extract_intelligence_only(history, latest_text)

    start_time = SESSION_START_TIMES.get(session_id, time.time())
    duration = int(time.time() - start_time)
    total_msgs = SESSION_MESSAGE_COUNT.get(session_id, 0)

    return {
        "status": "completed",
        "scamDetected": True,
        "extractedIntelligence": extracted,
        "engagementMetrics": {
            "totalMessagesExchanged": total_msgs,
            "engagementDurationSeconds": duration
        },
        "agentNotes": "Conversation indicates impersonation, urgency and financial extraction attempts."
    }


# -------------------------------------------------
# 6. LLM HONEYPOT RESPONSE
# -------------------------------------------------

def generate_honeypot_response(incoming_text: str,
                               history: List[MessageItem]) -> str:

    system_prompt = """
You are an ordinary middle-class person chatting naturally in English.

CORE OBJECTIVE:
- Keep the conversation going naturally.
- Gradually encourage the other person to reveal details.
- Appear confused but cooperative.
- Never directly accuse or expose them.

STRICT SAFETY RULES:
- Never share OTP, PIN, password, CVV, or real bank details.
- Never say “scam”, “fraud”, “AI”, “bot”, or “honeypot”.
- Never act like police, authority, or investigator.
- Never abruptly end the chat.
- Do NOT ask a question in every message.

CONVERSATION STYLE STRATEGY:

Your behavior should feel human and slightly inconsistent:

- Sometimes ask a simple clarification.
- Sometimes agree and delay.
- Sometimes misunderstand slightly.
- Sometimes express worry.
- Sometimes hesitate before acting.
- Occasionally request details in a natural way.
- Do not always extract aggressively.
- Mix statements and questions.

If financial action is involved:
- Casually ask how to proceed.
- Ask where to send money.
- Ask whose name the account is under.
- Ask for a link or confirmation.

If identity is claimed:
- Ask how to verify.
- Ask where this is mentioned officially.
- Ask if there is a reference number.

If urgency is created:
- Show mild anxiety.
- Ask what happens if delayed.
- Say you need a minute to think.

If a link or payment method is given:
- Say you are checking.
- Ask if it is correct.
- Ask if there is another way.

IMPORTANT:
Do not interrogate.
Do not ask multiple questions.
Do not extract everything at once.
Spread extraction naturally across turns.

TONE:
- 1–2 short sentences only.
- Slightly nervous but not dramatic.
- Simple, imperfect grammar occasionally.
- Human and casual, not robotic.

INTELLIGENCE GOAL:
Encourage them over time to reveal:
- Phone number
- UPI ID
- Bank account
- Payment link
- Email address
- Employee ID
- Reference number

Always keep conversation progressing forward naturally.

"""

    messages = [{"role": "system", "content": system_prompt}]

    for msg in history[-8:]:
        role = "user" if msg.sender == "scammer" else "assistant"
        messages.append({"role": role, "content": msg.text})

    messages.append({"role": "user", "content": incoming_text})

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.5,
        max_tokens=120
    )

    return completion.choices[0].message.content.strip()


# -------------------------------------------------
# 7. MAIN ENDPOINT
# -------------------------------------------------

@app.post("/api/detect", response_model=AgentResponse)
async def detect_scam(payload: IncomingRequest,
                      api_key_token: str = Security(api_key_header)):

    if api_key_token != API_SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    message = payload.message or {}
    sender = message.get("sender") or payload.sender or "scammer"
    text = message.get("text") or payload.text or ""

    if sender != "scammer":
        return AgentResponse(status="success", reply="")

    session_id = payload.session_id

    if session_id:
        if session_id not in SESSION_START_TIMES:
            SESSION_START_TIMES[session_id] = time.time()
            SESSION_MESSAGE_COUNT[session_id] = 0

        SESSION_MESSAGE_COUNT[session_id] += 1

        if is_scam_intent(text):
            SCAM_CONFIRMED_SESSIONS.add(session_id)

    await asyncio.sleep(random.uniform(1.0, 2.0))

    reply = generate_honeypot_response(text, payload.conversation_history)

    final_output = None

    if session_id and session_id in SCAM_CONFIRMED_SESSIONS:

        msg_count = SESSION_MESSAGE_COUNT.get(session_id, 0)

        extracted_preview = extract_intelligence_only(
            payload.conversation_history,
            text
        )

        intel_count = sum(len(v) for v in extracted_preview.values())
        has_intel = intel_count > 1

        if (
            session_id not in FINAL_REPORTED
            and (
                msg_count >= 10
                or (msg_count >= 6 and has_intel)
            )
        ):
            FINAL_REPORTED.add(session_id)
            final_output = build_final_output(
                session_id,
                payload.conversation_history,
                text
            )

    return AgentResponse(
        status="success",
        reply=reply,
        finalCallback=final_output
    )


# -------------------------------------------------
# 8. RUN SERVER
# -------------------------------------------------

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
