import json
from sentence_transformers import SentenceTransformer

# Load an open-source model
model = SentenceTransformer('all-MiniLM-L6-v2')  # Small and fast

def get_embedding(text):
    embedding = model.encode(text).tolist()  # convert numpy array to list for JSON compatibility
    return embedding

def vector_embedding(data: list[dict]) -> list[dict]:
    """
    Given a list of arXiv entries (each a dict with 'summary', 'title', etc.),
    return the same entries with an added 'embedding' field (only from summary).
    """
    enriched_data = []

    for entry in data:
        summary = entry.get("summary", "")
        embedding = get_embedding(summary)

        enriched_data.append({
            "title": entry["title"],
            "summary": summary,
            "link": entry["link"],
            "authors": entry["authors"],
            "embedding": embedding
        })

    return enriched_data
