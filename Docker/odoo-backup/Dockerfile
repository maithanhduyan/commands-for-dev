# Sử dụng image Python 3.9
FROM python:3.9-slim

# Cài đặt thư viện requests
RUN pip install requests
RUN pip install schedule

# Thêm file backup.py vào container
ADD app.py /
ADD backup.conf /

# Chạy đoạn code khi container được khởi chạy
CMD ["python", "/app.py"]
