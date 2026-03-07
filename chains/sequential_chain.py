from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

modelName = "claude-3-haiku-20240307"

prompt = PromptTemplate(
    template = "Give me detail information about {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Generate a 5 pointer summary from the following text: {text}",
    input_variables = ["text"]
)

model = ChatAnthropic(model=modelName)

parser = StrOutputParser()

chain = prompt | model | parser | prompt2 | model | parser

result = chain.invoke({"topic":"India"})

print(result)

chain.get_graph().print_ascii()