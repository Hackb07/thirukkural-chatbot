import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load FAISS index
index = faiss.read_index("thirukkural.faiss")

# Load dataset
df = pickle.load(open("thirukkural.pkl", "rb"))

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_kurals(query, top_k=30):
    """
    Retrieves the most relevant Thirukkural(s) for a given query
    """
    # Encode user query
    query_embedding = model.encode([query])

    # Search FAISS
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
        row = df.iloc[idx]
        results.append({
            "kural_id": row["kural_id"],
            "adhigaram": row["adhigaram_name"],
            "paal": row["paal"],
            "kural_tamil": row["kural_tamil"],
            "meaning_english": row["meaning_english"],
            "explanation": row["explanation"]
        })

    return results
