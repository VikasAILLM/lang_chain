from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

modelName = "claude-3-haiku-20240307"

prompt = PromptTemplate(
    template="Generate a LinkedIn post about {topic}.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a Twitter post about {topic}.",
    input_variables=["topic"]
)

model = ChatAnthropic(model=modelName)

parser = StrOutputParser()

# Create individual chains
linkedin_chain = prompt | model | parser
twitter_chain = prompt2 | model | parser

# Parallel chain
parallel_chain = RunnableParallel(
    linkedin_post=linkedin_chain,
    twitter_post=twitter_chain
)

result = parallel_chain.invoke({"topic": "Next.js and React.js"})

print("result:", result)