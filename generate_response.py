import os
import openai
import time

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your API key

# Function to list available models
try:
    models = openai.Model.list()
    print(models)
except openai.error.AuthenticationError as e:
    print("Authentication error:", e)


# Function to generate a response using GPT-3.5
def generate_response(retrieved_chunks, query):
    """Generate a response using GPT-3.5."""
    context = " ".join(retrieved_chunks)
    prompt = f"Answer the query based on the following context:\n{context}\n\nQuery: {query}"

    try:
        # Make API call to OpenAI for response generation
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.RateLimitError:
        # Handle rate limit exceeded error by waiting and retrying
        print("Rate limit exceeded. Retrying after a short delay...")
        time.sleep(60)  # Wait for 60 seconds before retrying
        return generate_response(retrieved_chunks, query)  # Retry the request
    except openai.error.AuthenticationError as e:
        print("Authentication error:", e)
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example Usage
if __name__ == "__main__":
    # Sample data
    retrieved_chunks = ["This is relevant chunk 1.", "This is relevant chunk 2."]
    query = "What is chunk 1 about?"

    # Generate and print the response
    response = generate_response(retrieved_chunks, query)
    if response:
        print("Response:\n", response)
    else:
        print("Failed to generate a response.")
