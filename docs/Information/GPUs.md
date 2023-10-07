# On GPUs

Whisper inference takes a long time with CPU. (Haven't tried yet but Diarization is bound to take even longer)
It will definitely require GPU processing.

This article has an interesting comparison of GPUs

[Whisper Deployment Decisions: Part I — Evaluating Latency, Costs, and Performance Metrics](https://blog.ml6.eu/whisper-deployment-decisions-part-i-evaluating-latency-costs-and-performance-metrics-d07f6edc9ec0)

The TL;DR is that the a cheaper hourly GPU (T4) is more cost effective.


## Cloud GPUs

Investigating options of GPU cloud compute to run a notebook. 

### AWS Sagemaker
- likely a more expensive option
- easy/straightforward to setup & use (I already use AWS)
- instances, GPUS, pricint info is confusing / difficult to sort through
- probably go for a `ml.g4dn.xlarge` or similar
- TODO: run a couple small Sagemaker jobs on a ml.g4dn.xlarge instance to estimate costs for longer tasks.


### Other options

[Reddit thread on GPUS](https://www.reddit.com/r/MachineLearning/comments/kcj80e/d_renting_high_end_gpu_resource_non_aws_options/)

#### Google Colab

- [colab pricing](https://colab.research.google.com/signup)
- pricing is really fucking opaque! (WTF is "compute unit" other than just "we want to hide the cost from you"? )
- reddit conversations suggest it might be a more expensive option


#### Vast.AI

- [vast.ai](https://cloud.vast.ai/)
- business model is cloud GPU rental matchmaking and aggregation service
- "Our software allows anyone to easily become a host by renting out their hardware."
- should save outputs to (different) cloud service continually in case interrupted
- probably pay under $1/hr for my needs
- seems to be the cheapest option -> worth at least trying out


#### Lambda Labs

- [lambdalabs](https://lambdalabs.com)
- [lambdalabs](https://lambdalabs.com/service/gpu-cloud)
- Great pricing page. Very clear. (Why can't & Google and AWS do better like this?)
- Seems to be under $1/hr for my needs (similar to vast.ai actually?)
- A GPU Cloud service (not a matchmaking rental like vast) and not a full-service Cloud service (like AWS, GCP)
- most compelling of this list! -> TODO: create an account and do some small experiements to estimate costs. 

