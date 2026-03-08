# Runnable Primitive 

from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_core.runnables import RunnableParallel , RunnablePassthrough
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


joke_gen_chain = RunnableSequence(prompt, model, parse)

parallel_chain = RunnableParallel({
    "joke":RunnablePassthrough(), 
    "explanation": RunnableSequence(prompt2, model, parse)
}
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print("result:" , final_chain.invoke({"text":"Friends"}) )