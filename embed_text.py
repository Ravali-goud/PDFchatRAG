from sentence_transformers import SentenceTransformer

def embed_chunks(chunks, model_name="all-MiniLM-L6-v2"):
    """Generate embeddings for text chunks."""
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks)
    return embeddings

# Example Usage
if __name__ == "__main__":
    chunks = ["This is chunk 1.", "This is chunk 2."]
    embeddings = embed_chunks(chunks)
    print("Embeddings:\n", embeddings)
