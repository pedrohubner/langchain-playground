from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv()

prompt = ChatPromptTemplate([
    ("system", "You're a helpfull assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{input}")
])

llm = ChatOpenAI(model="gpt-5.2", temperature=0.7)

chain = prompt | llm

session_store: dict[str, InMemoryChatMessageHistory] = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "demo-session"}}

response1 = conversational_chain.invoke({"input": "Hello, my name is Pedro. How are you?"}, config=config)
print("Assistant: ", response1.content)
print("-"*60)

response2 = conversational_chain.invoke({"input": "Do you remember my name?"}, config=config)
print("Assistant: ", response2.content)
print("-"*60)

response3 = conversational_chain.invoke({"input": "Write motivational phrases with my name."}, config=config)
print("Assistant: ", response3.content)
print("-"*60)
