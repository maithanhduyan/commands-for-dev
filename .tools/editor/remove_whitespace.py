import sys

if len(sys.argv) < 2:
    print("Usage: python remove_whitespace.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Đọc nội dung file
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Xử lý: loại bỏ khoảng trắng đầu và cuối mỗi dòng,
# và loại bỏ các dòng trống (sau khi đã strip)
processed_lines = [line.strip() for line in lines if line.strip() != ""]

# Ghép các đoạn đã xử lý bằng newline
result = "\n".join(processed_lines)

# Ghi đè lại file với nội dung đã xử lý
with open(filename, "w", encoding="utf-8") as f:
    f.write(result)

print("Đã xử lý khoảng trắng và xuống dòng thành công!")
