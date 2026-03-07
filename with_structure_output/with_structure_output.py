from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from typing import TypedDict , Annotated

load_dotenv()

class Review(TypedDict):
    summary: Annotated[str , "A brief summary of the review"]
    rating: Annotated[int , "The rating given to the product"]
    sentiment: Annotated[str , "The sentiment of the review either positive, negative or neutral"]

# Create model
model = ChatAnthropic(model="claude-3-haiku-20240307")

# Apply structured output
structured_model = model.with_structured_output(Review)

response = structured_model.invoke(
    "Apple always delivers premium design. The iPhone 15 feels very solid in hand and the glass + aluminum finish looks clean and high-end."
)

print(response)