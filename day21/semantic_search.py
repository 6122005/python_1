from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Python is a programming language",
    "Cricket is a popular sport in India",
    "Machine learning is part of artificial intelligence",
    "Virat Kohli is a famous cricketer"
]

query = "AI and ML"

doc_embeddings = model.encode(documents)
query_embedding = model.encode(query)

scores = util.cos_sim(query_embedding, doc_embeddings)

for doc, score in zip(documents, scores[0]):
    print(f"{score:.4f} --> {doc}")