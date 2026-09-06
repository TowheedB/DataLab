---
title: Benchmarking Fully Automated Scholarly Search for Biomedical Systematic Literature Reviews
year: 2024
type: journal
authors: Leandra Budau, Faezeh Ensan
venue: IEEE Access, 12
doi: 10.1109/ACCESS.2024.3405529
area: bio
tags:
- Biomedical IR
order: 12
---
Biomedical Systematic Literature Reviews (SLRs) play a fundamental role in evidence-informed healthcare and can serve as actionable insights for researchers and policy-making organizations in the field. In this paper, we focus on the phase of 'study search' in conducting SLRs, i.e., the process of organising a comprehensive search via biomedical databases, such PubMed, in order to obtain all the relevant articles on a certain topic of interest. We introduce FASS-BSLR, a dataset and a benchmark suit to facilitate developing and evaluating fully automated techniques for study search. We also provide and analyze a set of basic methods along with a number of generative models, and report the experiment's results over the introduced dataset. We introduce a simple but effective model based on the resent transformer-based generative model, ChatGPT, for generating Boolean queries over PubMed. Through different experiments, we illustrate that this model is more effective than basic search models, than keyword search over PubMed, and than existing methods for crafting Boolean queries using ChatGPT. We show that the introduced model is even more effective than manual queries in terms of Precision, Recall, NDCG, and MAP in positions 10, and 100, but falls short of the recall that manual queries achieve at position 1000. We also report the retrieval performance of different models when a number of relevant articled have been provided as seed documents. We demonstrate that, when three documents are used as seed articles, the introduced model outperforms manual queries in all metrics except Recall@1000, on which its performance is comparable with the performance attained by manual queries.
