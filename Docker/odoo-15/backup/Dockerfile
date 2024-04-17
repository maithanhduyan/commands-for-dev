# Sử dụng image Python 3.9
FROM python:3.9-slim

# Update pip
RUN python -m pip install --upgrade pip
# Cài đặt thư viện requests, schedule
RUN pip install requests
RUN pip install schedule

# Thêm file backup.py vào container
COPY ./backup/app.py /
COPY ./backup/backup.conf /

# Chạy đoạn code khi container được khởi chạy
CMD ["python", "/app.py"]
