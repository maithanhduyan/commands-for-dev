import sys

if len(sys.argv) < 2:
    print("Usage: python insert_prompt_openai.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Đoạn text cần chèn vào đầu file
header = """Đầu tiên đọc hiểu đoạn văn tiếng Việt. Yêu cầu:
- Kiểm tra lại toàn bộ đoạn văn cho đúng chính tả.
- Đặt dấu câu, xuống dòng, in đậm, in nghiêng... sao cho hợp lý.
- Trả lời tôi bằng cách viết lại toàn bộ đoạn văn.
Đoạn văn cần chỉnh sửa sau:
"""

footer ="""
Vui lòng chỉnh sửa toàn bộ đoạn văn theo các yêu cầu nêu trên và trả lời bằng văn bản đã được định dạng đúng.
---
Ghi chú: Hãy đảm bảo giữ nguyên nội dung gốc nhưng cải thiện cấu trúc, chính tả và định dạng sao cho dễ đọc và rõ ràng.
"""
# Đọc nội dung file hiện có
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

# Tạo nội dung mới: header + một dòng trống + nội dung cũ
new_content = header + "```\n" + content + "\n ```" + footer

# Ghi đè file với nội dung mới
with open(filename, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Đã chèn user prompt vào file!")
