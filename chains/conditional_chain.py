from  langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch , RunnableLambda


load_dotenv()

modelName = "claude-3-haiku-20240307"

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="The sentiment of the feedback, either positive or negative")


parser2 = PydanticOutputParser(pydantic_object=Feedback)
parser = StrOutputParser()
prompt = PromptTemplate(
    template = "Classify the sentiment of the following feedback text into positive or negative  \n {feedback}. \n {format_instructions}",
    input_variables = ["feedback"],
    partial_variables={"format_instructions":parser2.get_format_instructions()}
)


model = ChatAnthropic(model=modelName)


prompt2 = PromptTemplate(
    template = "Write a Appropriate response to the following positive feedback \n {feedback}",
    input_variables = ["feedback"],
   
)

prompt3 = PromptTemplate(
    template = "Write a Appropriate response to the following Negative feedback \n {feedback}",
    input_variables = ["feedback"],
   
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive" , prompt2 | model | parser),
    (lambda x:x.sentiment == "negative" , prompt3 | model | parser),
    RunnableLambda(lambda x: "Invalid sentiment")
   
)

classification_chain = prompt | model | parser2

chain = classification_chain | branch_chain
result = chain.invoke({"feedback":"Hi how are you?"})
print(result)

