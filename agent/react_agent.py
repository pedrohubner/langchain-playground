from dotenv import load_dotenv
from langsmith import Client
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.agents import create_react_agent, AgentExecutor

load_dotenv()
client = Client()

@tool(
    "calculator", 
    description= "Tool que serve como calculador para realizar operações matemáticas.", 
    return_direct=True
)
def calculator(expression: str) -> str:
    try:
        result = eval(expression)
    except Exception as e:
        return f"Error: {e}"
    return str(result)

tools = [calculator]

# Entender porque código quebra com outros modelos, como gpt-4.1, por exemplo.
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
prompt = client.pull_prompt("hwchase17/react")

agent_chain = create_react_agent(llm, tools, prompt, stop_sequence=True)
agent_executor= AgentExecutor.from_agent_and_tools(
    agent=agent_chain,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=3
)

print(agent_executor.invoke({"input": "How much is 10 + 10?"}))