import os

def collect_files(root_dir, extensions, filenames, exclude_dirs=None, exclude_files=None):
    if exclude_dirs is None:
        exclude_dirs = []
    if exclude_files is None:
        exclude_files = []
    matches = []
    for root, dirs, files_in_dir in os.walk(root_dir):
        # Loại trừ các thư mục không mong muốn
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for filename in files_in_dir:
            # Bỏ qua các tệp không mong muốn
            if filename in exclude_files:
                continue
            if filename.endswith(tuple(extensions)) or filename in filenames:
                filepath = os.path.join(root, filename)
                matches.append(filepath)
    return matches

def write_markdown(files, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for filepath in files:
            f.write(f'# {filepath}\n\n')
            f.write('```\n')
            with open(filepath, 'r', encoding='utf-8') as file_content:
                f.write(file_content.read())
            f.write('\n```\n\n')

if __name__ == '__main__':
    root_dir = '../'
    output_file = 'project_files.md'
    extensions = ['.html', '.js', '.css', 'java', '.properties']  # Danh sách các phần mở rộng tệp
    filenames = ['pom.xml', 'Dockerfile']  # Danh sách các tên tệp cụ thể
    exclude_dirs = ['node_modules','target']  # Thư mục cần bỏ qua
    exclude_files = ['package-lock.json','launch.json', 'maven-wrapper.properties']  # Tệp cần bỏ qua
    files = collect_files(root_dir, extensions, filenames, exclude_dirs, exclude_files)
    write_markdown(files, output_file)
