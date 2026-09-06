---
title: 'Schema-Tune: Noise-Driven Bias Mitigation in Transformer-based Language Models'
year: 2025
type: journal
authors: Omid Shokrollahi, Ruthvik Penumatcha, Faezeh Ensan, Zeinab Noorian
venue: Machine Learning, 114(73)
doi: 10.1007/s10994-024-06670-4
area: rai
tags:
- Responsible AI
- LLMs
order: 5
---
In this paper, we introduce Schema-Tune, a zero-shot self-supervised framework for bias mitigation in transformer-based language models. Schema-Tune introduces curated and optimized adaptive noises to the input embeddings of transformer models to challenge the models' embedded stereotypes. Through continuous fine-tuning steps, these noises prompt the models to change their internal semantic representations towards more socially fair representations. For fine-tuning language models, Schema-Tune relies on very limited input data: a couple of sentences formed by social group terms. Additionally, Schema-Tune defines bias and language model performance measures independently from labeled data. These measures are then used in forming the language model's fine-tuning objective function and in searching for effective noises in the embedding space. Experimental evaluation over the StereoSet and Crows-Pairs datasets confirms that Schema-Tune is effective in mitigating bias in different social stereotype categories, including gender, race, and religion.
