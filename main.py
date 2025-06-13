import os
import logging
from utils.crawler import get_latest_arxiv_paper
from utils.model import vector_embedding, get_embedding
from utils.db import save_data_embedded, retrieve_similar_entries


def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler("logs/arxiv_logger.log", mode='a', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger()


def main():
    logger = setup_logger()
    logger.info("🚀 Starting arXiv RAG pipeline")

    raw_data = get_latest_arxiv_paper("cs.AI")
    logger.info(f"📄 Fetched {len(raw_data)} arXiv entries")

    data_embedded = vector_embedding(raw_data)
    logger.info("🧠 Embeddings generated for all entries")

    # Uncomment to save to DB
    # save_data_embedded(data_embedded)
    # logger.info("💾 Data saved into PostgreSQL vector DB")

    user_question = input("💬 Write some idea you're interested in, and I’ll search for the latest papers: ")
    logger.info(f"📝 User input: {user_question}")

    # Uncomment when retrieval is ready
    # info_retrieved = retrieve_similar_entries(user_question)
    # logger.info(f"🔍 Retrieved {len(info_retrieved)} related papers for user query")

    logger.info("✅ Pipeline finished")
    logger.info("_" * 100)


if __name__ == "__main__":
    main()
