from langchain_text_splitters import CharacterTextSplitter

text = """
India is a diverse and vibrant country located in South Asia.
It is known for its rich history, cultural heritage, and democratic system.
India is the world’s largest democracy and one of the fastest-growing economies.
The country has many languages, religions, traditions, and festivals.
Major cities include New Delhi, Mumbai, and Bengaluru.
India is also famous for monuments like the Taj Mahal.
"""

# Create text splitter
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=20
)

# Split text
chunks = text_splitter.split_text(text)

print("Total Chunks:", len(chunks))