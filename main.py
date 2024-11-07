import os
from dotenv import load_dotenv
from handle_files_paths import get_files_paths
from extract_text import extract_text_from_pdf
from embeddings import embed_text, store_embeddings, query_document

load_dotenv()

august_2024_key = 'AUGUST_2024'
september_2024_key = 'SEPTEMBER_2024'
august_2024_files_path = os.getenv(august_2024_key)
september_2024_files_path = os.getenv(september_2024_key )
files_paths = get_files_paths([august_2024_files_path, september_2024_files_path])
for path in files_paths:
    text = extract_text_from_pdf(path)
    embeddings = embed_text(text[0].strip(),2)
    store_embeddings(text[0], embeddings, 2)
print('Done.')

