import whisper

model = whisper.load_model("turbo")
result = model.transcribe("/data/tamlyhoctienbac.mp3")
print(result["text"])