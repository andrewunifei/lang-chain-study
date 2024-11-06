from langchain_ollama.llms import OllamaLLM

def generate_names():
    model = OllamaLLM(model='llama3.2', temperature=0)
    names = model.invoke('I have a dog pet and I want a cool name for it.\
        Suggest me five cool names for my pet.')

    return names

if __name__ == '__main__':
    print(generate_names())