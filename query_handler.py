import numpy as np
import store_embeddings

def query_vector(query, model_name="all-MiniLM-L6-v2"):
    """Convert a user query into an embedding."""
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(model_name)
    return model.encode([query])

def retrieve_similar_chunks(query_embedding, index, chunks, k=5):
    """Retrieve the top-k similar chunks for a query."""
    distances, indices = index.search(np.array(query_embedding), k)
    return [chunks[i] for i in indices[0]]

# Example Usage
if __name__ == "__main__":
    chunks = ["This is chunk 1.", "This is chunk 2."]
    query = "Find chunk 1"
    embeddings = np.random.rand(len(chunks), 384)  # Example embeddings
    index = store_embeddings.store_embeddings(embeddings)
    query_embedding = query_vector(query)
    retrieved_chunks = retrieve_similar_chunks(query_embedding, index, chunks)
    print("Retrieved Chunks:\n", retrieved_chunks)
