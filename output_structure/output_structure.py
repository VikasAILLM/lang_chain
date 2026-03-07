from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

class PersonModel(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age")
    wifeName: str = Field(description="The name of the person's wife")
    profession: str = Field(description="The person's profession")


# Create parser
parser = PydanticOutputParser(pydantic_object=PersonModel)

# Create prompt template
template = PromptTemplate(
    template="""
Extract the name , wifeName , profession and age of the person.

{format_instructions}

Person: {value}

Return ONLY valid JSON.
""",
    input_variables=["value"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


# Create model
model = ChatAnthropic(model="claude-3-haiku-20240307")

chain = template | model | parser   


model_response = chain.invoke({"value": "virat kohli"})

print(model_response)