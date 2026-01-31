Here is the complete, professionally formatted `README.md` file. You can copy the code block below and paste it directly into your `README.md` file.

```markdown
# 🛡️ Agentic Honeypot API: Project "Girish"

> **An Autonomous, Context-Aware AI Honeypot designed to waste scammers' time using "Weaponized Incompetence."**

![Status](https://img.shields.io/badge/Status-Active-success) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![AI](https://img.shields.io/badge/Powered%20By-Groq%20%7C%20Llama3-orange)

## 📖 Overview

This project is an **Agentic AI Honeypot** built to counter social engineering scams (specifically banking, OTP, and KYC fraud). Unlike traditional honeypots that simply log attacks, this system actively engages the attacker in a conversation.

The core of the system is **"Girish"**, a hyper-realistic persona of a 68-year-old retired Indian SBI clerk. Girish is polite, bureaucratic, technologically illiterate, and prone to "network issues." By simulating these human flaws, the system keeps scammers trapped in a loop, wasting their valuable time while silently extracting actionable intelligence (UPI IDs, Phone Numbers, Bank Accounts) to report to authorities.

---

## 🧠 Why This Works: The Psychology of "Girish"

Scammers operate on **urgency** and **fear**. They demand immediate action ("Block in 2 hours", "Send OTP Now").

This system counters that with **Bureaucracy** and **Confusion**.
* **The Persona:** Girish represents the demographic scammers target most (the elderly). This lowers their guard.
* **Weaponized Incompetence:** By complaining about "oily hands from samosas," "lost spectacles," or "Jio network issues," the AI forces the scammer to slow down and explain things repeatedly.
* **Bureaucratic Delay:** Instead of refusing (which ends the chat), Girish *wants* to help but needs to "verify the Employee ID" or "check with his son-in-law," trapping the scammer in their own fake logic.

---

## ✨ Key Features

* **⚡ Powered by Groq & Llama-3.3:** Uses the `llama-3.3-70b-versatile` model for lightning-fast, highly contextual, and creative responses.
* **🧠 Mindful Context Awareness:** Maintains conversation history. The AI remembers previous excuses so it doesn't repeat "I lost my glasses" twice in a row.
* **🎭 Dynamic Scenario Engine:** Every response is influenced by a random "Micro-Scenario" (e.g., "Drinking tea," "Dog barking," "Wife calling"). This prevents the AI from becoming robotic or predictable.
* **🕵️‍♂️ Passive Intelligence Extraction:** Uses Regex patterns to silently scan incoming messages for UPI IDs, Phone Numbers, and Phishing Links.
* **⏳ Human Latency Simulation:** Random `time.sleep` intervals simulate the slow typing speed of an elderly user.
* **📡 Automated Reporting:** Automatically flags confirmed scams and sends a JSON report to the central command server (Judges/Authorities).

---

## ⚙️ Technical Architecture

1.  **Ingestion:** The FastAPI endpoint (`/api/detect`) receives the scammer's message.
2.  **Spy Layer:** The `extract_and_report` background task scans the text for keywords ("OTP", "Block") and entities (UPI, Phone).
3.  **Brain Layer:**
    * The system constructs a dynamic prompt including the **Current Persona Mood** (e.g., Stubborn, Confused) and **Conversation History**.
    * It calls the **Groq API** with parameters like `frequency_penalty` to ensure unique, non-repetitive responses.
4.  **Response:** The AI generates a "Girish-style" reply (typos and Indian English nuances included) and sends it back.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** FastAPI (High-performance Async Framework)
* **LLM Provider:** Groq Cloud (Model: `llama-3.3-70b-versatile`)
* **Server:** Uvicorn
* **Utilities:** Regex (Data Extraction), Pydantic (Data Validation)

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/agentic-honeypot.git](https://github.com/your-username/agentic-honeypot.git)
cd agentic-honeypot

```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
# Activate:
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

```

### 3. Install Dependencies

Create a `requirements.txt` file (or use the one provided) and install:

```bash
pip install fastapi uvicorn requests python-dotenv groq pydantic

```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Get your key from [https://console.groq.com/keys](https://console.groq.com/keys)
GROQ_API_KEY=gsk_your_groq_api_key_here

```

### 5. Run the Server

```bash
uvicorn main:app --reload

```

The server will start at `http://127.0.0.1:8000`.

---

## 🔌 API Documentation

### Endpoint: `POST /api/detect`

This is the main entry point for the scammer's messages.

**Request Payload:**

```json
{
  "sessionId": "unique-session-id-123",
  "text": "URGENT: Your account is blocked. Send OTP.",
  "sender": "scammer",
  "conversationHistory": [
    {
      "sender": "scammer",
      "text": "Hello",
      "timestamp": 17000000
    }
  ]
}

```

**Response Payload:**

```json
{
  "status": "success",
  "reply": "Arre beta, kindly have patience. My spectacles fell under the sofa. One minute."
}

```

---

## 📊 Sample Extraction Report

When the system detects a scam, it silently sends this report to the authorities:

```json
{
  "sessionId": "unique-session-id-123",
  "scamDetected": true,
  "totalMessagesExchanged": 12,
  "extractedIntelligence": {
    "upiIds": ["scammer.fraud@fakebank"],
    "phoneNumbers": ["9876543210"],
    "suspiciousKeywords": ["urgent", "block", "otp"]
  },
  "agentNotes": "Persona: Smart Indian Uncle (Girish). Status: Scammer is completely exhausted. Maximum delay achieved."
}

```

---

## 🔮 Future Improvements

* **Voice Capability:** Integrating VAPI (Voice AI) to allow Girish to speak on actual phone calls.
* **Image Analysis:** Using Llama-Vision to analyze QR codes or fake ID cards sent by scammers.
* **Multi-Persona:** Switching between "Girish" (Polite) and "Ramesh" (Angry Cop) depending on the scammer's aggression.

---

## 👤 Contact & Developer

**Vanshaj**

* 📧 **Email:** [official.vanshaj.garg@gmail.com](mailto:official.vanshaj.garg@gmail.com)
* 🔗 **LinkedIn:** [linkedin.com/in/vanshajgargg](https://www.linkedin.com/in/vanshajgargg)

---

*Built for the Hackathon 2026. Fighting scams, one samosa at a time.* 🥟

```

```
