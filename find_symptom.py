import json
from openai import OpenAI
from scipy.spatial.distance import cosine
import os
from set_env import set_env


def find_most_relevant_symptom(query):

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in environment variables.")
    
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )

    # Load the saved embeddings
    with open('./symptom_embeddings.json', 'r') as file:
        symptom_embeddings = json.load(file)
    
    # Convert the query to an embedding
    response = client.embeddings.create(
        input=query,
        model="text-embedding-ada-002"
    )
    query_embedding = response.data[0].embedding
    
    # Calculate similarities
    similarities = {key: 1 - cosine(query_embedding, embedding) for key, embedding in symptom_embeddings.items()}
    
    # Find the most relevant key
    most_relevant_key = max(similarities, key=similarities.get)
    
    # Return the key and its corresponding value
    return most_relevant_key, symptoms[most_relevant_key]

# 示例调用
if __name__ == "__main__":
    query = "I keep feeling like I've been here before."
    key, value = find_most_relevant_symptom(query)
    print(f"Key: {key}, Value: {value}")