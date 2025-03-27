import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: python insert_post_category.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Lấy ngày hiện tại theo định dạng yyyy-mm-dd
current_date = datetime.now().strftime("%Y-%m-%d")
# Đoạn text cần chèn vào đầu file
header = f"""---
date: {current_date}
category:
  - news
tag:
  - news
archive: true
---"""

# Đọc nội dung file hiện có
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

# Tạo nội dung mới: header + một dòng trống + nội dung cũ
new_content = header + "\n" + content + "\n"

# Ghi đè file với nội dung mới
with open(filename, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Đã chèn header vào đầu file!")
