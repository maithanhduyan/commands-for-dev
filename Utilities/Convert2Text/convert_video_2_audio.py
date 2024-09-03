import moviepy.editor as mp

# Load the video file
video_path = f"./mnt/data/video.mp4"
video = mp.VideoFileClip(video_path)

# Extract audio and convert it to text
audio = video.audio

# Save the audio to a file
audio_path = f"./mnt/data/audio1.wav"
audio.write_audiofile(audio_path)

audio_path
