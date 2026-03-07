from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

modelName = "claude-3-haiku-20240307"

prompt = PromptTemplate(
    template = "Generate a detail notes about {topic}.",
    input_variables = ["topic"]   
)


prompt2 = PromptTemplate(
    template = "Generate a 5 Quiz question based on the following text : {topic}",
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template = "Merge the Provided notes and quiz into a single document \n notes > {notes} and quiz > {quiz}",
    input_variables=["notes", "quiz"]
)

model = ChatAnthropic(model=modelName)
model2 = ChatAnthropic(model=modelName)

parser = StrOutputParser()


parallel_chain = RunnableParallel(
    {
        "notes": prompt | model | parser,
        "quiz": prompt2 | model2 | parser
    }
)


merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain
result = chain.invoke({"topic":"India"})

print(result)

chain.get_graph().print_ascii()
