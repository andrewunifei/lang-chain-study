from langchain_ollama import OllamaEmbeddings

models = {
    '0': 'mxbai-embed-large',
    '1': 'llama3.2'
}

def model_available():
    return models

def embed_text(text, model_key='0'):
    embeddings_model = OllamaEmbeddings(model=models[model_key])
    embeddings = embeddings_model.embed_documents(text)
    return embeddings
