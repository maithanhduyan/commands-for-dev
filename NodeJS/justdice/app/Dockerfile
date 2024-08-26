# Sử dụng node:16 làm image cơ sở
FROM node:lts-bookworm

# Cài đặt mysql-client
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*


# Tạo thư mục làm việc cho ứng dụng
WORKDIR /app

# Sao chép package.json và package-lock.json (nếu có) vào image
COPY package*.json ./

# Cài đặt dependencies
RUN npm install

# Sao chép toàn bộ mã nguồn của ứng dụng vào image
COPY . .

# Sao chép script kiểm tra MySQL
COPY wait-for-mysql.sh /app/wait-for-mysql.sh
RUN chmod +x /app/wait-for-mysql.sh

# NODE EVIRONMENT 
ENV NODE_ENV=development

# Mở cổng 3000 để ứng dụng lắng nghe
EXPOSE 3000

# Chạy ứng dụng khi container được khởi động, kiểm tra MySQL trước
ENTRYPOINT [ "./wait-for-mysql.sh" ]
CMD ["node", "app.js"]