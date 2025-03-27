import sys
import re

if len(sys.argv) < 2:
    print("Usage: python remove_amnhac.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Đọc nội dung file
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()

# Biểu thức chính quy để tìm kiếm chuỗi "[âm nhạc]"
pattern = r'\[âm nhạc\]'
# Thay thế bằng chuỗi rỗng
result = re.sub(pattern, '', data)

# Ghi đè lại file với nội dung đã xử lý
with open(filename, "w", encoding="utf-8") as f:
    f.write(result)

print("Đã xóa '[âm nhạc]' thành công!")
