from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def speak_text(text):
    tts = gTTS(text=text, lang="ta")
    filename = "response.mp3"
    tts.save(filename)
    
    # Convert to audio segment and play
    audio = AudioSegment.from_mp3(filename)
    play(audio)
    
    os.remove(filename)  # Delete after playing
