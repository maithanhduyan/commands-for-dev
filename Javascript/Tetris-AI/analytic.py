import os
import pathlib
import sys
from collections import deque

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

current_directory = current_dir = os.getcwd()  # Lấy đường dẫn thư mục hiện tại

# Danh sách các thư mục và file cần bỏ qua
exclude_dirs = ['.git', 'node_modules']
exclude_files = ['.gitignore', '.exe','.md']

def generate_header( markdown_file):
    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write(f"# You are an intelligent programming assistant.\n")
        f.write(f"# This is AI project\n\n")

def generate_tree(root_dir, markdown_file, exclude_dirs=None, exclude_files=None):
    if exclude_dirs is None:
        exclude_dirs = []
    if exclude_files is None:
        exclude_files = []

    with open(markdown_file, 'a', encoding='utf-8') as f:
        f.write(f"# Directory tree of {root_dir}\n\n")
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Bỏ qua các thư mục trong danh sách exclude_dirs
            dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
            
            depth = dirpath.replace(root_dir, '').count(os.sep)
            indent = '│   ' * depth  # Sử dụng 4 dấu cách cho mỗi cấp độ

            # Ghi tên thư mục
            if depth == 0:
                f.write(f"├── {os.path.basename(dirpath)}/\n")
            else:
                f.write(f"{indent}├── {os.path.basename(dirpath)}/\n")
            
            # Ghi tên file trong thư mục hiện tại
            subindent = '│   ' * (depth + 1)  # Tăng thêm cấp độ thụt đầu dòng cho file
            for i, filename in enumerate(filenames):
                # Bỏ qua các file trong danh sách exclude_files
                if any(filename.endswith(ext) for ext in exclude_files):
                    continue
                
                if i == len(filenames) - 1:
                    f.write(f"{subindent}└── {filename}\n")
                else:
                    f.write(f"{subindent}├── {filename}\n")
                
def generate_content(root_dir, output_markdown):
    """
    Quét các file trong thư mục root_dir, đọc nội dung và ghi vào file .markdown, 
    ngoại trừ các file có đuôi .jpg, .css, .min.js, .min.css, và .ttf,
    và không quét các thư mục node_modules và .git.
    """
    # Các đuôi file cần bỏ qua
    excluded_extensions = ['.jpg', '.css', '.min.js', '.min.css', '.ttf']
    # Các thư mục cần bỏ qua
    excluded_dirs = ['node_modules', '.git']

    with open(output_markdown, 'a', encoding='utf-8') as markdown_file:
        markdown_file.write(f"# Content of .js and .ejs files in {root_dir}\n\n")
        for dirpath, dirnames, filenames in os.walk(root_dir):
            
            # Bỏ qua các thư mục trong danh sách excluded_dirs
            dirnames[:] = [d for d in dirnames if d not in excluded_dirs]
            for filename in filenames:
                # Bỏ qua các file có đuôi trong danh sách excluded_extensions
                if any(filename.endswith(ext) for ext in excluded_extensions):
                    continue
                
                if filename.endswith('.js') or filename.endswith('.ejs'):
                    file_path = os.path.join(dirpath, filename)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    # Ghi nội dung file vào file Markdown
                    markdown_file.write(f"## {file_path}\n")
                    markdown_file.write("```\n")
                    markdown_file.write(content)
                    markdown_file.write("\n```\n\n")
                    
                    # In ra màn hình đường dẫn của file đã xử lý
                    print(f"Processed file: {file_path}")


def main():
    markdown_file = 'project_structure.md'
    generate_header(markdown_file)
    # root_dir = pathlib.Path(current_directory)
    # if not root_dir.is_dir():
    #     print("The specified root directory doesn't exist")
    #     sys.exit()
    # tree = DirectoryTree(
    #     root_dir, dir_only=0, output_file=markdown_file
    # )
    # tree.generate()

    # Generate structure first and write it to the file
    generate_tree(current_directory, markdown_file, exclude_dirs, exclude_files)
    
    # Ghi nội dung file
    generate_content(current_directory, markdown_file)


if __name__ == "__main__":
    main()
