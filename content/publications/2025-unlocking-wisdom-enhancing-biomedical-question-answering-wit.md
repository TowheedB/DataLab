---
title: 'Unlocking Wisdom: Enhancing Biomedical Question Answering with Domain Knowledge'
year: 2025
type: journal
authors: Bita Azad, Mahdiyar Ali Akbar Alavi, Parastoo Jafarzadeh, Faezeh Ensan, Dimitri Androutsos
venue: Knowledge and Information Systems, 67, 4087–4112
doi: 10.1007/s10115-025-02338-0
area: bio
tags:
- Biomedical IR
- QA
order: 6
---
Biomedical factoid question answering aims to provide factual answers from biomedical articles for questions related to the biomedical or healthcare domain. Recent advances in biomedical factoid question answering primarily involve using pre-trained Language Models (LMs) to retrieve relevant passages or comprehend text snippets for extracting accurate answers. However, due to the relatively smaller scale of biomedical datasets compared to those used in broader domains, fine-tuning LMs for the biomedical domain often results in decreased accuracy. To address this, we introduce the Biomedical Knowledge-enhanced Question Answering Framework (BK-QAF). This framework retrieves, ranks, and employs domain-specific concepts from the Unified Medical Language System (UMLS) to enhance the comprehension and reasoning capabilities of language models. By using Graph Attention Networks (GATs) to analyze the interconnections and relationships between entities in biomedical texts, we identify the most relevant concepts for the query. The framework then ranks these UMLS concepts by relevance, expands the questions with the top-ranked concepts, and processes them using a fine-tuned language model. We evaluated our framework using the BioASQ 6b, 7b, and 8b datasets, which are widely adopted in the field. Empirical evaluations demonstrate the superior performance of the proposed framework over state-of-the-art baselines across metrics such as Strict Accuracy and MRR@5. The framework's effectiveness is assessed using three distinct GAT architectures, demonstrating robustness across different configurations.
