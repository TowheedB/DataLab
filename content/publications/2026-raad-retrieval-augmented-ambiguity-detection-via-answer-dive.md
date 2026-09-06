---
title: 'RAAD: Retrieval-Augmented Ambiguity Detection via Answer Diversity'
year: 2026
type: conference
authors: Parth Patel, Sarah Kamoun, Bita Azad, Faezeh Ensan
venue: ACM ICTIR 2026
doi: 10.1145/3805713.3820422
area: rai
tags:
- QA
- Uncertainty
order: 3
---
Large language models (LLMs) often respond confidently to ambiguous questions by implicitly committing to a single interpretation, which can yield misleading answers when multiple meanings are plausible. We propose RAAD (Retrieval-Augmented Ambiguity Detection), a lightweight framework that detects question ambiguity by identifying semantically incompatible answers grounded in retrieved evidence. RAAD retrieves diverse contexts, extracts candidate answers, and detects ambiguity by measuring semantic incompatibility among answer pairs using a cross-encoder. In RAAD, retrieval and answer diversity act as complementary pillars: retrieval exposes multiple plausible "world states" in which the question can be answered, while cross-encoder scoring determines whether the resulting answers remain interchangeable or diverge semantically. We evaluate RAAD on AmbigQA, ASQA, CAmbigNQ, and SituatedQA (Geo/Temp) and show that when trained with gold supervision on AmbigQA and evaluated on noisy, realistic retrieved answers, RAAD generalizes strongly across datasets, outperforming reported baselines on multiple benchmarks.
