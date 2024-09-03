from TTS.api import TTS

# Load model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC_ph", progress_bar=True)

# Convert text to speech
tts.tts_to_file(text="Hello, this is a test of Coqui TTS.", file_path=f"./mnt/data/text2speech_output.wav")