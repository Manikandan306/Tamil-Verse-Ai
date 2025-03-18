import asyncio
import edge_tts
from playsound import playsound
import os

async def speak_text(text):
    voice = "ta-IN-PallaviNeural"  # Tamil voice
    filename = "response.mp3"

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

    playsound(filename)  # Play in VS Code terminal
    os.remove(filename)  # Delete file after playing

def speak_now(text):
    asyncio.run(speak_text(text))  # Ensure async execution
