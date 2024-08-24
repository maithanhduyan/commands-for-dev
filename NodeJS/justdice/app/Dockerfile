# Sử dụng Node.js LTS làm base image
FROM node:lts

# Set thư mục làm việc trong container
WORKDIR /app

# Sao chép file package.json và package-lock.json vào container
COPY package*.json ./

# Cài đặt các dependencies
RUN npm install --production

# Sao chép toàn bộ mã nguồn của dự án vào container
COPY . .

# Expose cổng mà ứng dụng của bạn sẽ chạy
EXPOSE 1337

# Lệnh để chạy ứng dụng khi container khởi động
CMD ["node", "app.js"]
