---
title: A Semantic Approach to Post-Retrieval Query Performance Prediction
year: 2022
type: journal
authors: Parastoo Jafarzadeh Hesar, Faezeh Ensan
venue: Information Processing & Management, 59(1), 102746
doi: 10.1016/j.ipm.2021.102746
area: ir
tags:
- Query Performance
order: 19
---
The importance of query performance prediction has been widely acknowledged in the literature, especially for query expansion, refinement, and interpolating different retrieval approaches. This paper proposes a novel semantics-based query performance prediction approach based on estimating semantic similarities between queries and documents. We introduce three post-retrieval predictors, namely (1) semantic distinction, (2) semantic query drift, and (3) semantic cohesion based on (1) the semantic similarity of a query to the top-ranked documents compared to the whole collection, (2) the estimation of non-query related aspects of the retrieved documents using semantic measures, and (3) the semantic cohesion of the retrieved documents. We assume that queries and documents are modeled as sets of entities from a knowledge graph, e.g., DBPedia concepts, instead of bags of words. With this assumption, semantic similarities between two texts are measured based on the relatedness between entities, which are learned from the contextual information represented in the knowledge graph. We empirically illustrate these predictors' effectiveness, especially when term-based measures fail to quantify query performance prediction hypotheses correctly. We report our findings on the proposed predictors' performance and their interpolation on three standard collections, namely ClueWeb09-B, ClueWeb12-B, and Robust04. We show that the proposed predictors are effective across different datasets in terms of Pearson and Kendall correlation coefficients between the predicted performance and the average precision measured by relevance judgments.
