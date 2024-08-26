#!/bin/bash

# Script này sẽ kiểm tra xem MySQL có sẵn không trước khi khởi động ứng dụng

set -e

host="$DB_HOST"
port="$DB_PORT"

# Kiểm tra nếu MySQL sẵn sàng
until nc -z -v -w30 $host $port
do
  echo "Waiting for MySQL at $host:$port..."
  sleep 5
done

echo "MySQL is up and running!"

# Chạy lệnh tiếp theo (khởi động ứng dụng)
exec "$@"
