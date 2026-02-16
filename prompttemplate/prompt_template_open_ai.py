from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-5.2")

template = """Explique de forma resumida o que é o {tema}."""

prompt = PromptTemplate(
    input_variables=["tema"],
    template=template,
)

# O operador | é usado para encadear o prompt com o modelo de linguagem, 
# criando um pipeline de processamento.
# Preciso entender melhor o que o pipe faz.
chain = prompt | llm

# O método invoke é usado para executar o pipeline, 
# passando os valores necessários para as variáveis de entrada do prompt.
# Doc para entender formato:
# - https://docs.langchain.com/oss/python/langchain/models#invoke
# - https://docs.langchain.com/oss/python/langchain/messages
result = chain.invoke({"tema": "Pomodoro Technique"})

print(result.content)