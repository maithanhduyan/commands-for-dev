import sys

if len(sys.argv) < 2:
    print("Usage: python insert_header.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Đoạn text cần chèn vào đầu file
header = """Đầu tiên đọc hiểu đoạn văn tiếng Việt. Yêu cầu:
- Kiểm tra lại toàn bộ đoạn văn cho đúng chính tả.
- Đặt dấu câu, xuống dòng, in đậm, in nghiêng... sao cho hợp lý.
- Trả lời tôi bằng cách viết lại toàn bộ đoạn văn.
Đoạn văn cần chỉnh sửa sau:
"""

# Đọc nội dung file hiện có
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

# Tạo nội dung mới: header + một dòng trống + nội dung cũ
new_content = header + "```\n" + content + "\n ```"

# Ghi đè file với nội dung mới
with open(filename, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Đã chèn header vào đầu file!")
