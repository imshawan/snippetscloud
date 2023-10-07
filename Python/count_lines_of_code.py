import os, io

def count_lines_in_ts_files(directory_path):
    total_lines = 0
    total_files = 0
    for foldername, subfolders, filenames in os.walk(directory_path):
        if 'node_modules' in foldername:
            continue
        else:
            for filename in filenames:
                if filename.endswith(file_type):
                    total_files += 1
                    file_path = os.path.join(foldername, filename)
                    with io.open(file_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                        total_lines += len(lines)
    return total_lines, total_files

# Provide the path to the root directory of your project
project_directory = os.getcwd()
file_type = '.ts'


total_lines_of_code, total_files = count_lines_in_ts_files(project_directory)
print(f'Total lines of code in {file_type} files: {total_lines_of_code}')
print(f'Total files ending with {file_type}: {total_files}')
