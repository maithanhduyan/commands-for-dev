from pydub import AudioSegment

# Đường dẫn đến file .m4a đầu vào
input_file_path = f"./mnt/data/input_file.m4a"

# Đường dẫn đến file đầu ra với định dạng WAV
output_file_path = f"./mnt/data/output_file.wav"

# Chuyển đổi file âm thanh từ .m4a sang .wav
audio = AudioSegment.from_file(input_file_path, format="m4a")
audio.export(output_file_path, format="wav")
