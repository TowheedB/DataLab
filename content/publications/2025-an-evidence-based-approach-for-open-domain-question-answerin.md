---
title: An Evidence-based Approach for Open Domain Question Answering
year: 2025
type: journal
authors: Parastoo Jafarzadeh, Faezeh Ensan
venue: Knowledge and Information Systems, 67, 1969–1991
doi: 10.1007/s10115-024-02269-2
area: ir
tags:
- QA
order: 7
---
Open-domain question answering (ODQA) stands at the forefront of advancing natural language understanding and information retrieval. Traditional ODQA systems, which predominantly utilize a two-step process of information retrieval followed by reading module, face significant challenges in aligning retrieved passages with the contextual nuances of user queries. This paper introduces a novel methodology that leverages a semi-structured knowledge graph to enhance both the accuracy and relevance of answers in ODQA systems. Our model employs a threefold approach: firstly, it extracts and ranks evidence from a textual knowledge graph, a semi-structured knowledge graph where the nodes are real-world entities and the edges are sentences that two entities co-occur in, based on the contextual relationships relevant to the question. Secondly, it utilizes this ranked evidence to re-rank initially retrieved passages, ensuring that they align more closely with the query's context. Thirdly, it integrates this evidence into a generative reading component to construct precise and context-rich answers. We compare our model, termed contextual evidence-based question answering (CEQA), against traditional and state-of-the-art ODQA systems across several datasets, including TriviaQA, Natural Questions, and SQuAD Open. Our extensive experiments and ablation studies show that CEQA significantly outperforms existing methods by improving both the relevance of retrieved passages and the accuracy of the generated answers, thereby establishing a new benchmark in ODQA.
