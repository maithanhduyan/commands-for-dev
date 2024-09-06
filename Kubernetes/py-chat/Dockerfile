# Sử dụng Ubuntu 22.04 làm base image
FROM ubuntu:22.04

# Cập nhật các package và cài đặt Python, pip, và các công cụ cần thiết để build các gói Python
RUN apt-get update && apt-get install -y \
    python3 python3-pip build-essential python3-dev libffi-dev \
    && apt-get clean

# Tạo thư mục cho ứng dụng
WORKDIR /app

# Sao chép các file yêu cầu vào image
COPY requirements.txt requirements.txt

# Cài đặt các package Python từ file requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn ứng dụng vào thư mục /app
COPY . .

# Chạy ứng dụng Python
CMD ["python3", "app.py"]
