---
title: Learning to Rank Query Expansion Terms for COVID-19 Scholarly Search
year: 2023
type: journal
authors: Ayesha Khader, Faezeh Ensan
venue: Journal of Biomedical Informatics, 142
doi: 10.1016/j.jbi.2023.104386
area: bio
tags:
- Biomedical IR
- Learning to Rank
order: 17
---
Objective: With the onset of the Coronavirus Disease 2019 (COVID-19) pandemic, there has been a surge in the number of publicly available biomedical information sources, which makes it an increasingly challenging research goal to retrieve a relevant text to a topic of interest. In this paper, we propose a Contextual Query Expansion framework based on the clinical Domain knowledge (CQED) for formalizing an effective search over PubMed to retrieve relevant COVID-19 scholarly articles to a given information need.

Materials and Methods: For the sake of training and evaluation, we use the widely adopted TREC-COVID benchmark. Given a query, the proposed framework utilizes a contextual and a domain-specific neural language model to generate a set of candidate query expansion terms that enrich the original query. Moreover, the framework includes a multi-head attention mechanism that is trained alongside a learning-to-rank model for re-ranking the list of generated expansion candidate terms. The original query and the top-ranked expansion terms are posed to the PubMed search engine for retrieving relevant scholarly articles to an information need. The framework, CQED, can have four different variations, depending upon the learning path adopted for training and re-ranking the candidate expansion terms.

Results: The model drastically improves the search performance, when compared to the original query. The performance improvement in comparison to the original query, in terms of RECALL@1000 is 190.85% and in terms of NDCG@1000 is 343.55%. Additionally, the model outperforms all existing state-of-the-art baselines. In terms of P@10, the model that has been optimized based on Precision outperforms all baselines (0.7987). On the other hand, in terms of NDCG@10 (0.7986), MAP (0.3450) and bpref (0.4900), the CQED model that has been optimized based on an average of all retrieval measures outperforms all the baselines.

Conclusion: The proposed model successfully expands queries posed to PubMed, and improves search performance, as compared to all existing baselines. A success/failure analysis shows that the model improved the search performance of each of the evaluated queries. Moreover, an ablation study depicted that if ranking of generated candidate terms is not conducted, the overall performance decreases. For future work, we would like to explore the application of the presented query expansion framework in conducting technology-assisted Systematic Literature Reviews (SLR).
