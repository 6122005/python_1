import chromadb

client = chromadb.Client()

collection = client.create_collection(
    name="learning_docs"
)

collection.add(
    documents = [
    "Python is a programming language",
    "Java is widely used",
    "Machine learning is part of AI",
    "Deep learning uses neural networks",
    "Cricket is a popular sport",
    "Football is played worldwide",
    "Mathematics is important",
    "Physics studies matter",
    "Chemistry studies reactions",
    "Biology studies living organisms",
    "India is a large country",
    "Mumbai is in India",
    "Delhi is the capital of India",
    "Data science uses statistics",
    "SQL manages databases",
    "MongoDB is NoSQL",
    "Docker creates containers",
    "Git tracks code changes",
    "Linux powers servers",
    "Cloud computing is growing"
],
    ids=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
)

results = collection.query(
    query_texts=[
        "How do I learn cricket?"
    ],
    n_results=2
)

print(results)

print("\nTop 3 Results:\n")

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"{i}. {doc}")