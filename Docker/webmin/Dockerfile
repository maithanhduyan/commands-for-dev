# Sử dụng Debian image
FROM debian:latest

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2

# Thêm repo Webmin và cài đặt
RUN echo "deb http://download.webmin.com/download/repository sarge contrib" > /etc/apt/sources.list.d/webmin.list && \
    wget -qO - http://www.webmin.com/jcameron-key.asc | apt-key add - && \
    apt-get update && \
    apt-get install -y webmin

# Mở cổng 10000 để truy cập Webmin
EXPOSE 10000

# Khởi chạy Webmin khi container được khởi động
CMD ["/usr/bin/perl", "/usr/share/webmin/miniserv.pl", "/etc/webmin/miniserv.conf"]
