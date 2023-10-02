# On Vespa.ai DB

## What Vespa can do

Search
- full text search
- fast ANN in vector space with HNSW algorithm
- support for 2-phase ranking
- ranking using mathematical expressions, tensors, models (XGBoost, etc any ONNX)
- Grouping, deduplication and aggregation over all matches.

Recommendation and Personalization
- search in vector space

Conversational AI
- Vespa integrates ML - can do model inference using ONNX, storing vectors and text and immediately retrieve the data in queries,

Semi-structured navigation
- allow users to navigate in the data using both structured navigation and text search
- can switch between drilling down by metadata and searching by text seamlessly without losing context

Personal search


## Vespa sample applications list includes...
- album recommendation
- semantic search
- customizing embeddings
- news search and recommendation
- billion scale image search
- Text Ranking (SoTA)
- e-commerce search
- extractive question answering
- search as you type and search suggestions
- Vespa as ML model inference server


## Links
- Vespa use cases: [https://vespa.ai/usecases]
- Vespa sample projects: [https://github.com/vespa-engine/sample-apps/tree/master]
- Docker quickstart: [https://docs.vespa.ai/en/vespa-quick-start.html]
- Pyvespa quickstart: [https://pyvespa.readthedocs.io/en/latest/getting-started-pyvespa.html]


------------------------------------------------------------------------------------------------------------------------

# Vespa install & setup notes

Install the Vespa CLI:

```bash 
$ brew install vespa-cli
```

Set local target:
```bash
$ vespa config set target local
```

Start a Vespa Docker container:
```bash
$ docker run --detach --name vespa --hostname vespa-container \
  --publish 8080:8080 --publish 19071:19071 \
  vespaengine/vespa
```

Initialize myapp/ to a copy of a sample application package:
```bash
$ vespa clone album-recommendation myapp && cd myapp
```

Deploy it:
```bash
$ vespa deploy --wait 300
```

Feed documents:
```bash
$ vespa feed ext/documents.jsonl
```


Issue queries:
```bash
$ vespa query "select * from music where album contains 'head'" language=en-US

$ vespa query "select * from music where true" "ranking=rank_albums" "input.query(user_profile)={pop:0.8,rock:0.2,jazz:0.1}"

$ vespa query "select * from music where true" \
  "ranking=rank_albums" \
  "input.query(user_profile)={pop:0.8,rock:0.2,jazz:0.1}" \
  "presentation.format.tensors=short-value"
```
