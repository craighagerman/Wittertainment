# On Topic Segmentation

n.b. by 'topic segmentation' I mean a broad catch-all that can include diarization, topic modeling, and clustering of text. 

Consider an automated speech recognition (ASR) transcription of a lengthy podcast. The output would not normally/automatically chunk text by speaker, or format into paragraphs and sections. This kind of segmention would be very useful (required?) for my end goals. 

Speaker diarization would help us identify blocks of content. Lots of back and forth = banter. Just Mark for 2-4 min = review. etc etc.

Same with segmenting into paragraphs/sections. It would help to identify topics (e.g within a review) and identify blocks of content. It would also be useful for summarization, information retrieval, text generation. 


## Overview of Approaches
- [Text Segmentation - Approaches, Datasets, and Evaluation Metrics](https://www.assemblyai.com/blog/text-segmentation-approaches-datasets-and-evaluation-metrics/)

### Supervised
- LSTM approach (Koshorek et al.)
- Transformer-based approach (Glavas et al. (2020))


### Unsupervised
- Lexical Cohesion
  - TextTiling (Hearst)
  - LCSeg (Galley et al. (2003))s
- Topic Modeling
  - TopicTiling
  - LDA
- Graph
  - GraphSeg (Glavas et al. (2016) )
- Similarity Measurement
  - Cosine Similarity

