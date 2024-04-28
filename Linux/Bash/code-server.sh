#!/bin/bash

# Trên Ubuntu, Debian chuẩn bị
sudo apt-get install -y \
  curl \
  git \
  build-essential \
  pkg-config \
  python3

mkdir -p /home/coder/code-server
# Clone mã nguồn code-server
git clone https://github.com/coder/code-server /home/coder/code-server

echo "Tải source code-server hoàn tất"

# Di chuyển vào thư mục code-server
cd /home/coder/code-server

sh install.sh

echo "Đã cài đặt code-server hoàn tất."

# Khởi động code-server
#code-server 

# Khởi động code-server không password
#code-server --auth none

# Khởi động code-server cho phép user truy cập từ internet (all IP)
#code-server --bind-addr=0.0.0.0:8080
# 099ef5d578f69473ba5ac35f