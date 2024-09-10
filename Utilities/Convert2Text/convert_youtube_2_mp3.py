from pytube import YouTube
from pydub import AudioSegment
import os

# Hàm tải video từ YouTube và chuyển đổi sang file âm thanh
def download_audio_from_youtube(url, output_format='mp3'):
    try:
        # Tạo đối tượng YouTube
        yt = YouTube(url)

        # Tải video ở định dạng âm thanh (audio)
        stream = yt.streams.filter(only_audio=True).first()

        # Đường dẫn tải về
        download_path = stream.download()

        # Chuyển đổi file tải về thành định dạng âm thanh
        audio = AudioSegment.from_file(download_path)

        # Đặt tên file đầu ra
        output_file = os.path.splitext(download_path)[0] + f".{output_format}"

        # Xuất file âm thanh
        audio.export(output_file, format=output_format)

        # Xóa file video gốc sau khi chuyển đổi (nếu không cần thiết)
        os.remove(download_path)

        print(f"Tải xuống và chuyển đổi hoàn tất! File âm thanh lưu tại: {output_file}")
    
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")


# Thay thế link của bạn vào đây
youtube_url = "https://www.youtube.com/watch?v=fnpeGE0gU10"

# Gọi hàm để tải và chuyển đổi
download_audio_from_youtube(youtube_url, output_format='mp3')
