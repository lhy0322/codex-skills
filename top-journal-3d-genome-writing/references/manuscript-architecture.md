# Manuscript Architecture

## Decide The Paper Type

Classify the manuscript before editing:

- Method: The contribution is a model, algorithm, assay, or framework.
- Discovery: The contribution is a biological mechanism or regulatory principle.
- Resource: The contribution is a dataset, atlas, benchmark, or software resource.
- Review: The contribution is synthesis and field positioning.

For top journals, combine types deliberately. A method paper should end in discovery or utility. A discovery paper should show method reliability without letting technical detail dominate the main text.

## Central Claim

Write one central claim before drafting:

`[Approach] reveals/enables [specific 3D genome capability] across [scope] and shows [biological or practical consequence].`

Examples of claim slots:

- capability: predict Micro-C-scale contacts from sequence, recover enhancer-promoter contacts from sparse Hi-C, infer variant effects on loops, forecast chromatin reorganization during differentiation;
- scope: held-out chromosomes, unseen cell types, disease loci, perturbation conditions, developmental stages;
- consequence: target gene assignment, mechanism of loop loss, regulatory rewiring, improved experimental prioritization.

## Title

Use a title that exposes the object of study and the advance.

Strong title patterns:

- `Sequence-based prediction of [3D genome feature] enables [biological use]`
- `[Method name] maps/predicts/reveals [specific contact or regulatory feature]`
- `[Perturbation/process] reshapes [3D genome structure] to control [function]`

Avoid titles that only say "a deep learning framework for 3D genome analysis" unless the target venue is technical and the method name is already the brand.

## Abstract

Use five moves:

1. Field problem: why 3D genome measurement or interpretation remains limited.
2. Gap: what current assays or models cannot resolve.
3. Approach: method/assay/data and prediction target.
4. Evidence: strongest validation, generalization, or perturbation result.
5. Consequence: biological insight, practical use, or resource value.

Keep the abstract claim-bounded. If the method was tested in two cell types, do not imply universal mammalian generality.

## Introduction

A strong Introduction can use four paragraphs:

1. Biological stakes: 3D genome organization links sequence, chromatin state, gene regulation, and disease.
2. Technical gap: Hi-C/Micro-C/contact assays or computational models face sparsity, cost, resolution, cell specificity, interpretability, or perturbation limits.
3. Field limitation: existing tools recover part of the problem but fail on scale, generalization, mechanism, or validation.
4. This study: what was built or discovered and what evidence supports it.

Do not turn the Introduction into a literature catalog. Every cited limitation should point toward the study's central claim.

## Results

Each Results section should answer one question:

- What was unknown or impossible before this section?
- What did the authors do?
- What is the key result?
- Why does it matter for the next section?

Useful section sequence for method papers:

1. Overview of the model, data, and prediction task.
2. Benchmark against measured maps and prior methods.
3. Generalization to held-out contexts.
4. Recovery of biological structures.
5. Perturbation, interpretation, or downstream discovery.
6. Resource/software and practical guidance.

Useful section sequence for biological discovery papers:

1. Observation or perturbation reveals a structural phenomenon.
2. Quantification across replicates, loci, or conditions.
3. Mechanistic factor or sequence feature is identified.
4. Functional consequence is linked to transcription, variants, or phenotype.
5. Model reconciles the evidence and makes a testable prediction.

## Discussion

Do not simply repeat Results. Use the Discussion to:

- state the conceptual advance;
- distinguish what is proven from what is inferred;
- explain why the result changes 3D genome interpretation or experimental design;
- name limitations honestly: resolution, cell-type coverage, assay bias, training data, perturbation scope, or causality;
- propose the next decisive experiment or application.

## Language Edits

Replace vague claims:

- "Our method performs well" -> "The model improved [metric] on held-out chromosomes and preserved [loop/TAD/compartment feature]."
- "This reveals regulatory mechanisms" -> "These predictions nominate [enhancer/promoter/variant] contacts that align with [expression/eQTL/CRISPR] evidence."
- "The framework is general" -> "The framework transferred from [source] to [target] without retraining/after fine-tuning, with [metric] change."

Keep the strongest verb for the strongest evidence:

- "show" for direct measurement;
- "suggest" for convergent but indirect evidence;
- "predict" for model output;
- "nominate" for candidate regulatory elements;
- "support" for consistency with prior knowledge.
