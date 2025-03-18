import asyncio
from stt import recognize_speech 
from responses import get_response
from tts import speak_now  # Using speak_now to properly handle async calls

if __name__ == "__main__":
    user_input = recognize_speech()
    if user_input:
        response = get_response(user_input)
        print("🤖 AI Response:", response)
        speak_now(response)  # This ensures async execution
