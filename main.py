import os
from dotenv import load_dotenv
from handle_files_paths import get_files_paths

load_dotenv()

august_2024_key = 'AUGUST_2024'
september_2024_key = 'SEPTEMBER_2024'
august_2024_files_path = os.getenv(august_2024_key)
september_2024_files_path = os.getenv(september_2024_key )
files_paths = get_files_paths([august_2024_files_path, september_2024_files_path])
print(len(files_paths))
