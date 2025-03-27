import re
import sys

def replace_think_tags(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Biểu thức chính quy tìm thẻ <think>...</think> với nội dung bất kỳ (bao gồm cả newline)
    new_content = re.sub(
        r'<think>(.*?)</think>',
        r'<details>\n <summary>Thinking</summary>\n\1\n</details>',
        content,
        flags=re.DOTALL
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Đã thay thế nội dung trong {filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python replace_think.py <filename>")
        sys.exit(1)
    replace_think_tags(sys.argv[1])
