from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

str_output_parser = StrOutputParser()
llm = ChatOpenAI(model="gpt-5.2", temperature=0.3)

def parse_to_int(value: str) -> int:
    return int(value)

subjectTopicsExplanation = PromptTemplate(
    input_variables = ["subject", "value"],
    template = "Fale sobre {subject} e defina {value} tópicos principais."
)

topicsExplanationTranslation = PromptTemplate(
    input_variables = ["topicsExplanation"],
    template = "Traduza o {topicsExplanation} para inglês."
)

explanationResume = PromptTemplate(
    input_variables = ["translatedExplanation"],
    template = "Resume the {translatedExplanation}"
)

chain_topics = subjectTopicsExplanation | llm | str_output_parser
chain_translate = topicsExplanationTranslation | llm | str_output_parser
chain_resume = explanationResume | llm | str_output_parser

topics_text = chain_topics.invoke({"subject": "Técnica Pomodoro", "value": "2"})
translated_text = chain_translate.invoke(topics_text)
resumed_text = chain_resume.invoke(translated_text)

print(resumed_text)