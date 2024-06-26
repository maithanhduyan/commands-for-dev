# Sử dụng image Python 3.9
FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Tạo thư mục cho Odoo
RUN mkdir -p /odoo-backup

# Đặt thư mục làm working directory
WORKDIR /odoo-backup

# Update pip
RUN python3.9 -m pip install --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel
# Cài đặt thư viện requests, schedule
RUN python3.9 -m pip install --no-cache-dir \
    requests \
    schedule

    COPY . .

#EXPOSE 5000

COPY . .

# Chạy đoạn code khi container được khởi chạy
CMD ["python3.9", "app.py"]
