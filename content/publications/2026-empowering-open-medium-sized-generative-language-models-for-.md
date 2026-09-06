---
title: Empowering Open Medium-Sized Generative Language Models for Effective Structured Search in Biomedical Systematic Reviews
year: 2026
type: journal
authors: Leandra Budau, Richard Finney, Faezeh Ensan
venue: International Journal of Medical Informatics, 216
doi: 10.1016/j.ijmedinf.2026.106463
area: bio
tags:
- Biomedical IR
- LLMs
order: 2
---
Background: Systematic Literature Reviews (SLRs) are essential in biomedical research, particularly for informing public health policy and clinical decision-making. However, the manual generation of Boolean queries for literature searches is resource-intensive, prone to errors, and difficult to scale. Recent advances in large language models (LLMs) have demonstrated potential, yet most existing approaches rely on zero-shot prompting of commercial models, overlooking the cost-efficiency and domain adaptability of fine-tuned open-source alternatives.

Methods: This study proposes a novel, three-stage framework that employs medium-sized, open-source generative models, specifically BioGPT and BioT5, for automated Boolean query generation over PubMed. We develop and release datasets comprising PubMed article titles, MeSH terms, and keywords, and fine-tune the models using both title-only and title-plus-metadata prompts. We evaluate performance on two benchmark datasets: CLEF TAR and FASS-BSLR. Our experiments include comparisons with state-of-the-art baselines, prompt-based large language models, and ablation studies exploring the effects of training data size, metadata inclusion, and post-processing with PubMed's Automatic Term Mapping.

Results: Fine-tuned BioGPT outperforms both traditional TAR models and commercial LLMs across key retrieval metrics. On the CLEF TAR dataset, it achieves a Precision of 0.2544, F1 of 0.2392, MAP@1000 of 0.1424, and NDCG@1000 of 0.2490, which surpasses all baselines. On the FASS dataset, it reaches a Recall of 0.1801 and NDCG@1000 of 0.0900, again outperforming all competing models. While slightly behind BioGPT, BioT5 still outperforms most baselines. Notably, BioGPT's Recall of 0.1801 on FASS is more than twice that of PubMed-Title and PubMed-Keyword, and exceeds GPT-3.5 Turbo, GPT-4, Gemini-2, and Llama-3.

Conclusion: This work demonstrates that fine-tuned, open-source, medium-sized generative models can match or exceed the performance of much larger commercial LLMs in Boolean query generation for biomedical SLRs. These models offer a cost-effective, privacy-preserving, and scalable alternative for structured retrieval of biomedical scholarly texts.
