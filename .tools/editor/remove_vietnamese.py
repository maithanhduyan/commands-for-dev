import sys
import re

if len(sys.argv) < 2:
    print("Usage: python remove_vietnamese.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Đọc nội dung file
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()

# Biểu thức chính quy để tìm kiếm chuỗi "Vietnamese (auto-generated)"
# Lưu ý: các dấu ngoặc được escape bằng "\"
pattern = r'Vietnamese \(auto-generated\)'
# Thay thế bằng chuỗi rỗng
result = re.sub(pattern, '', data)

# Ghi đè lại file với nội dung đã xử lý
with open(filename, "w", encoding="utf-8") as f:
    f.write(result)

print("Đã xóa 'Vietnamese (auto-generated)' thành công!")
