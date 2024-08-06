import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Load the audio file
audio_path = ".Convert2Text/media/11831.m4a"

# Recognize the speech from the audio file
with sr.AudioFile(audio_path) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data, language='vi-VN')

print(text)