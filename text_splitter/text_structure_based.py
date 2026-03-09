from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """India is a diverse and vibrant country located in South Asia. 
It is known for its rich history, cultural heritage, and democratic system. 
India is the world’s largest democracy and one of the fastest-growing major economies. 
The country has a wide variety of languages, religions, traditions, and festivals, 
which reflect its unity in diversity. Major cities like New Delhi, Mumbai, and Bengaluru 
play an important role in politics, finance, and technology. India is also famous for its 
historical monuments such as the Taj Mahal and for its contributions to fields like science, 
mathematics, and information technology. Overall, India is a country with a unique blend 
of ancient traditions and modern development."""

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

texts = text_splitter.split_text(text)

print(texts)
print(len(texts))