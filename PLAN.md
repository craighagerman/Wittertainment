# Plan



Idea

> Podcast search engine and fun content creator
>
> - First use case: Wittertainment podcast. Maybe after “My first million” etc
> - Scraper to get XML links, then download all podcasts. Then speech-to-text model to create script. Then vectorize, index etc and store in Vespa db. Then use free LLM, apply pre-training and create a chat service for wittertainees. Only answer questions mark and Simon would answer. Then identify text about individual movies and do sentiment, tone analysis on each.



**Podcast Text**

- Podcast RSS feed
- Download all podcasts
  - create a automated fetcher for weekly updating
- Convert podcast audio to text
  - Hugging Face: OpenAI Whisper
  - look into diarization to split and identify speakers



**LLM**

Research what I can/should to do fine-tuning/pre-training/post-training with LLM, which LLM to use, what approaches people use etc

- Download O/S LLM model (which?)
- Do fine-tuning with Podcast text
- Create chatbot



**Enrich Podcast Text**

- Find structured data with list of films (and TV)
  - use (somehow?) to do NER on text

- vectorize text and add useful metadata (dates, film NER etc)



**Data Storage**

- set up a Vespa.ai DB



**API**

- Set up FastAPI endpoints



**Frontend**

- Create a web app frontend (Vue ... or maybe Django)



**MVP Functionality**

- Chatbot about Wittertainment
- Text generator for a film review (e.g. Sex & The City III)
- Search engine to find review of a film (with type-ahead)
- Film suggester (like V.B.'s Viberary) -> type in what you are looking for and return film choices
- Authorship analysis (Mark vs Simon's language choices)





