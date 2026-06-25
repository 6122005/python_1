from sentence_transformers import SentenceTransformer

print("=" * 60)
print("LOADING MODEL...")
print("=" * 60)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

sentence = "How do I reset my password?"

embedding = model.encode(sentence)

print("\nSentence:")
print(sentence)

print("\nEmbedding Type:")
print(type(embedding))

print("\nEmbedding Dimension:")
print(len(embedding))

print("\nFirst 10 Values:")
print(embedding[:10])

print("\nEmbedding Generated Successfully!")