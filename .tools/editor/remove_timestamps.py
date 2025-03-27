import sys
import re

if len(sys.argv) < 2:
    print("Usage: python remove_timestamps.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Đọc nội dung file
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()

# Biểu thức chính quy tìm timestamp dạng HH:MM hoặc HH:MM:SS
pattern = r'\b\d{1,2}:\d{2}(?::\d{2})?\b'
result = re.sub(pattern, '', data)

# Ghi đè lại file với nội dung đã xử lý
with open(filename, "w", encoding="utf-8") as f:
    f.write(result)

print("Xóa timestamp thành công!")
