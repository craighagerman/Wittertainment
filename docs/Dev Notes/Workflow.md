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

vesba load corpus
- iterate over podcast text
- vectorize title & body (convert to embeddings using SentenceTransformers)
- add text & embedddings & metadata to vespa


## Run time

frontend web app
- Vue 3 app with basic/usual search functionality

api endpoint
- FastAPI endpoint(s) for receiving query from frontend, querying vespa, parsing and returning results

vespa query
- input query -> convert to embedding using SentenceTransformers -> HNSW lookup
- rank results and return
