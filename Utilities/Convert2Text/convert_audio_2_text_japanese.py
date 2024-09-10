import speech_recognition as sr
import os

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Load the audio file
audio_file_path = f"./mnt/data/beha.wav"
audio_file = sr.AudioFile(audio_file_path)

# Convert the audio to text
with audio_file as source:
    audio = r.record(source)
    text = r.recognize_google(audio, language="ja-JP")

# print(text)

def generate_text_file( markdown_file):
    with open(markdown_file, 'w', encoding='utf-8') as f:
        # f.write(f"# You are an intelligent programming assistant.\n")
        f.write(text)

text_file_path = f"./mnt/data/beha.txt"
generate_text_file(text_file_path)