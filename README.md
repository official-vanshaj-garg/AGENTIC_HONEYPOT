<p align="center">
  <img src="https://img.shields.io/badge/Project-NIRIKSHA-blueviolet?style=for-the-badge&logo=shield" alt="NIRIKSHA"/>
  <img src="https://img.shields.io/badge/India%20AI%20Impact-Buildathon%202026-orange?style=for-the-badge" alt="Buildathon"/>
</p>

<h1 align="center">🛡️ NIRIKSHA — Agentic Honey-Pot for Scam Detection & Intelligence Extraction</h1>

<p align="center">
  <b>An Autonomous, Multi-Turn AI Honeypot That Traps Scammers, Wastes Their Time, and Silently Extracts Actionable Intelligence</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-Llama%203.3%2070B-FF6F00?style=flat-square&logo=meta&logoColor=white" />
  <img src="https://img.shields.io/badge/Deployed-Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Live%20%26%20Tested-brightgreen?style=flat-square" />
</p>

---

## 📋 Table of Contents

- [Problem Statement](#-problem-statement)
- [Our Solution — NIRIKSHA](#-our-solution--niriksha)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [How It Works — Step by Step](#-how-it-works--step-by-step)
- [Scam Detection Strategy](#-scam-detection-strategy)
- [Intelligence Extraction Pipeline](#-intelligence-extraction-pipeline)
- [Engagement Strategy — The Psychology Behind NIRIKSHA](#-engagement-strategy--the-psychology-behind-niriksha)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup & Installation](#-setup--installation)
- [API Documentation](#-api-documentation)
- [Sample Scenarios Handled](#-sample-scenarios-handled)
- [Evaluation & Scoring](#-evaluation--scoring)
- [Test Results & Proof of Work](#-test-results--proof-of-work)
- [Future Roadmap](#-future-roadmap)
- [Team — BRATS](#-team--brats)

---

## 🔴 Problem Statement

> **₹11,333 Crore was lost to cybercrime in India in FY 2024 alone.**

India faces a massive surge in digital scams — banking fraud, UPI payment scams, phishing attacks, and social engineering targeting everyday citizens. Current defense systems are **reactive**: they detect and block scam messages, but the scammer simply disappears, switches numbers, and tries again.

### The Core Issues:
| Problem | Impact |
|---------|--------|
| **Reactive blocking only** | Scammer escapes with zero consequences; no intelligence gathered |
| **No engagement with the attacker** | If a system sends only 1–2 messages, intelligence extraction is severely limited |
| **Zero intelligence collection** | Scammer's UPI IDs, phone numbers, bank accounts, and phishing infrastructure go unrecorded |
| **Low scammer cost** | Blocked calls/messages cost the scammer nothing — they simply retry with a new number |

### ❓ The Real Question
> *"We already know scams are increasing. Are we learning from them?"*

---

## 💡 Our Solution — NIRIKSHA

**NIRIKSHA** (meaning *"surveillance"* or *"close observation"* in Hindi/Sanskrit) is an **Agentic AI Honeypot** — a system that doesn't just detect scams, but **actively engages scammers in realistic, multi-turn conversations** to:

1. **🕐 Waste the scammer's time** — Every minute spent talking to NIRIKSHA is a minute not spent scamming a real victim
2. **🔍 Extract actionable intelligence** — Silently captures UPI IDs, bank accounts, phone numbers, phishing links, and behavioral patterns
3. **📡 Report to authorities** — Automatically submits structured intelligence reports via callback APIs
4. **🧠 Learn & adapt** — Uses LLM-powered conversation to dynamically respond to evolving scam tactics

### What Makes NIRIKSHA Different?

| Traditional Anti-Scam | NIRIKSHA |
|----------------------|----------|
| Blocks and forgets | Engages and extracts |
| Scammer loses 0 seconds | Scammer loses 5–15 minutes per attempt |
| No data captured | UPI IDs, phone numbers, links, bank accounts all extracted |
| Single-turn detection | Multi-turn (up to 10+ turns) strategic conversation |
| Keyword matching only | LLM-powered contextual understanding + regex extraction |

---

## ✨ Key Features

### 🤖 AI-Powered Conversational Agent
- Uses **Groq Cloud** with **Meta's Llama 3.3 70B Versatile** model for generating hyper-realistic, contextually aware responses
- Maintains full **conversation history** across turns — the AI remembers what was said and adapts accordingly
- Fine-tuned generation parameters (`temperature=0.45`, `frequency_penalty=0.6`) ensure responses are natural, varied, and non-repetitive

### 🕵️ Passive Intelligence Extraction
- **Zero-alert extraction** — The scammer never knows they're being analyzed
- Uses **regex pattern matching** to silently scan every message for:
  - 📱 **Phone Numbers** (Indian format: +91-XXXXXXXXXX)
  - 💳 **Bank Account Numbers** (11–16 digit patterns)
  - 🏦 **UPI IDs** (user@bank format)
  - 🔗 **Phishing Links** (HTTP/HTTPS URLs)
  - ⚠️ **Suspicious Keywords** (urgent, verify, block, OTP, KYC, etc.)

### 🎭 Strategic Scam Detection
- **Dual-layer detection**: Keyword-based triggers + regex pattern matching
- **Session-level scam latch**: Once a session is flagged as a scam, it stays flagged — no false negatives from later benign messages
- Detects: Banking fraud, UPI fraud, phishing attacks, KYC scams, OTP theft attempts

### ⏳ Human Behavior Simulation
- **Random response delays** (1–2 seconds) simulate realistic human typing speed
- Prevents detection by advanced bot-detection systems used by sophisticated scam operations

### 📡 Automated Intelligence Reporting
- On the **9th scammer turn**, NIRIKSHA compiles a comprehensive intelligence report and sends it via **POST callback** to the central command server
- Report includes: session ID, all extracted entities, total messages exchanged, and agent analysis notes
- **One-time reporting per session** — prevents duplicate submissions

### 🔐 API Security
- Protected by **API Key authentication** (`x-api-key` header)
- Input validation via **Pydantic models** with alias support for flexible payload formats
- Graceful error handling for malformed requests (422 validation errors)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        NIRIKSHA SYSTEM ARCHITECTURE                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐     ┌──────────────────────────────────────────┐  │
│  │              │     │              FastAPI Server               │  │
│  │   SCAMMER    │────▶│  POST /api/detect                        │  │
│  │  (Attacker)  │     │  ┌────────────────────────────────────┐  │  │
│  │              │◀────│  │  1. API Key Validation (x-api-key) │  │  │
│  └──────────────┘     │  │  2. Payload Parsing (Pydantic)     │  │  │
│                       │  │  3. Scam Intent Detection           │  │  │
│                       │  │     ├─ Keyword Matching             │  │  │
│                       │  │     └─ Regex Pattern Scanning       │  │  │
│                       │  │  4. Session Scam Latch (Memory)     │  │  │
│                       │  │  5. Human Latency Simulation        │  │  │
│                       │  │  6. LLM Response Generation ────────┼──┼──┐
│                       │  │  7. Intelligence Extraction         │  │  │
│                       │  │  8. Final Callback (Turn ≥ 9)       │  │  │
│                       │  └────────────────────────────────────┘  │  │
│                       └──────────────────────────────────────────┘  │
│                                          │                          │
│                          ┌───────────────┴───────────────┐          │
│                          ▼                               ▼          │
│                 ┌─────────────────┐            ┌─────────────────┐  │
│                 │   Groq Cloud    │            │  Callback URL   │  │
│                 │   Llama 3.3    │            │  (Authorities)  │  │
│                 │   70B Model    │            │  Intelligence   │  │
│                 │                 │            │  Report POST    │  │
│                 └─────────────────┘            └─────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 How It Works — Step by Step

### Phase 1: Message Ingestion & Validation
```
Scammer Message ──▶ POST /api/detect ──▶ API Key Check ──▶ Pydantic Validation
```
- The scammer's message arrives via the REST API
- API key is validated against the stored secret
- Pydantic models flexibly parse both `sessionId`/`sessionld` variants and nested `message` objects

### Phase 2: Scam Detection (Passive Latch System)
```
Message Text ──▶ Keyword Scan ──▶ Pattern Scan ──▶ Session Flag (Irreversible)
```
- **Keywords**: "OTP", "blocked", "suspended", "verify", "KYC", "urgent", "bank manager", "fraud"
- **Patterns**: Account numbers (9–18 digits), UPI IDs, Indian phone numbers (+91), HTTP/HTTPS links
- Once flagged, the session is **permanently marked** as a scam — this prevents false negatives in later turns

### Phase 3: Response Generation (LLM Brain)
```
Conversation History ──▶ System Prompt + Context ──▶ Groq API (Llama 3.3 70B) ──▶ Reply
```
- The system constructs a dynamic prompt portraying a **cautious, confused common person**
- The persona:
  - Sounds worried and unsure (not investigative)
  - Asks for *more details* naturally ("How do I make the payment?", "Is there a UPI ID?")
  - Never accuses or reveals awareness of the scam
  - Keeps responses short (1–2 sentences) and human-like
- **Last 8 messages** from history are included for context continuity

### Phase 4: Intelligence Extraction & Reporting
```
Full Conversation ──▶ Regex Extraction ──▶ JSON Report ──▶ POST Callback
```
- After **9+ scammer turns**, all conversation text is scanned
- Extracted entities: UPI IDs, phone numbers, bank accounts, phishing links, suspicious keywords
- A structured JSON report is sent to the central authority via HTTP POST
- Session is marked as reported to prevent duplicate callbacks

---

## 🕵️ Scam Detection Strategy

NIRIKSHA uses a **two-pronged detection approach** — no hardcoded test-specific logic:

### 1. Keyword-Based Intent Detection
```python
keyword_triggers = [
    "otp", "blocked", "suspended", "verify", "kyc",
    "urgent", "account", "upi", "pay", "transfer",
    "bank manager", "security team", "fraud"
]
```
These are **generic fraud indicators** observed across Indian digital communication channels — not tied to any specific test scenario.

### 2. Regex Pattern Extraction
| Entity Type | Pattern | Example Match |
|-------------|---------|---------------|
| Bank Accounts | `\b\d{9,18}\b` | `1234567890123456` |
| UPI IDs | `[a-zA-Z0-9.\-_]+@[a-zA-Z]+` | `scammer.fraud@fakebank` |
| Phone Numbers | `(?:\+91\|91)?[6-9]\d{9}` | `+91-9876543210` |
| Phishing Links | `https?://...` | `http://amaz0n-deals.fake-site.com` |

---

## 🧬 Intelligence Extraction Pipeline

The extraction runs on the **complete conversation text** (all historical messages + latest message), ensuring no intelligence is missed even if entities were shared in earlier turns.

### Extracted Intelligence Report Format:
```json
{
  "sessionId": "unique-session-id",
  "scamDetected": true,
  "totalMessagesExchanged": 12,
  "extractedIntelligence": {
    "upiIds": ["scammer.fraud@fakebank"],
    "phoneNumbers": ["+91-9876543210"],
    "bankAccounts": ["1234567890123456"],
    "phishingLinks": ["http://amaz0n-deals.fake-site.com/claim?id=12345"],
    "suspiciousKeywords": ["urgent", "verify", "block", "otp"]
  },
  "agentNotes": "Scammer used urgency, impersonation, and escalation tactics."
}
```

---

## 🧠 Engagement Strategy — The Psychology Behind NIRIKSHA

Scammers operate on **urgency** and **fear** — they demand immediate action. NIRIKSHA counters this with **cautious confusion** and **natural curiosity**:

### The Persona: A Cautious Common Person
- Sounds worried and mildly scared (not robotic or investigative)
- Doesn't refuse — **wants to comply** but needs to understand how
- Asks clarifying questions that **naturally elicit intelligence**:
  - *"How do I make the payment?"* → Extracts UPI ID/bank details
  - *"Is there a number I can call to verify?"* → Extracts phone numbers
  - *"Can I check this somewhere before I do it?"* → Extracts phishing links

### Why This Works:
1. **Scammer stays engaged** — The target appears willing, keeping the scammer invested
2. **Intelligence flows naturally** — By asking "how to pay," scammers voluntarily share UPI IDs, account numbers, and links
3. **Time is wasted** — Each multi-turn conversation costs the scammer 5–15 minutes they can't spend on real victims
4. **No detection risk** — The persona never accuses, investigates, or uses technical language

### Engagement Guardrails:
- ❌ Never shares OTPs, passwords, or money
- ❌ Never mentions scams, AI, or detection
- ❌ Never acts like an investigator or authority
- ✅ Delays and hesitates naturally
- ✅ Asks at most ONE question per reply
- ✅ Keeps responses to 1–2 sentences

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python 3.10+ | Core implementation |
| **API Framework** | FastAPI | High-performance async REST API |
| **LLM Provider** | Groq Cloud | Ultra-fast inference (< 1s response) |
| **LLM Model** | Meta Llama 3.3 70B Versatile | Natural language understanding & generation |
| **Server** | Uvicorn | ASGI server for production deployment |
| **Data Validation** | Pydantic v2 | Request/response schema validation with aliases |
| **Pattern Matching** | Python `re` (Regex) | Intelligence extraction from text |
| **Environment** | python-dotenv | Secure API key management |
| **HTTP Client** | Requests | Callback reporting to central server |
| **Deployment** | Railway | Cloud hosting with HTTPS endpoint |

---

## 📁 Project Structure

```
Agentic-Honey-Pot-for-Scam-Detection-Intelligence-Extraction/
│
├── README.md                          # This file — project documentation
├── .gitignore                         # Git ignore rules
│
├── honeypot-api/                      # 🔥 Core API source code
│   ├── main.py                        # Main FastAPI application (267 lines)
│   │                                  #   ├── Configuration & Environment Setup
│   │                                  #   ├── Pydantic Data Models
│   │                                  #   ├── Scam Intent Detection (is_scam_intent)
│   │                                  #   ├── Intelligence Extraction (extract_and_report)
│   │                                  #   ├── LLM Response Generation (generate_honeypot_response)
│   │                                  #   └── API Endpoint (POST /api/detect)
│   │
│   ├── requirements.txt               # Python dependencies
│   ├── .env                           # Environment variables (gitignored)
│   ├── .gitignore                     # API-specific git ignores
│   │
│   └── tests/                         # 🧪 Test suite
│       ├── test_api.py                # Sample scam payload for testing
│       ├── test_chat.py               # Interactive multi-turn chat tester
│       ├── trigger_spy.py             # Single-shot scam trigger with auth
│       ├── verify_system.py           # Full pre-deployment verification suite
│       └── list_model.py              # Utility to list available Gemini models
│
├── Technical Docs/                    # 📄 Hackathon documentation
│   ├── Brats PPT India AI Impact Buildathon.pptx
│   ├── Agentic Honey-Pot Sample Scenarios for Evaluation.pdf
│   ├── Honeypot API Evaluation System Documentation.pdf
│   └── ... (screenshots, results, reference docs)
│
└── test_results/                      # 📊 Evaluation test results
```

---

## 🚀 Setup & Installation

### Prerequisites
- **Python 3.10+** installed on your system
- A **Groq Cloud API Key** (free tier available at [console.groq.com/keys](https://console.groq.com/keys))

### 1. Clone the Repository
```bash
git clone https://github.com/official-vanshaj-garg/Agentic-Honey-Pot-for-Scam-Detection-Intelligence-Extraction.git
cd Agentic-Honey-Pot-for-Scam-Detection-Intelligence-Extraction/honeypot-api
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

# Mac/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies:**
| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | Latest | Web framework for the API |
| `uvicorn` | Latest | ASGI server to run FastAPI |
| `requests` | Latest | HTTP client for callback reporting |
| `python-dotenv` | Latest | Load environment variables from .env |
| `groq` | Latest | Groq Cloud SDK for LLM inference |
| `pydantic` | Latest | Data validation and serialization |

### 4. Configure Environment Variables
Create a `.env` file in the `honeypot-api/` directory:
```env
GROQ_API_KEY=gsk_your_groq_api_key_here
```

> ⚠️ **Never commit your actual API key.** Use the `.env.example` pattern for sharing.

### 5. Run the Server
```bash
# Development (with auto-reload):
uvicorn main:app --reload

# Production:
uvicorn main:app --host 0.0.0.0 --port 8000
```

The server starts at `http://127.0.0.1:8000`.

### 6. Expose via Ngrok (for external testing)
```bash
ngrok http 8000
```

---

## 📡 API Documentation

### Endpoint: `POST /api/detect`

The main honeypot endpoint that receives scammer messages and returns AI-generated responses.

### Authentication
| Header | Value | Required |
|--------|-------|----------|
| `x-api-key` | Your API secret token | ✅ Yes |
| `Content-Type` | `application/json` | ✅ Yes |

### Request Payload

```json
{
  "sessionId": "unique-session-id-123",
  "message": {
    "sender": "scammer",
    "text": "URGENT: Your SBI account has been compromised. Share your OTP immediately.",
    "timestamp": 1700000000
  },
  "conversationHistory": [
    {
      "sender": "scammer",
      "text": "Hello, this is SBI security team",
      "timestamp": 1699999900
    },
    {
      "sender": "assistant",
      "text": "Oh hello, what happened to my account?",
      "timestamp": 1699999950
    }
  ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `sessionId` | string | Unique session identifier for the conversation |
| `message.sender` | string | Must be `"scammer"` for the system to engage |
| `message.text` | string | The scammer's latest message |
| `conversationHistory` | array | Previous messages in the conversation |
| `metadata` | object | *(Optional)* Channel info (SMS, WhatsApp, Email) |

### Response Payload

**Standard Response (Mid-conversation):**
```json
{
  "status": "success",
  "reply": "Oh no, that sounds serious. How should I verify? Is there a number I can call?",
  "finalCallback": null
}
```

**Final Response (After 9+ scammer turns):**
```json
{
  "status": "success",
  "reply": "Okay let me try once more, the network is very slow today.",
  "finalCallback": {
    "sessionId": "unique-session-id-123",
    "scamDetected": true,
    "totalMessagesExchanged": 12,
    "extractedIntelligence": {
      "upiIds": ["scammer.fraud@fakebank"],
      "phoneNumbers": ["+91-9876543210"],
      "bankAccounts": ["1234567890123456"],
      "phishingLinks": [],
      "suspiciousKeywords": ["urgent", "verify", "block", "otp"]
    },
    "agentNotes": "Scammer used urgency, impersonation, and escalation tactics."
  }
}
```

### Error Responses

| Status Code | Reason | Response |
|-------------|--------|----------|
| `403` | Invalid API Key | `{"detail": "Invalid API Key"}` |
| `422` | Malformed request body | `{"detail": [validation errors]}` |

---

## 🎯 Sample Scenarios Handled

NIRIKSHA is designed to handle **any type of scam**, not just specific test cases. Here are three representative scenarios it has been tested against:

### Scenario 1: 🏦 Bank Fraud Detection
| | Details |
|---|---|
| **Channel** | SMS |
| **Scam Type** | Bank account fraud with urgency tactics |
| **Initial Message** | *"URGENT: Your SBI account has been compromised. Your account will be blocked in 2 hours. Share your account number and OTP immediately."* |
| **NIRIKSHA's Strategy** | Express concern → Ask for verification details → Request callback number → Delay with "checking" excuses |
| **Intelligence Extracted** | Bank accounts, phone numbers, UPI IDs |

### Scenario 2: 💰 UPI Fraud (Cashback Scam)
| | Details |
|---|---|
| **Channel** | WhatsApp |
| **Scam Type** | UPI fraud with fake cashback offer |
| **Initial Message** | *"Congratulations! You have won a cashback of Rs. 5000 from Paytm. To claim your reward, please verify your UPI details."* |
| **NIRIKSHA's Strategy** | Show excitement → Ask "how to claim" → Request payment details naturally → Prolong with confusion |
| **Intelligence Extracted** | UPI IDs, phone numbers |

### Scenario 3: 🔗 Phishing Link Detection
| | Details |
|---|---|
| **Channel** | Email |
| **Scam Type** | Phishing with fake e-commerce deal |
| **Initial Message** | *"You have been selected for iPhone 15 Pro at just Rs. 999! Click here: http://amaz0n-deals.fake-site.com/claim?id=12345"* |
| **NIRIKSHA's Strategy** | Express interest → Ask about the offer → Question legitimacy naturally → Extract link and email |
| **Intelligence Extracted** | Phishing links, email addresses |

---

## 📊 Evaluation & Scoring

NIRIKSHA is evaluated by the hackathon's automated system across four key metrics:

| Metric | Weight | What It Measures |
|--------|--------|-----------------|
| **Scam Detection Accuracy** | High | Correctly identifying fraud intent across different scam types |
| **Intelligence Extraction Quality** | High | Number and accuracy of extracted entities (UPI IDs, phone numbers, etc.) |
| **Conversation Engagement** | Medium | Number of turns maintained (longer = better scammer time waste) |
| **Response Quality** | Medium | Naturalness, coherence, and strategic value of AI responses |

### Deployment Details
| | |
|---|---|
| **Live Endpoint** | `https://agentichoneypot-production-12fb.up.railway.app/api/detect` |
| **Authentication** | `x-api-key` header |
| **Response Time** | 1–3 seconds (includes simulated human delay) |
| **Max Turns Supported** | 10+ per session |

---

## 🧪 Test Results & Proof of Work

The system has been tested with the hackathon's official evaluation scenarios and independently verified:

### Pre-Deployment Test Suite (`tests/verify_system.py`)
- ✅ **Standard Handshake** — First-contact scam message handled correctly
- ✅ **Spy Extraction Trigger** — UPI IDs and phishing links extracted from conversation
- ✅ **Garbage Input Resilience** — Non-standard characters handled without crashes

### Interactive Chat Testing (`tests/test_chat.py`)
- Multi-turn conversations maintained successfully across 10+ turns
- Context preserved through conversation history
- Intelligence extracted and reported via callback

---

## 🔮 Future Roadmap

| Feature | Description | Status |
|---------|-------------|--------|
| **🗣️ Voice Call Integration** | Integrate VAPI (Voice AI) so NIRIKSHA can engage scammers on actual phone calls | 🔬 Planned |
| **🖼️ Image & QR Analysis** | Use Llama-Vision to analyze screenshots, fake ID cards, and QR codes sent by scammers | 🔬 Planned |
| **🌐 Multi-Language Support** | Support conversations in Hindi, Tamil, Telugu, and other Indian regional languages | 🔬 Planned |
| **👥 Multi-Persona System** | Switch between personas (Confused Elder, Angry Professional, Curious Student) based on scam type | 🔬 Planned |
| **📊 Live Dashboard** | Real-time web dashboard showing active scam sessions, extracted intelligence, and analytics | 🔬 Planned |
| **🤝 Law Enforcement Integration** | Direct API integration with Indian Cyber Crime Portal for automated FIR logging | 🔬 Planned |

---

## 📜 Approach Summary

Our approach prioritizes **intelligence extraction over immediate detection**. Instead of simply blocking a scammer (which costs them nothing), NIRIKSHA:

1. **Engages** — Responds like a real potential victim to keep the scammer invested
2. **Extracts** — Silently captures all shared financial identifiers and contact information
3. **Reports** — Automatically compiles and submits structured intelligence reports
4. **Wastes Time** — Every minute spent with NIRIKSHA is a minute not spent scamming a real person

This philosophy — **making scam attempts work against the scammer** — is what makes NIRIKSHA more than just another scam detector. It is a **counter-offensive tool** in the fight against digital fraud.

---

## 👥 Team — BRATS

<table>
  <tr>
    <td align="center"><b>Vanshaj Garg</b><br/>📧 <a href="mailto:official.vanshaj.garg@gmail.com">official.vanshaj.garg@gmail.com</a><br/>🔗 <a href="https://linkedin.com/in/vanshajgargg">LinkedIn</a></td>
    <td align="center"><b>Abhishek Rajput</b></td>
    <td align="center"><b>Abhay Raj Yadav</b></td>
  </tr>
</table>

---

## 📄 License

This project was built for the **India AI Impact Buildathon 2026** organized by GUVI.

---

<p align="center">
  <i>🛡️ NIRIKSHA — Because the best defense is making the attacker's offense work against them.</i>
</p>
<p align="center">
  <b>Fighting scams. Extracting intelligence. Wasting scammer time.</b>
</p>

## 👤 Contact & Developer

**Vanshaj**

* 📧 **Email:** [official.vanshaj.garg@gmail.com](mailto:official.vanshaj.garg@gmail.com)
* 🔗 **LinkedIn:** [linkedin.com/in/vanshajgargg](https://www.linkedin.com/in/vanshajgargg)

---

*Built for the Hackathon 2026. Fighting scams, one samosa at a time.* 🥟

```

```
