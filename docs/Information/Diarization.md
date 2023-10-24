# Diarization

## [Speaker Diarization: An Introductory Overview](https://lajavaness.medium.com/speaker-diarization-an-introductory-overview-c070a3bfea70#:~:text=Speaker%20diarization%20pipeline%3A%20who%20spoke,deep%20learning%20and%20neural%20networks.)

### Main approaches

#### Supervised approach
- treat as a classification problem
- train a model to recognize finite number of speakers
- speakers identified during inference must, of course be among those in the training data 
- model is trained on the audio data. (But could also be a text-based classifier for some use cases I think (e.g. stylometry classifier))

#### Unsupervised approach
- treat as a clustering problem
- cluster audio segments according to the speaker based on extracted audio features.
- most common approach


### Early approaches 
- Digital Signal Processing techniques
- Statistical modeling (HMM, GMM, etc)

### Modern approaches
- Deep learning-based
- constructed of a pipeline involving several sub-tasks

Typical Pipeline:
- input audio
- Voice Activity Detection (VAD) (Binary classification based on speech activity)
- Audio Embedding (Encoder model: extract voice characteristics and encode audio in the latent space)
- Clustering & Diarizer model (clustering or classification of the embedded audio segments)
- labeled audio segments



## [Comparing state-of-the-art speaker diarization frameworks : Pyannote vs Nemo](https://lajavaness.medium.com/comparing-state-of-the-art-speaker-diarization-frameworks-pyannote-vs-nemo-31a191c6300)


Comparison of PyAnnote & NeMo


