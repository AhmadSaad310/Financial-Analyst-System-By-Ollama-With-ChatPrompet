from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

templat = """Question: {question} """

while True:
    if question.lower == 'exit':
        break
    else:

        prompet = ChatPromptTemplate.from_template(templat)

        llm = OllamaLLM(model="llama3.2",stream=True)

        for x in llm.stream(prompet.format_messages(question=input('Enter your question : ')))

        print(x,end='')
