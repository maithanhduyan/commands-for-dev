import sys

if len(sys.argv) < 2:
    print("Usage: python insert_prompt_openai.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Đoạn text cần chèn vào đầu file
header = """
Tôi có một đoạn văn bản tiếng Việt cần được chỉnh sửa và định dạng lại. Hãy:
- Đầu tiên hãy đọc toàn bộ nội dung để hiểu về chủ đề.
- Sửa lỗi chính tả, dấu câu.
- Đặt dấu câu hợp lý, xuống dòng đúng ngữ cảnh, tách đoạn rõ ràng, để tăng tính mạch lạc.
- Áp dụng in đậm cho tiêu đề chính, in nghiêng cho ví dụ hoặc trích dẫn.
- Đảm bảo cấu trúc phân cấp rõ ràng (tiêu đề chương → mục con → nội dung chi tiết).
- Giữ nguyên thông điệp và ý nghĩa gốc, không thêm/bớt nội dung.
- Trả lời bằng cách viết lại toàn bộ đoạn văn đã định dạng theo yêu cầu.
Đoạn văn cần chỉnh sửa sau:
"""

footer ="""
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
