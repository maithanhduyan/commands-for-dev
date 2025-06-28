# Dockerfile lightweight - sử dụng pre-built image với customization
FROM ubuntu:22.04 AS runtime

# Thiết lập biến môi trường
ENV DEBIAN_FRONTEND=noninteractive

# Cài đặt các packages cần thiết cho runtime
RUN apt-get update && apt-get install -y \
    qemu-system-x86 \
    qemu-utils \
    socat \
    bridge-utils \
    iproute2 \
    iptables \
    curl \
    wget \
    nano \
    unzip \
    gzip \
    && rm -rf /var/lib/apt/lists/*

# Tạo thư mục cho OpenWRT
RUN mkdir -p /opt/openwrt

# Download pre-built OpenWRT image
RUN cd /opt/openwrt && \
    wget -c https://downloads.openwrt.org/releases/23.05.5/targets/x86/64/openwrt-23.05.5-x86-64-generic-ext4-combined.img.gz || \
    wget -c https://downloads.openwrt.org/releases/23.05.4/targets/x86/64/openwrt-23.05.4-x86-64-generic-ext4-combined.img.gz || \
    wget -c https://downloads.openwrt.org/releases/23.05.3/targets/x86/64/openwrt-23.05.3-x86-64-generic-ext4-combined.img.gz

# Copy script khởi động
COPY --chown=root:root start-openwrt.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start-openwrt.sh

# Expose các port cần thiết
EXPOSE 22 80 443 8080

# Thiết lập working directory
WORKDIR /opt/openwrt

# Command mặc định
CMD ["/usr/local/bin/start-openwrt.sh"]
