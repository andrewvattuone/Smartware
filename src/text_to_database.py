import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./chroma_db")

collection_name = "text_embeddings"

try:
    collection = client.get_collection(collection_name)
except:
    collection = client.create_collection(name=collection_name)

# Step 3: Initialize Embedding Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 4: Text String to Send
# Conversation 1: Space Exploration
conversation1 = [
    "Alex: Did you hear that NASA is planning another mission to Mars?",
    "Jordan: Yeah, it’s incredible how far space exploration has come in the past decade.",
    "Alex: I wonder if we’ll see a manned mission to Mars within our lifetime.",
    "Jordan: With the advancements in rocket technology, it’s definitely possible.",
    "Alex: SpaceX and other private companies are pushing the boundaries faster than ever before."
]

conversation1 = " ".join(conversation1)

# Conversation 2: Artificial Intelligence
conversation2 = [
    "Emma: AI models like LLaMA and Gemini are getting smarter every day.",
    "Liam: It’s fascinating how they can understand and generate human-like text now.",
    "Emma: True, but it also raises concerns about misinformation and ethical use.",
    "Liam: That’s why responsible AI development and regulation are so important.",
    "Emma: Agreed! We need to strike a balance between innovation and safety."
]

conversation2 = " ".join(conversation2)

# Conversation 3: Climate Change
conversation3 = [
    "Maya: Climate change is becoming more apparent with all these extreme weather events.",
    "Tyler: I know, it’s scary how quickly things are changing.",
    "Maya: We really need to invest more in renewable energy sources.",
    "Tyler: Solar and wind energy are becoming more affordable every year.",
    "Maya: Let’s hope governments and industries step up before it’s too late."
]

conversation3 = " ".join(conversation3)

conversation4 = [
    "Chris: The ocean covers more than 70% of the Earth's surface, yet we've only explored about 5% of it.",
    "Taylor: That's incredible! There could be so many undiscovered species down there.",
    "Chris: Absolutely. Deep-sea exploration has advanced, but the extreme conditions make it challenging.",
    "Taylor: I read that some researchers are using AI-powered submarines to map the ocean floor.",
    "Chris: Yeah, technology is revolutionizing oceanography, and who knows what mysteries we'll uncover next!"
]

# Convert to a single string
conversation4 = " ".join(conversation4)

documents = [
    conversation1,
    conversation2,
    conversation3,
    conversation4
]

print(documents)

# Step 5: Generate Embedding
embeddings = embedding_model.encode(documents).tolist()

# Step 6: Add the Text and Its Embedding to the Collection
collection.add(
    embeddings=embeddings,
    documents=documents,
    ids=[f"doc{i+1}" for i in range(len(documents))]
)