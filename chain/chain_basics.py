from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-5.2", temperature=0.3)

prompt = ChatPromptTemplate.from_messages([
    {"role": "system", "content": "Você é um especialista em {specialty} e só produz respostas em ingles."},
    {"role": "user", "content": "Me explique {content}"}
])

chain = prompt | llm

result = chain.invoke({
    "specialty": "física básica",
    "content": "de forma simples o que são as três leis de newton"
})

# print(type(chain))

print(result.content)