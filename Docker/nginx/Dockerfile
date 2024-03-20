# Sử dụng image Alpine làm base
FROM alpine:latest

# Cài đặt Nginx
RUN apk update && apk add --no-cache nginx

# Copy nội dung trang web vào thư mục www/html trong container
COPY ./www /var/www/html

# Copy file cấu hình Nginx vào container
COPY ./conf/nginx.conf /etc/nginx/nginx.conf

# Mở cổng 80 để truy cập web server
EXPOSE 80

# Khởi chạy Nginx
CMD ["nginx", "-g", "daemon off;"]