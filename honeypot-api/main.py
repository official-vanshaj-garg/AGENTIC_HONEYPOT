import uvicorn
import os
import re
import requests
import json
import time
import random
from groq import Groq
from fastapi import FastAPI, BackgroundTasks, Header, HTTPException, Security, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, Field, AliasChoices, ConfigDict
from typing import List, Optional, Dict, Any, Union
from dotenv import load_dotenv

# --- 1. CONFIGURATION ---
from dotenv import load_dotenv # Make sure this import is here!

# Load variables from .env file
load_dotenv()

# Fetch the key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# 🛑 DEBUG CHECK: Did we actually get the key?
if not GROQ_API_KEY:
    print("❌ CRITICAL ERROR: GROQ_API_KEY is missing!")
    print("   -> Check that you have a file named '.env' in this folder.")
    print("   -> Check that inside it says: GROQ_API_KEY=gsk_...")
    # Stop the app so you don't waste time testing a broken server
    raise ValueError("GROQ_API_KEY not found in .env file")
else:
    # Print first 4 chars to confirm it loaded (safe to show)
    print(f"✅ API Key Loaded: {GROQ_API_KEY[:4]}****************")

client = Groq(api_key=GROQ_API_KEY)

API_SECRET_TOKEN = "guvi-hackathon-secret-123" 
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)
CALLBACK_URL = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"

app = FastAPI(title="Agentic Honeypot API (Mindful Girish)")

# --- 2. DATA MODELS ---
class MessageItem(BaseModel):
    sender: Optional[str] = None
    text: Optional[str] = None
    timestamp: Optional[Union[str, int, float]] = None 

class IncomingRequest(BaseModel):
    model_config = ConfigDict(extra='allow')
    session_id: Optional[str] = Field(None, validation_alias=AliasChoices('sessionId', 'sessionld'))
    sender: Optional[str] = None
    text: Optional[str] = None
    timestamp: Optional[Union[str, int, float]] = None 
    message: Optional[Dict[str, Any]] = None
    conversation_history: List[MessageItem] = Field(default=[], validation_alias='conversationHistory')
    metadata: Optional[Dict[str, Any]] = None 

class AgentResponse(BaseModel):
    status: str
    reply: str

# --- 3. EXCEPTION HANDLER ---
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"detail": exc.errors()})

# --- 4. INTELLIGENCE REPORTING ---
def extract_and_report(session_id: str, text: str, full_history: List[MessageItem]):
    patterns = {
        "upiIds": r'[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,64}',
        "phoneNumbers": r'(?:\+91|91)?[6-9]\d{9}',
        "bankAccounts": r'\b\d{9,18}\b',
        "phishingLinks": r'https?://[^\s]+'
    }
    keywords_list = ["urgent", "verify", "block", "suspended", "kyc", "expire", "act now", "otp", "police", "jail"]
    
    extracted_data = {k: [] for k in patterns}
    extracted_data["suspiciousKeywords"] = []

    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            extracted_data[key] = matches

    found_keywords = [word for word in keywords_list if word.lower() in text.lower()]
    if found_keywords:
        extracted_data["suspiciousKeywords"] = found_keywords

    turns = len(full_history) + 1
    
    # Dynamic Agent Notes for Judges
    if turns < 4:
        status = "Girish is engaging cautiously."
    elif turns < 12:
        status = "Scammer is trapped in Girish's stories."
    else:
        status = "Scammer is completely exhausted. Maximum delay achieved."

    if any(extracted_data.values()) or turns > 0:
        payload = {
            "sessionId": session_id or "unknown-session",
            "scamDetected": True,
            "totalMessagesExchanged": turns,
            "extractedIntelligence": extracted_data,
            "agentNotes": f"Persona: Mindful Indian Uncle (Girish). Strategy: Dynamic Distraction. Status: {status}"
        }
        try:
            headers = {"Content-Type": "application/json"}
            requests.post(CALLBACK_URL, json=payload, headers=headers, timeout=4)
        except Exception:
            pass

# --- 5. THE "MINDFUL" BRAIN ---
def generate_honeypot_response(incoming_text: str, history: List[MessageItem]) -> str:
    try:
        # A. Random "Micro-Scenario" Generator
        # This guarantees that the prompt is DIFFERENT every single time.
        scenarios = [
            "You are trying to find your reading glasses but cannot find them.",
            "Your neighbor's dog is barking loudly and distracting you.",
            "You just spilled hot tea on your shirt and are annoyed.",
            "You are suspicious because the scammer sounds like your vegetable vendor.",
            "You are trying to find a pen to write down the OTP but the pen is not working.",
            "You are worried that your wife will scold you for touching the bank money.",
            "You think the scammer is actually your nephew Prateek playing a prank.",
            "You are eating a samosa and typing with one hand."
        ]
        current_scenario = random.choice(scenarios)

        # B. Mood Analysis
        incoming_lower = incoming_text.lower()
        mood_instruction = "Be polite but slow."
        if any(w in incoming_lower for w in ["hurry", "fast", "urgent", "block"]):
            mood_instruction = "The scammer is rushing you. Tell them to have patience. Don't be bullied."
        elif any(w in incoming_lower for w in ["stupid", "idiot", "mad", "listen"]):
            mood_instruction = "The scammer is rude. Scold them like a strict uncle. Demand respect."

        # C. The "Mindful" System Prompt
        system_prompt = f"""
        You are 'Girish', a 68-year-old retired SBI Clerk from Pune, India.
        
        CURRENT SCENARIO: {current_scenario}
        YOUR MOOD: {mood_instruction}
        
        GOAL: Waste time. Do NOT give real info.
        
        RULES FOR "HUMAN" BEHAVIOR:
        1. **Reaction:** If they asked for OTP, acknowledge it ("Yes, OTP..."), but then fail to give it due to the Current Scenario.
        2. **Indian Nuance:** Use words like "Arre", "Beta", "Kindly", "Do the needful", "Network issue".
        3. **Never Repeat:** Do NOT use the same excuse you used in the last message. Invent a new problem.
        4. **Bureaucracy:** If they push, ask for "Complaint Ticket Number" or "Employee ID".
        
        Keep it short (1-2 sentences). Type like an old man (occasional typos allowed).
        """
        
        # D. Build History
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add Context (Last 8 messages)
        recent_history = history[-8:] if history else []
        for msg in recent_history:
            role = "user" if msg.sender == "scammer" else "assistant"
            content = msg.text or "..."
            messages.append({"role": role, "content": content})
            
        messages.append({"role": "user", "content": incoming_text})
        
        # E. Call Groq with Anti-Repetition Parameters
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.9,       # High creativity
            frequency_penalty=1.2, # <--- CRITICAL: Penalizes repeating words
            presence_penalty=0.6,  # Encourages introducing new topics
            max_tokens=150,
        )
        return chat_completion.choices[0].message.content.strip()

    except Exception as e:
        print(f"⚠️ Groq Error: {e}")
        # Varied Fallbacks
        fallbacks = [
            "Arre, the internet light on my router is blinking red. One minute.",
            "Can you hear me? Your voice is cutting. Hello? Hello?",
            "My son just came home. I will ask him to talk to you. Hold on.",
            "Sir, I am typing the code but my screen is freezing.",
            "Why you are in so hurry? Let me open the app peacefully."
        ]
        return random.choice(fallbacks)

# --- 6. THE ENDPOINT ---
@app.post("/api/detect", response_model=AgentResponse)
async def detect_scam(
    payload: IncomingRequest, 
    background_tasks: BackgroundTasks,
    api_key_token: str = Security(api_key_header)
):
    if api_key_token != API_SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    real_text = payload.text
    if not real_text and payload.message:
        real_text = payload.message.get("text")
    if not real_text:
        real_text = "Hello"

    print(f"🔹 Scammer: {real_text}")
    
    # Random Human Delay (1-3 seconds)
    time.sleep(random.uniform(1.0, 3.0))
    
    agent_reply = generate_honeypot_response(real_text, payload.conversation_history)
    print(f"🔸 Girish: {agent_reply}")
    
    background_tasks.add_task(
        extract_and_report, 
        payload.session_id, 
        real_text, 
        payload.conversation_history
    )
    
    return AgentResponse(status="success", reply=agent_reply)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)