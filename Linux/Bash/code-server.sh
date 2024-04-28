#!/bin/bash

# Trên Ubuntu, Debian chuẩn bị
sudo apt-get install -y \
  build-essential \
  pkg-config \
  python3
  
# 2024-04-28 NOT USE ------------------------------------------------------------
# # cài nodejs version 18
# # echo 'Cài đặt Node Version Manager - nvm'
# curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
 
# nvm install 18
# # Sau khi chạy đoạn script: 'nvm install 18' mặc định sẽ sử dụng nodejs version 18.
# # Để chắc chắn hệ thống đang sử dụng version 18 hay chưa thì dùng
# nvm use 18
# 2024-04-28 NOT USE ------------------------------------------------------------

# Clone mã nguồn code-server
git clone https://github.com/coder/code-server /home/coder/code-server
# echo 'OK'

# Di chuyển vào thư mục code-server
cd /home/coder/code-server

# Cài yarn
# npm install --global yarn

# Cài đặt code-server
npm install -g code-server

# Khởi động code-server
code-server 

# Khởi động code-server không password
code-server --auth none

# Khởi động code-server cho phép user truy cập từ internet (all IP)
code-server --bind-addr=0.0.0.0:8080