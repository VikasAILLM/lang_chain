from langchain_core.runnables import RunnableBranch, RunnableSequence, RunnableParallel , RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

parser = StrOutputParser()
modelName = "claude-3-haiku-20240307"

model = ChatAnthropic(model=modelName)

prompt = PromptTemplate(
    template = "write a detailed story  on {text}",
    input_variables=["text"]
)
prompt2 = PromptTemplate(
    template = "summarize the story  {text}",
    input_variables=["text"]
)


report_gen_chain = prompt | model | parser

branch_chain = RunnableBranch(
    (lambda x:len(x.split()) > 500 , RunnableSequence(prompt2, model ,parser)), 
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({"text":"Friends"})

print(result)