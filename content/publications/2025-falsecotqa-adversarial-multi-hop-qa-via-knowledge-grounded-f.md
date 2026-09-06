---
title: 'FalseCoTQA: Adversarial Multi-Hop QA via Knowledge-Grounded False Chains of Thought'
year: 2025
type: conference
authors: Julien Serbanescu, Mahdiyar Ali Akbar Alavi, Faezeh Ensan, Fattane Zarrinkalam
venue: ACM SIGIR-AP 2025, Xi'an, China
doi: 10.1145/3767695.3769494
area: kg
tags:
- QA
- Knowledge Graphs
order: 8
---
Multi-hop question answering (QA) models excel at decomposing complex queries into sequential reasoning steps, yet they remain vulnerable to subtly flawed inference chains that appear reasonable but are factually incorrect. To quantify and address this weakness, we present FalseCoTQA, an adversarial benchmark that injects knowledge-grounded false reasoning into retrieval-augmented contexts. Unlike prior methods that merely tweak surface text, FalseCoTQA leverages a domain-agnostic knowledge graph to systematically replace entities to construct semantically coherent yet incorrect chains of thought on top of standard multi-hop datasets (HotpotQA and MuSiQue). By evaluating state-of-the-art language models on this benchmark, we observe dramatic drops in answer accuracy, highlighting their tendency to follow deceptive reasoning without verifying factual consistency. We expect the proposed benchmark to contribute to the evaluation and improvement of the robustness and reliability of language models in multi-hop question answering.
