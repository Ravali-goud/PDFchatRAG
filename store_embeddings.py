import faiss
import numpy as np

def store_embeddings(embeddings):
    """Store embeddings in a FAISS index."""
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

# Example Usage
if __name__ == "__main__":
    embeddings = np.random.rand(10, 384)  # Example embeddings
    index = store_embeddings(embeddings)
    print("FAISS Index Created!")
