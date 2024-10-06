# Sử dụng Golang image chính thức để build ứng dụng
FROM golang:1.22 AS builder

# Đặt thư mục làm việc
WORKDIR /app

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Biên dịch ứng dụng với CGO tắt đi để tạo file nhị phân static
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o helloworld

# Tạo một image chỉ để chạy ứng dụng
FROM debian:latest

# Đặt thư mục làm việc
WORKDIR /app/

VOLUME [ "/app/" ]

# Sao chép binary từ giai đoạn build
COPY --from=builder /app/helloworld .

# Mở cổng 8080 nếu cần
EXPOSE 8080

# Lệnh chạy ứng dụng
CMD ["./helloworld"]
