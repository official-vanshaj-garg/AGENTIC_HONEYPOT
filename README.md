<p align="center">
  <img src="https://img.shields.io/badge/Project-NIRIKSHA.ai-blueviolet?style=for-the-badge&logo=shield" alt="NIRIKSHA.ai"/>
  <img src="https://img.shields.io/badge/India%20AI%20Impact-Buildathon%202026-orange?style=for-the-badge" alt="Buildathon"/>
</p>

<h1 align="center">🛡️ NIRIKSHA.ai — Agentic Honey-Pot for Scam Detection & Intelligence Extraction</h1>

<p align="center">
  <b>An Autonomous, Multi-Turn AI Honeypot That Traps Scammers in Realistic Conversations,<br/>Wastes Their Time, and Silently Extracts Actionable Intelligence</b>
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

- [What is NIRIKSHA.ai?](#-what-is-niriksha-ai)
- [Problem Statement](#-problem-statement)
- [Our Solution](#-our-solution)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [How It Works (Step by Step)](#-how-it-works-step-by-step)
- [Module Breakdown (main.py)](#-module-breakdown-mainpy)
- [Scam Detection & Scoring System](#-scam-detection--scoring-system)
- [Intelligence Extraction Pipeline](#-intelligence-extraction-pipeline)
- [LLM-Powered Response Engine](#-llm-powered-response-engine)
- [Final Output & Scam Classification](#-final-output--scam-classification)
- [Engagement Strategy — The Psychology Behind NIRIKSHA.ai](#-engagement-strategy--the-psychology-behind-nirukshaai)
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

## 🔍 What is NIRIKSHA.ai?

**NIRIKSHA** (meaning *"surveillance"* or *"close observation"* in Hindi/Sanskrit) is an **Agentic AI Honeypot** — think of it as an AI that pretends to be a real person when a scammer calls or messages.

**In simple terms:** When a scammer sends a fraudulent message (like "Your bank account is blocked, share your OTP"), instead of simply blocking it, NIRIKSHA.ai starts a realistic conversation with the scammer. The scammer believes they're talking to a real victim. Meanwhile, the AI is:
- ⏳ **Wasting the scammer's time** so they can't scam real people
- 🔍 **Secretly recording** every UPI ID, bank account, phone number, and phishing link the scammer shares
- 📡 **Automatically sending a report** with all this information to the authorities

The scammer never realizes they're talking to an AI.

---

## 🔴 Problem Statement

> **₹11,333 Crore was lost to cybercrime in India in FY 2024.**
> **5,00,000+ scam calls flood India every single day.**

India faces a massive surge in digital scams: banking fraud, UPI payment scams, phishing attacks, and social engineering targeting everyday citizens. Current defense systems are **reactive** — they detect and block scam messages, but the scammer simply disappears, switches numbers, and tries again.

### What's Wrong with Current Solutions?

| Problem | What Happens |
|---------|-------------|
| **Blocking only** | The scammer is blocked but faces zero consequences. No data is collected. They switch numbers and try again. |
| **No conversation** | If a system sends only 1-2 messages before blocking, there's no chance to gather useful information about the scammer. |
| **Zero intelligence** | The scammer's UPI IDs, phone numbers, bank accounts, and phishing websites go completely unrecorded. |
| **Low cost to scammer** | Getting blocked costs the scammer nothing — they simply retry with a different number in seconds. |

### The Real Question
> *"We already know scams are increasing. But are we learning anything from them?"*

---

## 💡 Our Solution

NIRIKSHA.ai flips the script. Instead of blocking scammers (which costs them nothing), we **engage them** in long, realistic conversations that:

| What NIRIKSHA.ai Does | Why It Matters |
|----------------------|---------------|
| **Engages the scammer for 10+ conversation turns** | Every minute spent talking to NIRIKSHA.ai is a minute NOT spent scamming a real person |
| **Extracts UPI IDs, bank accounts, phone numbers, phishing links** | This data can be used by law enforcement to track and shut down scam operations |
| **Classifies the type of scam** (bank fraud, UPI fraud, phishing, etc.) | Helps in understanding patterns and building better defenses |
| **Generates detailed intelligence reports automatically** | No manual analysis needed; reports are machine-readable JSON |
| **Adapts conversation based on what the scammer says** | Uses LLM (AI language model) to respond naturally, not with scripted responses |

### NIRIKSHA.ai vs. Traditional Anti-Scam Systems

| Feature | Traditional Systems | NIRIKSHA.ai |
|---------|-------------------|------------|
| Response to scam | Block and forget | Engage, extract, and report |
| Time cost to scammer | 0 seconds | 5-15 minutes per attempt |
| Data captured | None | UPI IDs, phone numbers, links, bank accounts, reference IDs, emails |
| Conversation depth | 1-2 messages | 10+ turns of strategic conversation |
| Detection method | Simple keyword matching | LLM-powered understanding + regex extraction + scam scoring |
| Scam classification | None | AI-powered classification into 9 scam categories |

---

## ✨ Key Features

### 🤖 1. AI-Powered Conversational Agent
NIRIKSHA.ai uses **Groq Cloud** with **Meta's Llama 3.3 70B Versatile** model — one of the most powerful open-source language models available. This means:
- Responses sound like a real person, not a chatbot
- The AI understands context from previous messages (it remembers what was said earlier in the conversation)
- Each response is unique and natural — no two conversations are the same

### 🧮 2. Multi-Factor Scam Scoring System
Instead of a simple "is this a scam? yes/no" check, NIRIKSHA.ai uses a **weighted scoring system** that assigns points based on:
- **+6 points** if someone asks for your OTP or PIN
- **+3 points** if they ask you to click a suspicious link
- **+3 points** if the message contains payment demands with UPI/bank details
- **+1-2 points** for urgency words like "immediately", "blocked", "suspended"
- **-4 points** if the message *warns against* sharing OTP (meaning it's a genuine safety message)

This scoring system makes NIRIKSHA.ai extremely accurate — it can distinguish between a real bank warning ("Never share your OTP") and a scammer pretending to be your bank ("Share your OTP immediately").

### 🕵️ 3. Deep Intelligence Extraction
NIRIKSHA.ai silently scans every message for **7 types of intelligence data**:

| Data Type | What It Captures | Example |
|-----------|-----------------|---------|
| 📱 Phone Numbers | Indian format numbers | +91-9876543210 |
| 💳 Bank Accounts | 9-18 digit account numbers | 1234567890123456 |
| 🏦 UPI IDs | Payment addresses | scammer.fraud@fakebank |
| 🔗 Phishing Links | Suspicious URLs | http://amaz0n-deals.fake-site.com |
| 📧 Email Addresses | Scammer email IDs | offers@fake-amazon-deals.com |
| 🎫 Reference/Case IDs | Fake ticket numbers | REF-2024-789456, CASE-12345 |
| 📋 Policy/Order Numbers | Fake order references | POLICY-123456, ORDER-789 |

The extraction is **smart enough** to:
- Distinguish UPI IDs from email addresses (they look similar but work differently)
- Not count phone numbers twice as bank accounts
- Filter out timestamps that look like large numbers
- Clean up and normalize phone numbers to a standard format

### 🎯 4. Rubric-Aware Response Generation
NIRIKSHA.ai tracks specific **conversation quality metrics** across the entire session:

| Metric | Target by Turn 8 | Why It Matters |
|--------|-----------------|---------------|
| Questions asked | ≥ 5 | More questions = more scammer data extracted |
| Investigative/verification wording | ≥ 3 times | Shows the "victim" is cautious but engaged |
| Red-flag word mentions | ≥ 5 references | Keeps the conversation on-topic (about the scam) |
| Data elicitation attempts | ≥ 4 | Actively pulls out accounts, UPIs, links, emails |

The AI automatically adjusts its behavior to hit these targets. If it hasn't asked enough questions by turn 5, it naturally adds one.

### 🧠 5. LLM-Based Scam Classification
At the end of the conversation, NIRIKSHA.ai uses a **separate AI call** to classify the scam into one of 9 categories:

```
bank_fraud | upi_fraud | phishing | job_scam | investment_scam
lottery_scam | kyc_scam | utility_scam | unknown
```

This classification comes with a **confidence score** (0.0 to 1.0), telling you how sure the AI is about its classification.

### ⏳ 6. Human Behavior Simulation
NIRIKSHA.ai adds **random response delays** (0.1-0.28 seconds) to simulate realistic human behavior. This prevents detection by advanced bot-detection systems.

### 📡 7. Automated Intelligence Reporting
Once the conversation reaches a sufficient number of turns (8-10) and enough intelligence has been gathered, NIRIKSHA.ai automatically compiles a comprehensive JSON report containing everything it extracted.

### 🔐 8. API Security
- Protected by **API Key authentication** (`x-api-key` header)
- Input validation via **Pydantic v2 models** with flexible alias support
- Graceful error handling for malformed requests

### 🧹 9. Smart Reply Sanitization
Every AI response goes through a sanitization layer that:
- Removes any accidental mentions of "scam", "fraud", "AI", "bot", or "honeypot"
- Ensures only ONE question is asked per reply (to sound natural)
- Trims responses to stay under 200 characters (short, human-like messages)

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                     NIRIKSHA.ai SYSTEM ARCHITECTURE                     │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  SCAMMER ──► POST /api/detect                                            │
│               │                                                          │
│               ▼                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │  LAYER 1: INGESTION & VALIDATION                                  │  │
│  │  • API Key check (x-api-key header)                               │  │
│  │  • Pydantic model parsing (handles sessionId/sessionld aliases)   │  │
│  │  • Session initialization (first-time setup for new sessions)     │  │
│  └─────────┬──────────────────────────────────────────────────────────┘  │
│             ▼                                                            │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │  LAYER 2: SCAM SCORING                                            │  │
│  │  • Keyword-based scoring (+1 to +6 per signal)                    │  │
│  │  • Pattern detection (OTP requests, payment demands, link clicks) │  │
│  │  • Anti-false-positive checks (genuine safety warnings get -4)    │  │
│  └─────────┬──────────────────────────────────────────────────────────┘  │
│             ▼                                                            │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │  LAYER 3: INTELLIGENCE PREVIEW                                    │  │
│  │  • Extract entities from all messages so far                      │  │
│  │  • Identify missing intelligence (what haven't we captured yet?)  │  │
│  │  • Generate "next hint" for the LLM (e.g., "ask for UPI ID")     │  │
│  └─────────┬──────────────────────────────────────────────────────────┘  │
│             ▼                                                            │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │  LAYER 4: LLM RESPONSE GENERATION (Groq Cloud)                   │  │
│  │  • Builds dynamic system prompt with rubric targets               │  │
│  │  • Includes last 8 messages for context                           │  │
│  │  • Sanitizes output (remove banned words, limit to 1 question)    │  │
│  │  • Enforces minimum rubric thresholds if behind schedule          │  │
│  └─────────┬──────────────────────────────────────────────────────────┘  │
│             ▼                                                            │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │  LAYER 5: FINAL OUTPUT (Triggered at Turn 8-10)                   │  │
│  │  • LLM-based scam type classification (9 categories)              │  │
│  │  • Full intelligence extraction across entire conversation        │  │
│  │  • Engagement metrics (duration, message count)                   │  │
│  │  • JSON report generation                                         │  │
│  └─────────┬──────────────────────────────────────────────────────────┘  │
│             ▼                                                            │
│         RESPONSE ──► { status, reply, finalCallback, finalOutput }       │
│                                                                          │
│  ┌─────────────────────────┐        ┌─────────────────────────────────┐  │
│  │   Groq Cloud (LLM)     │        │   Session State (In-Memory)     │  │
│  │   Llama 3.3 70B        │        │   • Turn counts                 │  │
│  │   • Conversation AI    │        │   • Scam scores                 │  │
│  │   • Scam classification│        │   • Rubric feature tracking     │  │
│  └─────────────────────────┘        │   • Asked-question tracking    │  │
│                                     │   • Start time tracking        │  │
│                                     └─────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 How It Works (Step by Step)

Here's what happens each time a scammer sends a message to NIRIKSHA.ai, explained in plain English:

### Step 1: Receive & Validate the Message
When a new message comes in:
1. The system checks the **API key** in the request header. If it's wrong, the request is rejected with a 403 error.
2. The message text and sender information are extracted from the request body.
3. If this is a **new session** (first message from this scammer), the system creates a fresh set of tracking variables: turn count, scam score, rubric feature counts, and a start time.

### Step 2: Score the Scam Risk
The incoming message is run through the **scam scoring engine**:
- Words like "urgent", "blocked", "OTP" each add points
- Patterns like UPI IDs, phone numbers, and links add more points  
- Genuine safety messages ("don't share your OTP") subtract points
- The score accumulates across the entire conversation

### Step 3: Extract Intelligence (Preview)
Before generating a reply, the system scans **all messages in the conversation so far** to extract:
- Phone numbers, UPI IDs, bank accounts, email addresses, phishing links, and reference IDs
- It then figures out what information it **hasn't** captured yet, and tells the AI to ask for that specific thing ("ask for their UPI ID" or "ask for the reference number")

### Step 4: Generate AI Response
The system sends the conversation to **Groq Cloud (Llama 3.3 70B)** to generate a response. The AI is instructed to:
- Sound like a confused, worried common person
- Ask naturally for the missing intelligence (without seeming suspicious)
- Never mention "scam", "fraud", "AI", or "honeypot"
- Keep responses short (1-2 sentences, max 1 question)

The response is then **sanitized**: banned words are removed, multiple questions are reduced to one, and length is capped at 200 characters.

### Step 5: Track Rubric Metrics
After generating the reply, the system counts specific features in the response:
- Did it contain a question? (+1 to question count)
- Did it use investigative wording like "verify" or "confirm"? (+1)
- Did it mention red-flag words like "OTP" or "blocked"? (+1)
- Did it try to elicit details like "account" or "UPI"? (+1)

If the counts are falling behind the targets, a **minimal guardrail** adds a natural question to catch up.

### Step 6: Generate Final Report (When Ready)
At **turn 10** (or turn 8 if enough intelligence has been collected), the system:
1. Uses a **separate LLM call** to classify the scam type (bank fraud, phishing, etc.)
2. Runs the **full extraction pipeline** one last time across all messages
3. Calculates engagement metrics (duration, total messages)
4. Packages everything into a structured **JSON report**
5. Returns this report in the `finalCallback` and `finalOutput` fields

---

## 📦 Module Breakdown (main.py)

The entire API is contained in a single, well-organized `main.py` file (614 lines), divided into 10 clearly labeled sections:

| Section | Lines | Purpose | What It Does (Simple Explanation) |
|---------|-------|---------|----------------------------------|
| **1. Config** | 1-38 | Environment setup | Loads API keys, sets delay timing, initializes the FastAPI app |
| **2. Session State** | 40-49 | Memory management | Dictionaries that track each conversation: turn counts, scam scores, what questions were already asked |
| **3. Models** | 51-84 | Data structure definitions | Defines the shape of incoming requests and outgoing responses using Pydantic |
| **4. Normalization + Patterns** | 86-136 | Regex patterns | All the regular expressions used to find phone numbers, UPI IDs, links, emails, reference IDs in text |
| **5. Scam Score** | 138-185 | Risk assessment | The point-based scoring system that evaluates how "scammy" each message is |
| **6. Extraction** | 187-284 | Intelligence gathering | Functions that pull out all useful data from conversation text, with smart filtering |
| **7. LLM Reply** | 286-442 | AI response generation | Builds prompts, calls Groq API, sanitizes output, enforces rubric minimums |
| **8. Final Output** | 444-527 | Report generation | LLM-based scam classification, engagement metrics, final JSON report building |
| **9. Endpoint** | 529-607 | API handler | The main `/api/detect` POST endpoint that orchestrates everything |
| **10. Run** | 609-614 | Server startup | Starts the Uvicorn server |

Additionally, the `app/` directory contains a **modular version** of the same logic, split into individual files for maintainability:

| File | Purpose |
|------|---------|
| `config.py` | Environment variables and app configuration |
| `schemas.py` | Pydantic request/response models |
| `patterns.py` | All regex patterns for entity extraction |
| `scoring.py` | Scam scoring engine |
| `extraction.py` | Intelligence extraction pipeline |
| `replies.py` | LLM response generation and sanitization |
| `llm_client.py` | Groq API client wrapper |
| `session_store.py` | Session state management |
| `state.py` | Global state variables |
| `service.py` | Business logic orchestration |
| `models.py` | Internal data models |

---

## 🧮 Scam Detection & Scoring System

NIRIKSHA.ai uses a **point-based scoring system** that's far more sophisticated than simple keyword matching. Here's exactly how it works:

### High-Value Signals (Strong Scam Indicators)

| Signal | Points | Example |
|--------|--------|---------|
| Asking victim to share OTP | **+6** | "Send your OTP immediately" |
| Asking for PIN/CVV/password | **+6** | "Enter your PIN to verify" |
| Asking victim to click a link | **+3** | "Click this link to verify" |
| Payment demand with UPI/bank details | **+3** | "Transfer ₹5000 to scammer@oksbi" |

### Medium Signals (Scam Patterns)

| Signal | Points | Example |
|--------|--------|---------|
| Contains a phishing URL | **+2** | Any http:// or https:// link |
| Contains a UPI ID | **+2** | user@bankname |
| Contains a phone number | **+1** | +91-9876543210 |
| Contains a long number (possible account) | **+1** | 1234567890123456 |

### Urgency Words (+1 each)

`urgent` · `immediately` · `asap` · `final warning` · `within` · `blocked` · `suspended` · `disconnect` · `penalty` · `frozen`

### False Positive Protection (-4 each)

| Signal | Points | Example |
|--------|--------|---------|
| Warning NOT to share OTP | **-4** | "Do not share your OTP with anyone" |
| Warning NOT to share PIN | **-4** | "Never share your PIN" |

This negative scoring prevents NIRIKSHA.ai from misclassifying genuine bank safety messages as scams.

---

## 🔬 Intelligence Extraction Pipeline

The extraction system processes **every message in the conversation** (not just the latest one). Here's what it captures and how:

### Entity Types & Detection Patterns

| Entity | Pattern | Smart Filtering |
|--------|---------|----------------|
| **Phone Numbers** | Matches Indian numbers: `+91XXXXXXXXXX`, `91XXXXXXXXXX`, `XXXXXXXXXX` (starting with 6-9) | Normalizes all formats to `+91XXXXXXXXXX` |
| **UPI IDs** | Matches `username@bankcode` format | Excludes email addresses (checks for dots in domain); excludes truncated emails |
| **Bank Accounts** | Matches 9-18 digit numbers | Excludes numbers that are phone numbers; excludes epoch timestamps (13-digit values) |
| **Phishing Links** | Matches all HTTP/HTTPS URLs | Cleans trailing punctuation |
| **Email Addresses** | Standard email pattern matching | Kept separate from UPI IDs |
| **Reference/Case IDs** | Matches patterns like `REF-12345`, `CASE-789`, `TICKET-456` | Categorizes into case IDs, policy numbers, and order numbers |

### Deduplication & Normalization
- All extracted values are **deduplicated** (no repeats)
- Phone numbers are **normalized** to a standard `+91XXXXXXXXXX` format
- URLs are **cleaned** of trailing punctuation
- Reference IDs are **categorized** into sub-types (case IDs, policy numbers, order numbers)

---

## 🤖 LLM-Powered Response Engine

NIRIKSHA.ai uses a carefully crafted approach to generating responses that feel natural while strategically extracting information:

### 1. Hint System
Before each reply, the system determines what intelligence is **still missing** and generates a "hint" for the AI:
- If no phishing link has been captured yet, the hint might be: *"ask about the verification link"*
- If no UPI ID has been extracted, the hint might be: *"ask for the UPI ID"*
- The order of priority changes based on context (e.g., if the scammer mentions KYC, link-related hints come first)

### 2. Dynamic System Prompt
The AI receives a system prompt that includes:
- Persona instructions ("sound worried and confused, but cooperative")
- Strict rules ("never say scam, fraud, AI, bot, or honeypot")
- The current hint ("preferred question topic: UPI ID")
- Rubric targets ("you still need to ask 3 more questions by turn 8")

### 3. Safety Guardrails
Every response passes through multiple checks:
- **Banned word removal**: Any mention of "honeypot", "bot", "AI", "fraud", or "scam" is automatically stripped
- **Single question enforcement**: If the AI generates multiple questions, only the first is kept
- **Length cap**: Responses over 200 characters are truncated
- **Minimum rubric enforcement**: On specific turns (1, 2, 3, 5, 7), if the conversation is behind on targets, a natural follow-up question is added

---

## 🏷️ Final Output & Scam Classification

When the conversation reaches turn 8-10 and enough intelligence has been gathered, NIRIKSHA.ai generates a comprehensive final report:

### LLM-Based Scam Classification
A separate AI call analyzes the **entire conversation** and classifies it into one of 9 categories:

| Category | Description |
|----------|-------------|
| `bank_fraud` | Fake bank warnings, account blocking threats |
| `upi_fraud` | Fake cashback offers, UPI payment scams |
| `phishing` | Fake websites, link-based attacks |
| `job_scam` | Fake job offers requiring upfront payment |
| `investment_scam` | Fake investment schemes promising returns |
| `lottery_scam` | Fake lottery/prize winning notifications |
| `kyc_scam` | Fake KYC verification requests |
| `utility_scam` | Fake utility bill payment scams |
| `unknown` | Unclassifiable scam patterns |

### Final Report Format
```json
{
  "sessionId": "unique-session-id",
  "status": "completed",
  "scamDetected": true,
  "totalMessagesExchanged": 12,
  "engagementDurationSeconds": 195,
  "scamType": "bank_fraud",
  "confidenceLevel": 0.92,
  "extractedIntelligence": {
    "phoneNumbers": ["+919876543210"],
    "bankAccounts": ["1234567890123456"],
    "upiIds": ["scammer.fraud@fakebank"],
    "phishingLinks": ["http://amaz0n-deals.fake-site.com/claim?id=12345"],
    "emailAddresses": ["offers@fake-amazon-deals.com"],
    "caseIds": ["CASE-12345"],
    "policyNumbers": [],
    "orderNumbers": [],
    "referenceIds": ["CASE-12345"]
  },
  "engagementMetrics": {
    "totalMessagesExchanged": 12,
    "engagementDurationSeconds": 195
  },
  "agentNotes": "Session completed. scamType=bank_fraud."
}
```

---

## 🧠 Engagement Strategy — The Psychology Behind NIRIKSHA.ai

Scammers operate on **urgency** and **fear** — they demand immediate action. NIRIKSHA.ai counters this with **cautious confusion** and **cooperative curiosity**:

### The Persona: A Confused But Willing Victim
The AI plays the role of a worried, slightly confused person who **wants to cooperate** but needs more information before they can act. This is the perfect trap because:

1. **The scammer stays engaged** — The target seems willing to comply, so the scammer keeps investing time
2. **Intelligence flows naturally** — By asking "How should I pay?" or "What's the reference number?", scammers voluntarily give up their UPI IDs, account numbers, and fake reference numbers
3. **Time is wasted** — Each conversation costs the scammer 5-15 minutes they can't spend on real victims
4. **No detection risk** — The persona never accuses, investigates using technical language, or reveals awareness

### What the AI Does:
| Behavior | Example Response |
|----------|-----------------|
| Express concern | "Oh no, that sounds serious..." |
| Ask for details naturally | "How should I make the payment?" |
| Request verification | "Is there a reference number I can check?" |
| Show cooperation | "Okay, I want to do it right. Where do I send it?" |
| Hesitate naturally | "I'm not sure about this... can you confirm?" |

### What the AI Never Does:
- ❌ Never shares OTPs, PINs, CVVs, or passwords
- ❌ Never says "scam", "fraud", "AI", "bot", or "honeypot"
- ❌ Never acts like an investigator or authority figure
- ❌ Never asks more than one question per reply

---

## 🛠️ Tech Stack

| Component | Technology | Why We Chose It |
|-----------|-----------|----------------|
| **Language** | Python 3.10+ | Widely supported, rich ecosystem for AI/NLP |
| **API Framework** | FastAPI | High-performance async framework with auto-generated docs |
| **LLM Provider** | Groq Cloud | Ultra-fast inference (under 1 second), supports large models |
| **LLM Model** | Meta Llama 3.3 70B Versatile | One of the best open-source language models for natural conversation |
| **Server** | Uvicorn | ASGI server optimized for async Python applications |
| **Data Validation** | Pydantic v2 | Robust request/response validation with alias support |
| **Pattern Matching** | Python `re` (Regex) | Powerful text pattern extraction without external dependencies |
| **Environment** | python-dotenv | Secure API key management through .env files |
| **HTTP Client** | Requests | Lightweight HTTP client for callback reporting |
| **Deployment** | Railway | One-click cloud deployment with HTTPS |

---

## 📁 Project Structure

```
Agentic-Honey-Pot-for-Scam-Detection-Intelligence-Extraction/
│
├── README.md                           # This documentation file
├── .gitignore                          # Git ignore rules
│
├── honeypot-api/                       # 🔥 Core API source code
│   │
│   ├── main.py                         # Main FastAPI application (614 lines)
│   │   ├── Section 1: Config           #   Environment setup & API initialization
│   │   ├── Section 2: Session State    #   In-memory conversation tracking
│   │   ├── Section 3: Models           #   Pydantic request/response schemas
│   │   ├── Section 4: Patterns         #   Regex patterns for entity extraction
│   │   ├── Section 5: Scam Score       #   Weighted risk scoring engine
│   │   ├── Section 6: Extraction       #   Intelligence extraction pipeline
│   │   ├── Section 7: LLM Reply        #   AI response generation + guardrails
│   │   ├── Section 8: Final Output     #   Scam classification + report builder
│   │   ├── Section 9: Endpoint         #   POST /api/detect handler
│   │   └── Section 10: Run             #   Server startup
│   │
│   ├── app/                            # 📦 Modular version (same logic, split files)
│   │   ├── config.py                   #   Configuration & environment variables
│   │   ├── schemas.py                  #   Pydantic models
│   │   ├── patterns.py                 #   Regex patterns
│   │   ├── scoring.py                  #   Scam scoring engine
│   │   ├── extraction.py               #   Intelligence extraction
│   │   ├── replies.py                  #   LLM response generation
│   │   ├── llm_client.py               #   Groq API client
│   │   ├── session_store.py            #   Session management
│   │   ├── state.py                    #   Global state
│   │   ├── service.py                  #   Business logic
│   │   └── models.py                   #   Data models
│   │
│   ├── requirements.txt                # Python dependencies
│   ├── .env                            # Environment variables (gitignored)
│   ├── .gitignore                      # API-specific gitignore
│   │
│   └── tests/                          # 🧪 Comprehensive test suite
│       ├── test_api.py                 # Sample payload for quick testing
│       ├── test_chat.py                # Interactive multi-turn chat tester
│       ├── trigger_spy.py              # Single-shot authenticated test
│       ├── verify_system.py            # Full pre-deployment verification
│       ├── gpt_test.py                 # Extended GPT-based test scenarios
│       ├── offline_test.py             # Offline test runner
│       ├── testings.py                 # Comprehensive scenario testing
│       ├── xx.py                       # Additional test utilities
│       ├── list_model.py               # Available model checker
│       ├── honeypot_test_report.json   # Test result records
│       ├── honeypot_test_report_v2.json# Updated test results
│       └── pdf_self_test_report.json   # Self-evaluation results
│
├── Technical Docs/                     # 📄 Hackathon documentation & screenshots
│
└── test_results/                       # 📊 Evaluation results
```

---

## 🚀 Setup & Installation

### What You'll Need Before Starting
- **Python 3.10 or higher** installed on your computer (download from [python.org](https://python.org))
- A **Groq Cloud API Key** (free signup at [console.groq.com/keys](https://console.groq.com/keys))
- **Git** installed (download from [git-scm.com](https://git-scm.com))

### Step 1: Download the Code
```bash
git clone https://github.com/official-vanshaj-garg/Agentic-Honey-Pot-for-Scam-Detection-Intelligence-Extraction.git
cd Agentic-Honey-Pot-for-Scam-Detection-Intelligence-Extraction/honeypot-api
```

### Step 2: Create a Virtual Environment
A virtual environment keeps this project's dependencies separate from your other Python projects.
```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On Mac/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
| Package | What It Does |
|---------|-------------|
| `fastapi` | The web framework that handles incoming API requests |
| `uvicorn` | The server that runs the FastAPI application |
| `groq` | The SDK that connects to Groq Cloud for AI responses |
| `pydantic` | Validates incoming data to make sure it's in the right format |
| `python-dotenv` | Reads your API key from the `.env` file |
| `requests` | Sends HTTP requests (used for callback reporting) |

### Step 4: Set Up Your API Key
Create a file called `.env` in the `honeypot-api/` folder:
```env
GROQ_API_KEY=gsk_your_groq_api_key_here
```
You can also customize these optional settings:
```env
GROQ_MODEL=llama-3.3-70b-versatile    # Which AI model to use
API_SECRET_TOKEN=your-secret-key       # API authentication key
MIN_HUMAN_DELAY_S=0.10                 # Minimum response delay (seconds)
MAX_HUMAN_DELAY_S=0.28                 # Maximum response delay (seconds)
PORT=8000                              # Server port number
```

> ⚠️ **Important:** Never share or commit your actual API key. Add `.env` to your `.gitignore` file.

### Step 5: Start the Server
```bash
# For development (auto-reloads when you change code):
uvicorn main:app --reload

# For production:
python main.py
```
The server will start at `http://127.0.0.1:8000`.

### Step 6: Test It Works
Open a new terminal and run:
```bash
cd tests
python verify_system.py
```
You should see all three tests pass (✅).

---

## 📡 API Documentation

### Endpoint: `POST /api/detect`

This is the main endpoint that receives scammer messages and returns AI-generated responses.

### Request Headers

| Header | Value | Required |
|--------|-------|----------|
| `x-api-key` | Your API secret token | ✅ Yes |
| `Content-Type` | `application/json` | ✅ Yes |

### Request Body

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
  ],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `sessionId` | string | Yes | A unique ID for this conversation. Used to track state across turns. |
| `message.sender` | string | Yes | Must be `"scammer"` for the system to respond. |
| `message.text` | string | Yes | The scammer's latest message. |
| `conversationHistory` | array | No | All previous messages in this conversation. Helps the AI understand context. |
| `metadata` | object | No | Optional info about the communication channel (SMS, WhatsApp, Email). |

### Response Body

**During conversation (before final report):**
```json
{
  "status": "success",
  "reply": "Oh no, that sounds serious. How do I verify this?",
  "finalCallback": null,
  "finalOutput": null
}
```

**After final report is triggered (turn 8-10+):**
```json
{
  "status": "success",
  "reply": "Okay, let me try once more...",
  "finalCallback": {
    "sessionId": "unique-session-id-123",
    "status": "completed",
    "scamDetected": true,
    "scamType": "bank_fraud",
    "confidenceLevel": 0.92,
    "totalMessagesExchanged": 12,
    "engagementDurationSeconds": 195,
    "extractedIntelligence": { ... },
    "engagementMetrics": { ... },
    "agentNotes": "Session completed. scamType=bank_fraud."
  },
  "finalOutput": { ... }
}
```

### Error Responses

| Status | When | Response |
|--------|------|----------|
| `403 Forbidden` | Wrong or missing API key | `{"detail": "Invalid API Key"}` |
| `422 Unprocessable Entity` | Malformed request body | `{"detail": [validation errors]}` |

### cURL Example
```bash
curl -X POST https://your-deployed-url.com/api/detect \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-api-key-here" \
  -d '{
    "sessionId": "test-001",
    "message": {
      "sender": "scammer",
      "text": "Your account is blocked. Send OTP now.",
      "timestamp": 1700000000
    },
    "conversationHistory": []
  }'
```

---

## 🎯 Sample Scenarios Handled

NIRIKSHA.ai is built with **generic detection logic** (no hardcoded test responses). It handles any type of scam naturally. Here are three representative scenarios:

### Scenario 1: 🏦 Bank Fraud Detection

| | Details |
|---|---|
| **Channel** | SMS |
| **Scam Type** | Bank account fraud with urgency tactics |
| **Initial Message** | *"URGENT: Your SBI account has been compromised. Your account will be blocked in 2 hours. Share your account number and OTP immediately to verify your identity."* |
| **NIRIKSHA.ai's Strategy** | Express concern about account safety ➜ Ask for employee ID/reference number ➜ Request callback number ➜ Ask which branch this is from ➜ Keep delaying with "checking" excuses |
| **Intelligence Extracted** | Bank accounts, phone numbers, UPI IDs, reference IDs |

### Scenario 2: 💰 UPI Fraud (Cashback Scam)

| | Details |
|---|---|
| **Channel** | WhatsApp |
| **Scam Type** | UPI fraud with fake cashback offer |
| **Initial Message** | *"Congratulations! You have won a cashback of Rs. 5000 from Paytm. To claim your reward, please verify your UPI details. This is from official customer support."* |
| **NIRIKSHA.ai's Strategy** | Show excitement about winning ➜ Ask "how to claim" ➜ Request UPI payment details naturally ➜ Ask for verification link ➜ Question the reference number |
| **Intelligence Extracted** | UPI IDs, phone numbers, email addresses |

### Scenario 3: 🔗 Phishing Link Detection

| | Details |
|---|---|
| **Channel** | Email |
| **Scam Type** | Phishing with fake e-commerce deal |
| **Initial Message** | *"You have been selected for iPhone 15 Pro at just Rs. 999! Click here to claim: http://amaz0n-deals.fake-site.com/claim?id=12345. Offer expires in 10 minutes!"* |
| **NIRIKSHA.ai's Strategy** | Express interest ➜ Ask about the offer details ➜ Question the link's legitimacy naturally ➜ Ask for official email/phone ➜ Request order reference number |
| **Intelligence Extracted** | Phishing links, email addresses, order numbers |

---

## 📊 Evaluation & Scoring

NIRIKSHA.ai is evaluated across multiple dimensions by the hackathon's automated testing system:

### Scoring Categories

| Category | What It Measures | How NIRIKSHA.ai Scores Well |
|----------|-----------------|---------------------------|
| **Scam Detection** | Did the system correctly identify the fraud? | Weighted scoring system catches all common scam patterns |
| **Intelligence Extraction** | How many entities (UPI IDs, phones, etc.) were captured? | 7-type extraction pipeline with smart filtering |
| **Conversation Engagement** | How many turns was the scammer kept talking? | Hint system + cooperative persona keeps scammers engaged for 10+ turns |
| **Response Quality** | Are responses natural, non-repetitive, and strategic? | LLM generates unique responses with rubric-aware adjustments |
| **Scam Classification** | Was the scam type correctly identified? | Separate LLM classification call with confidence scoring |

### Deployment Details

| | |
|---|---|
| **Live Endpoint** | `https://agentichoneypot-production-12fb.up.railway.app/api/detect` |
| **Authentication** | `x-api-key` header |
| **Response Time** | 1-3 seconds (includes human delay simulation) |
| **Max Turns** | 10+ per session |

---

## 🧪 Test Results & Proof of Work

### Pre-Deployment Verification (`tests/verify_system.py`)
- ✅ **Standard Handshake** — First-contact scam handled correctly
- ✅ **Intelligence Extraction** — UPI IDs and phishing links captured
- ✅ **Garbage Input Resilience** — Non-standard characters handled without crashes

### Interactive Chat Testing (`tests/test_chat.py`)
- Multi-turn conversations maintained across 10+ turns
- Context preserved through conversation history
- Final intelligence report generated with complete extraction

### Automated Test Reports
- `honeypot_test_report.json` — Initial evaluation results
- `honeypot_test_report_v2.json` — Updated evaluation with expanded scenarios
- `pdf_self_test_report.json` — Self-evaluation against official documentation

### Local Testing Score
- **100/100** achieved in local testing against all three official scenarios

---

## 🔮 Future Roadmap

| Feature | Description | Status |
|---------|-------------|--------|
| 🗣️ **Voice Call Integration** | VAPI integration so NIRIKSHA.ai can handle actual phone call scams | 🔬 Planned |
| 🖼️ **Image & QR Analysis** | Use vision models to analyze screenshots, fake ID cards, and QR codes | 🔬 Planned |
| 🌐 **Multi-Language Support** | Hindi, Tamil, Telugu, and other Indian regional languages | 🔬 Planned |
| 👥 **Multi-Persona System** | Switch between personas (elderly victim, young student, working professional) | 🔬 Planned |
| 📊 **Live Dashboard** | Real-time web dashboard showing active sessions and extracted intelligence | 🔬 Planned |
| 🤝 **Law Enforcement API** | Direct integration with Indian Cyber Crime Portal | 🔬 Planned |
| 🔁 **Continuous Learning** | Feedback loop to improve responses based on scammer behavior patterns | 🔬 Planned |

---

## 📜 Approach Summary

NIRIKSHA.ai is built on a simple but powerful philosophy: **make scam attempts work against the scammer.**

Instead of simply blocking (which costs the scammer nothing), we:
1. **Engage** — Respond like a real potential victim to keep the scammer invested
2. **Extract** — Silently capture every piece of shared financial information
3. **Classify** — Use AI to identify the type and severity of the scam
4. **Report** — Automatically compile and submit structured intelligence reports
5. **Waste Time** — Every minute with NIRIKSHA.ai is a minute not spent scamming a real person

This is not just another scam detector. It's a **counter-offensive tool** in the fight against India's ₹11,333 Crore cybercrime crisis.

---

## 👥 Team — BRATS

<table>
  <tr>
    <td align="center"><b>Vanshaj Garg</b><br/>📧 <a href="mailto:official.vanshaj.garg@gmail.com">official.vanshaj.garg@gmail.com</a><br/>🔗 <a href="https://www.linkedin.com/in/vanshajgargg">LinkedIn</a></td>
    <td align="center"><b>Abhishek Rajput</b><br/>📧 <a href="mailto:rajputabhishek512@gmail.com">rajputabhishek512@gmail.com</a><br/>🔗 <a href="https://www.linkedin.com/in/abhi-99-rajput/">LinkedIn</a></td>
    <td align="center"><b>Abhay Raj Yadav</b><br/>📧 <a href="mailto:19abhay26@gmail.com">19abhay26@gmail.com</a><br/>🔗 <a href="https://www.linkedin.com/in/contactabhayraj">LinkedIn</a></td>
  </tr>
</table>

---

## 📄 License

This project was built for the **India AI Impact Buildathon 2026** organized by **HCL GUVI** under the **India AI Impact Summit**.

---

<p align="center">
  <b>🛡️ NIRIKSHA.ai</b><br/>
  <i>Because the best defense is making the attacker's offense work against them.</i><br/><br/>
  <b>Fighting scams. Extracting intelligence. Wasting scammer time.</b>
</p>
