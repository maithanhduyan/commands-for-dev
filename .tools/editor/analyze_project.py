import os
import ast
import argparse

WARNING_LINE_LIMIT = 50  # Cảnh báo nếu hàm > 50 dòng

def analyze_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read(), filename=filepath)
        except SyntaxError:
            print(f"⚠️  Không thể phân tích file: {filepath}")
            return

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            start_line = node.lineno
            end_line = max(getattr(n, "lineno", start_line) for n in ast.walk(node))
            length = end_line - start_line + 1

            if length > WARNING_LINE_LIMIT:
                print(f"🚨 [DÀI] Hàm '{node.name}' trong {filepath}:{start_line} dài {length} dòng.")

            # Tìm vòng lặp chứa I/O
            for subnode in ast.walk(node):
                if isinstance(subnode, (ast.For, ast.While)):
                    for body_node in subnode.body:
                        if isinstance(body_node, ast.Expr) and isinstance(body_node.value, ast.Call):
                            func = getattr(body_node.value.func, 'attr', '') or getattr(body_node.value.func, 'id', '')
                            if func in ['get', 'post', 'open']:
                                print(f"⚠️  [I/O trong vòng lặp] Hàm '{node.name}' gọi '{func}()' trong vòng lặp tại {filepath}:{subnode.lineno}")

def analyze_project(root_folder):
    for dirpath, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(dirpath, file)
                analyze_file(filepath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phân tích project Python để tìm vấn đề hiệu suất/mở rộng.")
    parser.add_argument("path", help="Đường dẫn tới thư mục chứa mã nguồn Python")
    args = parser.parse_args()

    print(f"🔍 Phân tích project: {args.path}\n")
    analyze_project(args.path)
    print("\n✅ Phân tích hoàn tất.")