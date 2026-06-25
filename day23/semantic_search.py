import chromadb

from sentence_transformers import SentenceTransformer

from data.faq_data import faqs


print("=" * 60)
print("LOADING EMBEDDING MODEL")
print("=" * 60)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


print("=" * 60)
print("CONNECTING TO CHROMADB")
print("=" * 60)

client = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = client.get_or_create_collection(
    name="faq_collection"
)


print("=" * 60)
print("GENERATING FAQ EMBEDDINGS")
print("=" * 60)

embeddings = model.encode(faqs)

print(f"\nTotal FAQs: {len(faqs)}")
print(f"Embedding Dimension: {len(embeddings[0])}")


existing_count = collection.count()

if existing_count == 0:

    print("\nStoring FAQs in ChromaDB...\n")

    collection.add(
        documents=faqs,
        embeddings=embeddings.tolist(),
        ids=[str(i) for i in range(len(faqs))]
    )

    print("FAQs Stored Successfully!")

else:

    print(
        f"\nCollection already contains {existing_count} records."
    )


print("\nSemantic Search Ready!")
print("=" * 60)


while True:

    query = input(
        "\nAsk a Question (q to quit): "
    )

    if query.lower() == "q":
        print("\nGoodbye!")
        break

    query_embedding = model.encode(
        query
    )

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=5
    )

    print("\n" + "=" * 60)
    print("TOP 5 MATCHES")
    print("=" * 60)

    matches = results["documents"][0]

    for index, match in enumerate(
        matches,
        start=1
    ):
        print(f"{index}. {match}")

    print("=" * 60)