# Initial Plan

inception date: 2023-09029

## The Vision

Create a search engine for Kermode & Mayo's film review podcast

Simple functionality
- enter a film / TV show name -> return podcasts that mention the title

Add-on functionality
- identify which podcast contains a full review of the title vs brief review vs mention
- identify timestamp where above occurs
- option to play given podcast from above timestamp

Advanced functionality
- LLM-powered
- text generation -> generate new (fake) review for fake film (e.g. new Sex & the City movie)
- Chatbot / Question-Answering / Conversational AI
- Semantic search
- Summarization - enter film title -> return summary of Mark's review
- "Vibe search" (like Vicki Boykis's Vibery project)
- Identify similarities -> "if you like this, you will like that"
- Blockbuster analysis - identify attributes that go into a hit vs a flop (in Mark's review)
- HITL labeling (like BBG Indicators app)

Extras
- Authorship analysis (stylometry) of Mark vs Simon speech
- "Nabokov's favorite word is mauve" style analysis
- other Comp Ling / NLP analysis

Future functionality
- load other podcast -> do comparative analysis, suggest podcast (not episode) based on search, etc
- Podcast rating for branding -> rate across various dimensions (content, profanity, other) - kind of like BBFC rating
- Get other film/TV data (e.g. reviews; year, director, actor metadata, etc) -> incorporate into LLM & recommender


## Inspiration

Where did the idea come from? Two things...

1. I listen to the podcasts but end up watching things much later and sometimes can't remember how it was reviewed. Other times I see a title and wonder what Mark said about it ... but don't know in which podcast it was mentioned. I'd like to be able to find and be reminded of the review and comments easily (in text form).
2. Vicki Boykis's Vibery (https://github.com/veekaybee/viberary) project is a great inspiration. I love her writing style. The vibery project inspires me to take on a personal passion project as well. 


------------------------------------------------------------------------------------------

## What is needed (Ideas)
(Rough Implementation plan)


### Podcast Collector
Have to be able to collect past podcasts and retrieve new ones

- get link to RSS feed(s) (n.b. old and new show)
- Create `collector` to fetch & parse feeds and download
  - Python project: use feedparser, fastApi


### Speech-to-Text
Need to convert podcast audio to text

- use trained speech-to-text model (huggingface: OpenAI Whisper)

Other
- preferable to also do Diarisation (speaker identification)
  - have to look into how to do that


## Vectorize / LLM
Need to vectorize text

- use embedddings from LLM (huggingface: ms-marko?)
- vectorize podcast text
- fine-tune LLM using podcast embeddings
- create chatbot
- create RAG IR search


## Storage / DB
Need to store (1) audio data (probably), (2) raw text data (2) vector embeddings

- use Vespa.ai DB for all of above


## API
Have to wrap everything up together with an API

- use Python FastAPI


## Frontend
Everything could work as a CLI, but it'd be far more usable to have a front end. A web app is probably best/easiest.

- Create basic web app 
  - probably using Vue 3 (since I have some experience)
    - composition API
    - Pinia store
  - alternatives: Django (no experience, but I'd like to learn), or a Bootstrap UI (no experience)


## Infrastructure
Need an approach to wrap everything up and productionize. 
For a personal project at this stage I think its better to use a mono-repo, docker containers for all the separate services and docker compose to combine them. 

- Docker containers + docker compose


## Cloud / Server
Need an inexpensive option for prod deployment. Maybe just pay for a cheap VPS (Ramnode) or AWS Lightsail? Maybe Digital Ocean. TBD, but the cloud choice could affect other decisions. 

- need a VPS probably


------------------------------------------------------------------------------------------

