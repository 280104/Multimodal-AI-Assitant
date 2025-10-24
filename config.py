import os
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
if not GEMINI_API_KEY:
    raise ValueError("Set GEMINI_API_KEY environment variable before running.")
genai.configure(api_key=GEMINI_API_KEY)

