# Sử dụng Python 3.12 làm base image
FROM python:3.12-slim

WORKDIR /app

# Cài đặt curl và các phụ thuộc cần thiết
RUN apt-get update && apt-get install -y curl && apt-get clean

# Cập nhật pip
RUN pip install --upgrade pip

# Cài đặt các thư viện cần thiết
RUN pip install openai \
    google-generativeai \
    ollama \
    requests \
    selenium


COPY . .

VOLUME ["/app"]

# Mount thư mục bên ngoài vào /app/config để lấy file app.config
VOLUME ["/app/config"]

# Chờ Selenium server khởi động
ENTRYPOINT ["./docker/entrypoint.sh"]

# Lệnh mặc định khi container được khởi động
CMD ["python3","app.py"]
