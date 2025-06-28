# OpenWrt Docker Container

A containerized OpenWrt instance running in QEMU for virtualized network testing and development.

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- At least 2GB RAM available
- Windows/Linux/macOS with Docker support

### Running OpenWrt (Lightweight Version)

```bash
# Clone or download the project files
cd openwrt

# Start the lightweight OpenWrt container
docker-compose -f docker-compose.lightweight.yml up -d

# Check container status
docker ps

# View logs
docker logs openwrt-lightweight-lab
```

## 📋 What's Included

### Container Components
- **Base Image**: Ubuntu 22.04 LTS
- **Virtualization**: QEMU (software emulation)
- **OpenWrt Version**: 23.05.5 x86_64
- **Network**: Virtio network with port forwarding
- **Storage**: Persistent volumes for configuration

### Network Configuration
- **SSH Access**: `localhost:2222` (root login, no password initially)
- **Web Interface**: `http://localhost:8080` (LuCI)
- **HTTPS Web**: `https://localhost:8443` (LuCI SSL)

## 🌐 Access Methods

### Web Interface (LuCI)
1. Open browser to `http://localhost:8080`
2. Default login: `root` (no password)
3. Configure OpenWrt through the web interface

### SSH Access
```bash
# SSH to OpenWrt
ssh root@localhost -p 2222

# Or using PuTTY on Windows
# Host: localhost
# Port: 2222
# Username: root
# Password: (leave empty initially)
```

### Serial Console (Advanced)
```bash
# Attach to container for serial console access
docker exec -it openwrt-lightweight-lab /bin/bash

# The QEMU console is accessible within the container
```

## 🔧 Configuration Files

### File Structure
```
openwrt/
├── docker-compose.yml              # Main Docker Compose
├── docker-compose.lightweight.yml  # Lightweight version
├── Dockerfile                      # Main Dockerfile
├── Dockerfile.lightweight          # Lightweight Dockerfile
├── start-openwrt.sh               # OpenWrt startup script
└── README.md                      # This documentation
```

### Container Configuration
- **RAM**: 512MB allocated to OpenWrt VM
- **CPU**: 2 virtual cores
- **Storage**: Persistent volume for OpenWrt data
- **Networking**: Bridge mode with port forwarding

## 🛠️ Management Commands

### Container Management
```bash
# Start the container
docker-compose -f docker-compose.lightweight.yml up -d

# Stop the container
docker-compose -f docker-compose.lightweight.yml down

# Restart the container
docker-compose -f docker-compose.lightweight.yml restart

# View real-time logs
docker logs -f openwrt-lightweight-lab

# Check container resource usage
docker stats openwrt-lightweight-lab
```

### OpenWrt Commands (via SSH)
```bash
# Connect to OpenWrt
ssh root@localhost -p 2222

# Check network status
ip addr show

# Check OpenWrt services
service

# Update package lists
opkg update

# Install packages
opkg install <package-name>

# Reboot OpenWrt
reboot
```

## 🔄 Boot Process

The container follows this startup sequence:

1. **Container Start**: Docker container initializes
2. **QEMU Launch**: Starts with OpenWrt image
3. **OpenWrt Boot**: Linux kernel loads (30-60 seconds)
4. **Network Init**: Bridge and interface setup
5. **Services Start**: SSH, web interface, and other services
6. **Ready**: All services accessible

## 🧪 Testing Connectivity

### Port Testing
```bash
# Test web interface
curl -I http://localhost:8080

# Test SSH port
telnet localhost 2222

# PowerShell testing
Test-NetConnection -ComputerName localhost -Port 8080
Test-NetConnection -ComputerName localhost -Port 2222
```

### Service Verification
1. **Web Interface**: Browse to `http://localhost:8080`
2. **SSH Access**: `ssh root@localhost -p 2222`
3. **Container Logs**: Check for "link becomes ready" message

## 🚨 Troubleshooting

### Common Issues

#### Container Won't Start
```bash
# Check Docker daemon status
docker version

# View container logs
docker logs openwrt-lightweight-lab

# Check for port conflicts
netstat -an | findstr :8080
netstat -an | findstr :2222
```

#### OpenWrt Boot Issues
```bash
# View boot logs
docker logs openwrt-lightweight-lab | grep -E "(error|failed|panic)"

# Check QEMU process
docker exec openwrt-lightweight-lab ps aux | grep qemu
```

#### Network Connectivity Problems
```bash
# Check port mappings
docker port openwrt-lightweight-lab

# Test network connectivity
Test-NetConnection -ComputerName localhost -Port 8080

# Check OpenWrt network status (via SSH)
ssh root@localhost -p 2222 "ip addr show"
```

### Recovery Steps

#### Reset OpenWrt Configuration
```bash
# Stop container
docker-compose -f docker-compose.lightweight.yml down

# Remove persistent volume (WARNING: Deletes all configuration)
docker volume rm openwrt_openwrt_light_data

# Restart container
docker-compose -f docker-compose.lightweight.yml up -d
```

#### Access Failsafe Mode
1. Watch container logs during boot
2. When prompted, press 'f' key within 5 seconds
3. This boots OpenWrt in failsafe mode for recovery

## 📊 Performance Notes

### Resource Usage
- **RAM**: ~512MB for OpenWrt VM + ~100MB container overhead
- **CPU**: Low usage during idle, spikes during boot
- **Disk**: ~150MB for OpenWrt image + config data
- **Network**: Minimal overhead with port forwarding

### Optimization Tips
1. Use lightweight version for basic testing
2. Allocate sufficient RAM to host system
3. Consider SSD storage for better I/O performance
4. Monitor container resource usage with `docker stats`

## 🔐 Security Considerations

### Default Security
- **Root Access**: No password required initially
- **SSH**: Enabled by default on port 2222
- **Web Interface**: HTTP (not HTTPS) by default
- **Firewall**: OpenWrt firewall enabled

### Hardening Steps
1. Set root password: `passwd` (via SSH)
2. Configure SSH key authentication
3. Enable HTTPS for web interface
4. Configure OpenWrt firewall rules
5. Change default ports if needed

## 🔄 Updates and Maintenance

### Container Updates
```bash
# Rebuild container with latest OpenWrt
docker-compose -f docker-compose.lightweight.yml build --no-cache

# Pull latest base images
docker pull ubuntu:22.04
```

### OpenWrt Updates
```bash
# Connect to OpenWrt
ssh root@localhost -p 2222

# Update package database
opkg update

# Upgrade packages
opkg list-upgradable
opkg upgrade <package-name>
```

## 💡 Use Cases

### Development & Testing
- Network configuration testing
- Router firmware development
- Network automation testing
- VPN and firewall rule testing

### Learning & Education
- OpenWrt feature exploration
- Linux networking concepts
- Containerized network appliances
- DevOps network automation

### Production Scenarios
- Network appliance prototyping
- Isolated network testing
- Configuration management testing
- Network troubleshooting environment

## 📞 Support

### Getting Help
1. Check container logs: `docker logs openwrt-lightweight-lab`
2. Verify network connectivity with test commands
3. Access OpenWrt documentation: https://openwrt.org/docs/start
4. Check Docker documentation for container issues

### Known Limitations
- Software emulation only (no KVM in containers)
- Limited to x86_64 architecture
- Network performance limited by Docker networking
- No hardware acceleration support

---

**Status**: ✅ Working and Tested
**Last Updated**: 2025-06-06
**OpenWrt Version**: 23.05.5
**Container**: Lightweight Ubuntu-based QEMU setup

## Tính Năng

- ✅ Build từ source code OpenWRT mới nhất
- ✅ Multi-stage build để tối ưu kích thước
- ✅ Chạy OpenWRT trong QEMU với KVM acceleration
- ✅ LuCI web interface
- ✅ SSH access
- ✅ Tùy chỉnh cấu hình build
- ✅ Hỗ trợ VPN, QoS, và các tính năng nâng cao

## Yêu Cầu Hệ Thống

- Docker và Docker Compose
- Ít nhất 8GB RAM (để build)
- 20GB dung lượng trống
- CPU hỗ trợ virtualization (cho KVM)

## Cách Sử Dụng

### Tùy Chọn 1: Build Từ Source (Recommended cho Custom)

```bash
# Build image từ source (có thể mất 1-2 giờ)
docker-compose build

# Khởi động container
docker-compose up -d

# Xem logs
docker-compose logs -f openwrt
```

### Tùy Chọn 2: Sử Dụng Pre-built Image (Nhanh hơn)

```bash
# Build và chạy phiên bản lightweight
docker-compose -f docker-compose.lightweight.yml build
docker-compose -f docker-compose.lightweight.yml up -d

# Xem logs
docker-compose -f docker-compose.lightweight.yml logs -f openwrt-light
```

### Xử Lý Lỗi Network Khi Build

Nếu gặp lỗi network timeout khi clone repository:

```bash
# Thử build lại với no-cache
docker-compose build --no-cache

# Hoặc sử dụng phiên bản lightweight
docker-compose -f docker-compose.lightweight.yml up -d
```

### 2. Truy Cập OpenWRT

- **LuCI Web Interface**: http://localhost:8080
- **SSH**: `ssh root@localhost -p 2222`
- **Password mặc định**: (để trống, nhấn Enter)

### 3. Tùy Chỉnh Build

Để tùy chỉnh build OpenWRT:

1. Copy file cấu hình mẫu:
```bash
cp .config.template .config
```

2. Chỉnh sửa file `.config` theo nhu cầu

3. Uncomment dòng trong Dockerfile:
```dockerfile
COPY --chown=openwrt:openwrt .config .config
```

4. Rebuild:
```bash
docker-compose build --no-cache
```

## Cấu Hình Có Sẵn

Build mặc định bao gồm:

- **Target**: x86_64 (generic)
- **LuCI**: Web interface với SSL
- **Networking**: WiFi, VPN (OpenVPN + WireGuard)
- **QoS**: Traffic shaping và monitoring  
- **File Sharing**: Samba4
- **System Tools**: htop, nano, vim, python3
- **Development**: git, python3-pip

## Troubleshooting

### Build Lỗi
```bash
# Xem logs chi tiết
docker-compose build --no-cache --progress=plain

# Build lại từ đầu
docker-compose down -v
docker-compose build --no-cache
```

### Không Truy Cập Được Web Interface
```bash
# Kiểm tra container đang chạy
docker-compose ps

# Kiểm tra logs
docker-compose logs openwrt

# Restart container
docker-compose restart openwrt
```

### Performance Issues
- Đảm bảo KVM được enable trên host
- Tăng RAM cho container (sửa trong start-openwrt.sh)
- Sử dụng SSD cho tốc độ I/O

## Customization

### Thêm Packages
Chỉnh sửa file `.config` và thêm:
```
CONFIG_PACKAGE_ten_package=y
```

### Thay Đổi Target Platform
```
CONFIG_TARGET_platform=y
CONFIG_TARGET_platform_subtarget=y
```

### Build cho Router Cụ Thể
```
CONFIG_TARGET_DEVICE_platform_subtarget_DEVICE_device=y
```

## Ghi Chú

- Build lần đầu sẽ mất thời gian (1-2 giờ)
- Image cuối cùng sẽ nhỏ hơn nhờ multi-stage build
- Để cập nhật source code, rebuild image với `--no-cache`
- Dữ liệu được lưu trong Docker volume `openwrt_data`

## Liên Kết Hữu Ích

- [OpenWRT Official Documentation](https://openwrt.org/docs/start)
- [OpenWRT Build System](https://openwrt.org/docs/guide-developer/toolchain/use-buildsystem)
- [LuCI Documentation](https://openwrt.org/docs/guide-user/luci/luci.essentials)
