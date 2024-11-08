from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import chromadb

__models = {
    0: 'mxbai-embed-large',
    1: 'llama3.2',
    2: 'llama3.1',
    3: 'stablelm2'
}

def models_available():
    return __models

def get_embeddings_model(model_key):
    embeddings_model = OllamaEmbeddings(model=__models[model_key])
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

def store_embeddings(page_content, embeddings, model_key='0'):
    documents = [Document(page_content=page_content, metadate={"source": "personal_report"})]
    vector_store = get_vector_store(model_key)
    vector_store.add_documents(documents=documents, embeddings=embeddings)

def query_document(query, k=1, model_key='0'):
    embeddings_model = get_embeddings_model(model_key)
    query_vector = embeddings_model.embed_documents([query])[0]
    vector_store = get_vector_store(model_key)
    result = vector_store.similarity_search_by_vector(embedding=query_vector, k=k)
    return result

def count_documents():
    client = chromadb.PersistentClient(path="./chroma.db")
    collection_name = "trading_reports"
    collection = client.get_or_create_collection(collection_name)
    print(collection.count())
