from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage , SystemMessage, AIMessage
from dotenv import load_dotenv  


load_dotenv()
modelName = "claude-3-haiku-20240307"
llm = ChatAnthropic(model=modelName)

chatMessage = [SystemMessage(content="You are a helpful assistant")]

while True:
    userInput = input("User: ")
    if(userInput.lower() == "exit"):
        break
    chatMessage.append(HumanMessage(content=userInput))
    response = llm.invoke(chatMessage)
    chatMessage.append(AIMessage(content=response.content))
    
    print("AI: " + response.content)
    