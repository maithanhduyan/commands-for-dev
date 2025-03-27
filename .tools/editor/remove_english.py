import sys

if len(sys.argv) < 2:
    print("Usage: python remove_text.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Đọc nội dung file
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()

# Xóa chuỗi "English (auto-generated)"
result = data.replace("English (auto-generated)", "")

# Ghi đè lại file với nội dung đã xử lý
with open(filename, "w", encoding="utf-8") as f:
    f.write(result)

print("Đã xóa 'English (auto-generated)' thành công!")
