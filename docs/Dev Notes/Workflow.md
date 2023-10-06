# Processing Workflow

## Pre-Preprocessing

collector
- download & save podcast audio for RSS feed


## Preprocessing

speech-to-text (cloud GPU)
- iterate over mps audio files -> extract text (& diarize) using Whisper -> save output text (s3?)

vesba initialization
- set up a vespa docker container & create an app package
- create and add schema to app package
- define rankings

vesba load
- iterate over podcast text
- vectorize title & body (convert to embeddings using SentenceTransformers)
- add text & embedddings & metadata to vespa


## Query

vespa query
- input query -> convert to embedding using SentenceTransformers -> HNSW lookup
- rank results
