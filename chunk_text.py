def chunk_text(text, chunk_size=512):
    """Split text into smaller chunks."""
    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

# Example Usage
if __name__ == "__main__":
    sample_text = "This is a sample text for chunking. " * 100
    chunks = chunk_text(sample_text)
    print("Chunks:\n", chunks)
