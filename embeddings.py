from langchain_ollama.llms import OllamaLLM

models = {
    '0': 'mxbai-embed-large',
    '1': 'llama3.2'
}

def model_available():
    return models

def embed(model_key):
    model = OllamaLLM(model=models[model_key], temperature=0)
    names = model.invoke('I have a dog pet and I want a cool name for it.\
        Suggest me five cool names for my pet. They are black in color.\
         Just list the names, no additional information')

    return names

