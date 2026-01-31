import requests
import json
import time

# 1. Define the URL (Keep your ngrok link)
url = "https://bd187e6cfcff.ngrok-free.app/api/detect"

# 2. Define the Secret Key (MUST match what is in main.py)
API_KEY = "guvi-hackathon-secret-123"

# 3. Define the Headers (Crucial Step for PDF Compliance)
headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY  # This solves requirement [Source: 18]
}

# 4. Define the Scam Payload
payload = {
    "sessionld": "spy-test-session",
    "sender": "scammer",
    "text": "URGENT: Send 5000 INR to scammer@oksbi or your card is blocked!",
    "timestamp": "2026-01-21T10:15:30Z",
    "conversationHistory": []
}

print("\n🔫 FIRING SECURE TRIGGER AT HONEYPOT...")

try:
    # 5. Send the request WITH HEADERS
    response = requests.post(url, json=payload, headers=headers)
    
    # 6. Print the result
    if response.status_code == 200:
        data = response.json()
        print("✅ SUCCESS! Access Granted.")
        print(f"🗣️ Martha said: '{data['reply']}'")
        print("\n👀 Check Server Terminal for '🚨 CAUGHT upiIds'")
    elif response.status_code == 403:
        print("⛔ FAILED: 403 Forbidden. Did you set the right API Key?")
    else:
        print(f"❌ Server Error: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"\n❌ FAILED TO CONNECT: {e}")