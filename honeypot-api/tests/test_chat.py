import requests
import time
import uuid

API_URL = "http://127.0.0.1:8000/api/detect"
API_KEY = "guvi-hackathon-secret-123"

session_id = str(uuid.uuid4())
conversation_history = []

print("🧪 Honeypot Test Chat Started")
print("Type 'exit' to quit\n")

while True:
    user_input = input("🕵️ Scammer: ")
    if user_input.lower() == "exit":
        print("Exiting chat.")
        break

    payload = {
        "sessionId": session_id,
        "text": user_input,
        "sender": "scammer",
        "conversationHistory": conversation_history
    }

    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code != 200:
        print("❌ Error:", response.text)
        break

    data = response.json()
    reply = data["reply"]

    print("👤 User:", reply)

    conversation_history.append({
        "sender": "scammer",
        "text": user_input,
        "timestamp": int(time.time())
    })

    conversation_history.append({
        "sender": "assistant",
        "text": reply,
        "timestamp": int(time.time())
    })

