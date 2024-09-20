import os
import sys
import io

# Set stdout to handle UTF-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def generate_tree(dir_path, prefix=''):
    files = os.listdir(dir_path)
    files.sort()
    pointers = ['├── '] * (len(files) - 1) + ['└── ']

    for pointer, file in zip(pointers, files):
        file_path = os.path.join(dir_path, file)
        print(prefix + pointer + file)

        if os.path.isdir(file_path):
            extension = '│   ' if pointer == '├── ' else '    '
            generate_tree(file_path, prefix + extension)

# Folder Path
root_dir = r'E:\\messenger\\venv'
print(os.path.basename(root_dir) + '/')
generate_tree(root_dir)
