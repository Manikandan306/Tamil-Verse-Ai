from stt import recognize_speech
from responses import get_response
from tts import speak_text

if __name__ == "__main__":
    user_input = recognize_speech()
    if user_input:
        response = get_response(user_input)
        print("🤖 AI Response:", response)
        speak_text(response)
