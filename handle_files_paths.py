import os

def generate_paths(directory_path):
    files_paths = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            full_path = os.path.join(root, file)
            files_paths.append(full_path)

    return files_paths

def get_files_paths(directories_names):
    all_files_paths = []

    for path in directories_names:
        all_files_paths.extend(generate_paths(path))

    return all_files_paths
