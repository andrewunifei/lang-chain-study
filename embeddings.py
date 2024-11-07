from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

models = {
    '0': 'mxbai-embed-large',
    '1': 'llama3.2'
}

def model_available():
    return models

def get_embeddings_model(model_key):
    embeddings_model = OllamaEmbeddings(model=models[model_key])
    return embeddings_model

def get_vector_store(model_key='0'):
    embeddings_model = get_embeddings_model(model_key)
    vector_store = Chroma(
        collection_name='trading_reports',
        embedding_function=embeddings_model,
        persist_directory='./chroma.db'
    )
    return vector_store

def embed_text(text, model_key='0'):
    embeddings_model = get_embeddings_model(model_key)
    embeddings = embeddings_model.embed_documents(text)
    return embeddings

def store_embeddings(vectors,  model_key='0'):
    documents = [Document(page_content='daily_report_cards')]
    vector_store = get_vector_store(model_key)
    vector_store.add_documents(documents=documents, embeddings=vectors)

def query_document(query, model_key='0'):
    embeddings_model = get_embeddings_model(model_key)
    vector_store = get_vector_store(model_key)
    query_vector = embeddings_model.embed_documents([query])[0]
    result = vector_store.similarity_search(query_vector=query_vector, k=2)
    return result
