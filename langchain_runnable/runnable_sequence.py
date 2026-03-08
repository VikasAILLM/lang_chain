# Runnable Primitive 

from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv


load_dotenv()

modelName = "claude-3-haiku-20240307"

prompt = PromptTemplate(
    template = "Give me a Joke on {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template = "Give me a explanation of  the following > {text}",
    input_variables=["text"]
)
model = ChatAnthropic(model=modelName)
parse = StrOutputParser()


chain = RunnableSequence(prompt, model, parse , prompt2, model, parse)

result = chain.invoke({"text":"Friends"})


print("result:" , result )