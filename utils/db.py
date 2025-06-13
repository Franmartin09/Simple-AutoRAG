import psycopg2
from psycopg2.extras import execute_values
import os
from typing import List, Dict
import numpy as np
from utils.model import get_embedding
# PostgreSQL connection (adjust with your env or .env support)
DB_CONFIG = {
    "dbname": "your_db",
    "user": "your_user",
    "password": "your_password",
    "host": "localhost",
    "port": 5432
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def save_data_embedded(data: List[Dict]):
    """
    Save a list of arXiv entries (each a dict with 'summary', 'title', etc.) with embeddings.
    """
    to_insert = []
    for entry in data:
        to_insert.append((entry.get("title", ""), ", ".join(entry.get("authors", [])), entry.get("link", ""), entry.get("summary", ""), entry.get("embedding", "")))

    query = """
    INSERT INTO arxiv_papers (title, authors, link, summary, embedding)
    VALUES %s
    ON CONFLICT (link) DO NOTHING;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            execute_values(cur, query, to_insert)

def retrieve_similar_entries(user_question: str, top_k: int = 2) -> List[Dict]:
    """
    Retrieve top_k most similar entries from DB given a user question.
    """
    question_embedding = get_embedding(user_question)

    query = f"""
    SELECT title, authors, link, summary,
           embedding <#> %s AS distance
    FROM arxiv_papers
    ORDER BY distance ASC
    LIMIT %s;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (question_embedding, top_k))
            rows = cur.fetchall()

    results = []
    for row in rows:
        results.append({
            "title": row[0],
            "authors": row[1],
            "link": row[2],
            "summary": row[3],
            "distance": row[4]
        })

    return results
