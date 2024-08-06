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
# 

# tạo SSL cho server
# tao thư mục chứa cert
mkdir -p /home/coder/ssl

# tạo file fullchain.pem
cat <<EOF > /home/coder/ssl/fullchain.pem
-----BEGIN CERTIFICATE-----
MIIDazCCAlOgAwIBAgIUB3EtGYvUIh+8nxKNi2tvr1CXY10wDQYJKoZIhvcNAQEL
BQAwRTELMAkGA1UEBhMCQVUxEzARBgNVBAgMClNvbWUtU3RhdGUxITAfBgNVBAoM
GEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDAeFw0yMTEwMjAxNjU0MjFaFw0yMjEw
MjAxNjU0MjFaMEUxCzAJBgNVBAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEw
HwYDVQQKDBhJbnRlcm5ldCBXaWRnaXRzIFB0eSBMdGQwggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQDWtDFSWnmF2ElhmYHB+Qqjt6X/KosYwwoNupEDZjdD
sYsZkdljyqUiGxD6Bbe7o5ChZRRrX6h8rlE8bWmtDVnMu/Pd/BpACkTSYCMTPoLT
PXN5W8vAEguTrtMzA1GkA3JHfvJbU7C3iZDV327Ev9Z2oI4vJaiGIHG1ChoL0X7v
OKkO/RbvzUAvNdOJmKAvUqGvYfeYyaH086PK0jxSqJmJ02w0QPiLy9y8jzgl3eV0
c6f8HDvdkugifYPaEbZc5IkXKytDdpfIvAxZcy2CqhwPQl/bwsjrxGd5kIY3t6H1
0AaVAdYgcq1gwFT3rztZYN+sdKrsjgejGyYx6wmO2PtxAgMBAAGjUzBRMB0GA1Ud
DgQWBBQ1H3DN0LT2b9wqVTAFdTT9R6Fc1jAfBgNVHSMEGDAWgBQ1H3DN0LT2b9wq
VTAFdTT9R6Fc1jAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQAo
nRm+pHdLf1Gh+8Jv7IlzgJ40M1NkrqRMwRM+jlXa8GEJuSjIu3cop9aVC9WFG5dJ
yEe+GzRghBPW4jmnSgcXdcsDc783ijtOt/Q6ZJv6DBIOtZAl9AYXhvF4xfje7r+W
0/QJT8pHWIBXwldEhLDbXpRsfqRR8zlkw5dTgVbSQGzus3c81YaSR5ER5gxEA3Vs
JCBIQXyz69RCx5N7Gjx9SSdR2ImQ5UrLFAEp7872RkkJjfaIB58AnEv3dmp+C90W
rntVwR3+XugkU8mPgejcJqCyytPou+I58ObNdH9n+wtoDBtaRhGWmz2gMgEttb4p
NNp/no1ze/UrcEPU7mOE
-----END CERTIFICATE-----

EOF

# tạo file privkey.pem

cat <<EOF > /home/coder/ssl/privkey.pem
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDWtDFSWnmF2Elh
mYHB+Qqjt6X/KosYwwoNupEDZjdDsYsZkdljyqUiGxD6Bbe7o5ChZRRrX6h8rlE8
bWmtDVnMu/Pd/BpACkTSYCMTPoLTPXN5W8vAEguTrtMzA1GkA3JHfvJbU7C3iZDV
327Ev9Z2oI4vJaiGIHG1ChoL0X7vOKkO/RbvzUAvNdOJmKAvUqGvYfeYyaH086PK
0jxSqJmJ02w0QPiLy9y8jzgl3eV0c6f8HDvdkugifYPaEbZc5IkXKytDdpfIvAxZ
cy2CqhwPQl/bwsjrxGd5kIY3t6H10AaVAdYgcq1gwFT3rztZYN+sdKrsjgejGyYx
6wmO2PtxAgMBAAECggEAagRWKm0kfpPbQEdVjFuWBluDqyjtwE9monrSalRJy7Ja
lkiviJgizGGDE4JJRG0y2I8Z8x8sCkzlLip0uQ/TnMXeWGnI6IBplVwFVdZTMU2x
vGY4iOIgN09nWFQ2Nv/AqU8lCzWbGDXkf8cxYhO8KZ2EOAGnYnuYyiVv0RAkVqjC
zE/ff+v6e17YWV9rz8Nges2GCGWMUKiCvkhxiUOCaoEFx8jihmfxDAD5aAJL3KJD
8oDZ0WDW5aqcSgnFzptFsaoc5QMoO6tKBUqvJwf4DOo9K8OCvd/F3foVXtWqYx/h
lJoYrF9mvuvP4dsEWgcpB3xype3da/jrrGkjWtr7RQKBgQD5qs2spl26DWWW+jT4
i+U6NCEZYeiqNUjPQwckC3lQC7SawvSqJJSOqtLk4SRlxa8/a0qsURcBhTq6bEz8
Htg7uAFV1IWW7YAUn5zptorD5U0KaeKs6G2S15ZHTUyya8D1+97XB3JlWPHxVVl1
f0ur/1HEmIFUHHA6cG4wpOGIhwKBgQDcJlt6xkWBuRidQm1mQSiQGg3MJ51FERod
lHsQKfhNTDEvRglrGeJ7dCc4VyKiPMe15zCZGGFp14L9qpHvCy5nM2sf64kR4735
uwy2B+s8T6CHn2uQbLji7/ZPtfwkz96Axt0KGxCx/A/ublSdwoM7bHpaIYL66fwI
X9KuToByRwKBgFP0gdEq6J2l36GTZbimomCeIvs8F1cVL/SyX3ZZfWPTa9oW8Ns+
Dc6j1uMsambmwPWciLHFWu0h9gu2W3T0klYSnDBWlM2Z89X7jnJw9dzGANAdpyHp
zt7wLBKyBbaB0ZNmLRs139wAuusifkCqm7Gs27w2ZFb6cSrVn9gvub+FAoGAe2+e
V0aYblXkMTivsmfSYInbNp73lWQzamZ4YeXGbUDNSx5P5ZdL38COxQ5GQwUlTR7l
ptF+vSOzNJvQ22E/kWnJJMqhvkAdosp4JBBomxZigeinHQF44PV++86kI9fRgA8A
nMv0HnegTyXZl+MaRdVa/PJRSHKtd9ySel1Vs70CgYEA9vI9niCu6pHrzxI6FoVS
HF8u+JY3SIeYuh40KH7RzW7C3jqCulH3NdOqhk6M5ka9h/fff8JnBjIH2YORq4t+
koRGSPJsB6vKZm7R5/jwpiFt80LjTrmSserxw9ZYRfnklLl5MubmUopS8fMpBsi3
h3y5mGYu56ukyTfxMtV5h+Q=
-----END PRIVATE KEY-----

EOF

echo "Tạo 2 file: /home/coder/ssl/fullchain.pem và /home/coder/ssl/privkey.pem hoàn tất." 

## Tạo service cho code-server - Create code-server as a service.
# nano /root/.config/code-server/config.yaml
# sudo nano /lib/systemd/system/code-server.service
# systemctl daemon-reload
# sudo systemctl start code-server
# 
cat <<EOF > /lib/systemd/system/code-server.service
[Unit]
Description=code-server
After=nginx.service

[Service]
Type=simple
Environment=PASSWORD=dc7119311305b3f10166bd5c
ExecStart=code-server --bind-addr 0.0.0.0:8443 --cert /home/coder/ssl/fullchain.pem --cert-key /home/coder/ssl/privkey.pem
Restart=always

[Install]
WantedBy=multi-user.target

EOF

systemctl daemon-reload
systemctl start code-server

# chạy code-server dưới https port: 8443
# certbot 
# code-server --bind-addr 0.0.0.0:8443 --cert /etc/letsencrypt/live/example.com/fullchain.pem --cert-key /etc/letsencrypt/live/example.com/privkey.pem

# WARNING : Không an toàn
# chạy code-server dưới https với 2 file vừa tạo 
# code-server --bind-addr 0.0.0.0:8443 --cert /home/coder/ssl/fullchain.pem --cert-key /home/coder/ssl/privkey.pem

ufw allow 8443


