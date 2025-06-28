#!/bin/bash

# Script khởi động OpenWRT trong Docker container

# Thiết lập màu cho output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${GREEN}=======================================${NC}"
echo -e "${GREEN}    OpenWRT Docker Container Started   ${NC}"
echo -e "${GREEN}=======================================${NC}"

# Kiểm tra xem có file image OpenWRT không
OPENWRT_IMG=$(find /opt/openwrt -name "*.img.gz" | head -1)
OPENWRT_VMDK=$(find /opt/openwrt -name "*.vmdk" | head -1)

if [ -z "$OPENWRT_IMG" ] && [ -z "$OPENWRT_VMDK" ]; then
    echo -e "${RED}Không tìm thấy OpenWRT image files!${NC}"
    echo -e "${YELLOW}Các file có sẵn:${NC}"
    ls -la /opt/openwrt/
    exit 1
fi

# Tạo thư mục runtime
mkdir -p /tmp/openwrt-runtime
cd /tmp/openwrt-runtime

# Giải nén image nếu cần
if [ ! -z "$OPENWRT_IMG" ]; then
    echo -e "${BLUE}Tìm thấy OpenWRT image: $OPENWRT_IMG${NC}"
    if [[ "$OPENWRT_IMG" == *.gz ]]; then
        echo -e "${YELLOW}Giải nén image...${NC}"
        gunzip -c "$OPENWRT_IMG" > openwrt.img
        OPENWRT_IMG="openwrt.img"
    fi
fi

# Thiết lập networking
echo -e "${YELLOW}Thiết lập network...${NC}"

# Tạo tap interface (nếu có quyền)
if command -v ip >/dev/null 2>&1; then
    # Tạo bridge interface
    ip link add name br0 type bridge 2>/dev/null || true
    ip link set dev br0 up 2>/dev/null || true
fi

# Khởi động OpenWRT với QEMU
echo -e "${GREEN}Khởi động OpenWRT...${NC}"
echo -e "${BLUE}Truy cập LuCI web interface tại: http://localhost:8080${NC}"
echo -e "${BLUE}SSH tại: ssh root@localhost -p 2222${NC}"
echo -e "${YELLOW}Password mặc định: (để trống)${NC}"

# Tùy chọn khởi động
if [ ! -z "$OPENWRT_VMDK" ]; then
    echo -e "${YELLOW}Sử dụng VMDK image...${NC}"
    exec qemu-system-x86_64 \
        -m 512M \
        -smp 2 \
        -drive file="$OPENWRT_VMDK",format=vmdk,if=virtio \
        -netdev user,id=net0,hostfwd=tcp::2222-:22,hostfwd=tcp::8080-:80,hostfwd=tcp::8443-:443 \
        -device virtio-net,netdev=net0 \
        -nographic
elif [ ! -z "$OPENWRT_IMG" ]; then
    echo -e "${YELLOW}Sử dụng IMG image...${NC}"
    exec qemu-system-x86_64 \
        -m 512M \
        -smp 2 \
        -drive file="$OPENWRT_IMG",format=raw,if=virtio \
        -netdev user,id=net0,hostfwd=tcp::2222-:22,hostfwd=tcp::8080-:80,hostfwd=tcp::8443-:443 \
        -device virtio-net,netdev=net0 \
        -nographic
else
    echo -e "${RED}Không thể khởi động OpenWRT!${NC}"
    exit 1
fi
