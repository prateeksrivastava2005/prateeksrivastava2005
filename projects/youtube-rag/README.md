# YouTube RAG — Semantic Video Search & Question Answering

Built by **Prateek Srivastava** *(LangChain, LangGraph, PostgreSQL, pgvector, Python)*

## Architecture Overview
1. **Video Ingestion & Transcript Extraction**:
   - Fetches subtitles and automated captions using YouTube Transcript API.
   - Cleans formatting, strips filler tags, and extracts millisecond-accurate timestamps.
2. **Recursive Semantic Chunking**:
   - Employs sliding window chunking (500 tokens, 50 token overlap) with semantic boundary detection.
   - Embeds transcript segments using state-of-the-art embedding models.
3. **Vector Database (PostgreSQL + pgvector)**:
   - Stores chunk embeddings with metadata: `video_id`, `start_time`, `end_time`, `text`.
   - Executes HNSW index cosine distance similarity searches (`<->`).
4. **LangGraph Agentic Search Loop**:
   - Evaluates retrieved chunk relevance.
   - If cosine similarity or relevance score is below confidence threshold, refines the search query using sub-query generation.
5. **Timestamped Answer Synthesis**:
   - Generates concise answers with direct YouTube timestamp URLs (e.g., `https://youtu.be/<id>?t=142`).

