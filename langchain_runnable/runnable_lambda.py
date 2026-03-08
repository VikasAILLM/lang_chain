from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnableParallel , RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def wordCounter(text: str) -> int:
    return len(text.split())

prompt = PromptTemplate(
    template="Generate a joke: {text}",
    input_variables=["text"]
)

model = ChatAnthropic(model="claude-3-haiku-20240307")
parser = StrOutputParser()

joke_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    joke=RunnablePassthrough(),  # pass joke text forward
    word_count=RunnableLambda(wordCounter)
)

final_chain = joke_chain | parallel_chain

result = final_chain.invoke({"text": "Humans"})

print("result:", result)