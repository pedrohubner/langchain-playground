from langchain_core.prompts import PromptTemplate

template = """Qual a versão mais recente da LLM do {agent}"""

prompt = PromptTemplate(
    input_variables=["agent"],
    template=template,
)

result = prompt.format(agent="OpenAI")

print(result)
