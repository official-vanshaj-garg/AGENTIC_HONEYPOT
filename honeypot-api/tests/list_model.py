import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: No API Key found in .env")
else:
    genai.configure(api_key=api_key)
    print("🔹 Contacting Google to list available models for your key...")
    
    try:
        models = genai.list_models()
        found_any = False
        for m in models:
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ AVAILABLE: {m.name}")
                found_any = True
        
        if not found_any:
            print("❌ No text generation models found. Your key might be restricted?")
            
    except Exception as e:
        print(f"❌ Error listing models: {e}")