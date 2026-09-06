---
title: A Knowledge Graph Embedding Model for Answering Factoid Entity Questions
year: 2025
type: journal
authors: Parastoo Jafarzadeh, Faezeh Ensan, Mahdiyar Ali Akbar Alavi, Fattane Zarrinkalam
venue: ACM Transactions on Information Systems, 43(2), 1–27
doi: 10.1145/3678003
area: kg
tags:
- Knowledge Graphs
- QA
order: 4
---
Factoid entity questions (FEQ), which seek answers in the form of a single entity from knowledge sources, such as DBpedia and Wikidata, constitute a substantial portion of user queries in search engines. This article introduces the knowledge graph embedding model for FEQ (KGE-FEQ) answering. Leveraging a textual knowledge graph derived from extensive text collections, KGE-FEQ encodes textual relationships between entities. The model employs a two-step process: (1) Triple Retrieval, where relevant triples are retrieved from the textual knowledge graph based on semantic similarities to the question, and (2) Answer Selection, where a knowledge graph embedding approach is utilized for answering the question. This involves positioning the embedding for the answer entity close to the embedding of the question entity, incorporating a vector representing the question and textual relations between entities. Extensive experiments evaluate the performance of the proposed approach, comparing KGE-FEQ to state-of-the-art baselines in FEQ answering and the most advanced open-domain question answering techniques applied to FEQs. The results show that KGE-FEQ outperforms existing methods across different datasets. Ablation studies highlights the effectiveness of KGE-FEQ when both the question and textual relations between entities are considered for answering questions.
