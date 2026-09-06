---
title: Towards Semantic-Driven Boolean Query Formalization for Biomedical Systematic Literature Reviews
year: 2023
type: journal
authors: Mohammadreza Pourreza, Faezeh Ensan
venue: International Journal of Medical Informatics, 170
doi: 10.1016/j.ijmedinf.2022.104928
area: bio
tags:
- Biomedical IR
order: 16
---
Objective: Study identification refers to formalizing an effective search over biomedical databases for retrieving all eligible evidence for a systematic review. Manual construction of queries, where a user submit a search query for which a biomedical search system such as PubMed would identify the most relevant documents, has been recognized as a very costly step in conducting systematic reviews. The objective of this paper is to present an automatic query generation approach to reduce the time and labor cost of manual biomedical study identification.

Materials and methods: The evaluation benchmark is the widely adopted CLEF 2018 Technology Assisted Reviews (TAR) collection, with 72 systematic reviews on Diagnosis Test Accuracy. We use and fine-tune pre-trained language models for generating high-level key-phrases and their dense embeddings. We constructed and published a dataset consists of almost one million PubMed articles' abstracts and their keywords for fine-tuning pre-trained language models. We also use concepts that are represented in the Unified Medical Language System, UMLS, for query expansion and embedding generation. We exploit and test different clustering methods, namely Agglomerative clustering, Affinity Propagation, and K-Means, over the generated embeddings to form query clauses.

Results: Our proposed methods outperform existing state-of-the-art automatic query generation models across Precision (0.0821 compared with 0.005), Recall (0.9676 compared with 0.878), and F-measures (0.2898 compared with 0.0356 in F3 measure). In addition, some of the proposed methods can even outperform the performance of the manually crafted queries in some specific measures.

Conclusion: The proposed model in this paper can be utilized to form an effective initial search query that can be further refined and updated by human reviewers for achieving the desired performance. For future work, we would like to explore the application of the presented query formalization methods in existing study identification methodologies and techniques, especially those that iteratively train machine learning models based on the domain experts' feedback on the relevancy of the retrieved studies.
