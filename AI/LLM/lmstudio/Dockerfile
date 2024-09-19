# Sử dụng image Python 3.12-alpine3.19
FROM python:3.12-alpine3.19

# Update pip
RUN python -m pip install --upgrade pip
# Cài đặt thư viện requests, schedule
RUN pip install requests
RUN pip install openai

# Thêm file backup.py vào container
ADD app.py /
ADD backup.conf /

# Chạy đoạn code khi container được khởi chạy
CMD ["python", "/app.py"]
