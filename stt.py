import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak something in Tamil...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="ta-IN")
        print("📝 You said:", text)
        return text
    except:
        print("❌ Could not recognize speech")
        return None