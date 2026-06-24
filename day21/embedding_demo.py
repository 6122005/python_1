from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

sentences = [
    "I love cricket",
    "I enjoy cricket",
    "How to cook pasta"
]

embeddings = model.encode(sentences)

similarity = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)

print("output:", similarity)