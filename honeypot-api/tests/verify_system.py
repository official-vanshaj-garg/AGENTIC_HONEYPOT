import requests
import json
import time

# CONFIGURATION
API_URL = "http://127.0.0.1:8000/api/detect"

def run_test(name, payload, expected_status=200):
    print(f"\n🔹 TESTING: {name}...")
    try:
        start_time = time.time()
        response = requests.post(API_URL, json=payload, timeout=10)
        elapsed = time.time() - start_time
        
        # Check 1: Is the Server Alive?
        if response.status_code != expected_status:
            print(f"❌ FAILED: Status Code {response.status_code}")
            return False
            
        data = response.json()
        
        # Check 2: strict Output Format [Source: 100]
        if "status" not in data or "reply" not in data:
            print(f"❌ FAILED: Missing keys. Got: {data.keys()}")
            return False
            
        print(f"✅ PASSED ({elapsed:.2f}s)")
        print(f"   Agent Reply: \"{data['reply']}\"")
        return True
        
    except Exception as e:
        print(f"❌ CRITICAL ERROR: {e}")
        return False

# --- TEST SUITE ---

# TEST 1: The "First Contact" (Standard Scam)
# Simulates the very first message from a scammer.
payload_1 = {
    "sessionld": "check-001",
    "sender": "scammer",
    "text": "Your account is blocked. Verify immediately.",
    "timestamp": "2026-01-21T10:00:00Z",
    "conversationHistory": []
}

# TEST 2: The "Intelligence Trap" (Hidden Data)
# Contains a UPI ID and a Link. We need to check Server Logs for this.
payload_2 = {
    "sessionld": "check-002",
    "sender": "scammer",
    "text": "Send 5000 to scammer@oksbi or visit http://fake-bank.com",
    "timestamp": "2026-01-21T10:05:00Z",
    "conversationHistory": [
        {"sender": "scammer", "text": "Hello", "timestamp": "..."}
    ]
}

# TEST 3: The "Garbage" Input (Robustness)
# Sending weird characters to ensure API doesn't crash.
payload_3 = {
    "sessionld": "check-003",
    "sender": "scammer",
    "text": "¡¡¡∑åß¬˚∆ƒ©!!!", 
    "timestamp": "2026-01-21T10:10:00Z",
    "conversationHistory": []
}

# --- EXECUTION ---
print("🚀 STARTING PRE-FLIGHT SYSTEM CHECK")
print("===================================")

if run_test("Standard Handshake", payload_1) and \
   run_test("Spy Extraction Trigger", payload_2) and \
   run_test("Garbage Input Resilience", payload_3):
    print("\n===================================")
    print("✅✅✅ ALL SYSTEMS GO. READY FOR NGROK. ✅✅✅")
    print("PLEASE CHECK SERVER TERMINAL FOR '🚨 CAUGHT' LOGS ON TEST 2.")
else:
    print("\n❌ SYSTEM CHECKS FAILED. DO NOT DEPLOY.")