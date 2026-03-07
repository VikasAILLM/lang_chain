from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv


load_dotenv()
modelName = "claude-3-haiku-20240307"
llm = ChatAnthropic(model=modelName)

response = llm.invoke("What is reddit?")

print(response.content)