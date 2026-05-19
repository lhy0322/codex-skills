# Local 3D Genome Corpus Notes

These notes summarize reusable patterns observed from the user's local folder of 52 PDFs on 3D genome research. Use them as style and structure guidance, not as source text to copy.

## Corpus Shape

The folder spans 2018-2026 and includes papers or preprints associated with Nature, Science, Nature Methods, Nature Genetics, Nature Biotechnology, Nature Communications, Genome Biology, Genome Research, NAR, Bioinformatics, PLOS Computational Biology, BIB, bioRxiv, and arXiv.

Major clusters:

- Hi-C or Micro-C resolution enhancement and denoising: HiCPlus, DeepHiC, EnHiC, HiCARN, iEnhance, DFHiC, HiCBridge, HiCDiffusion, Hic2MicroC.
- Sequence-to-3D genome prediction: Akita, DeepC, Orca, Origami, AkitaV2, ChromaFold, CTG.
- Enhancer-promoter and gene regulation prediction: DeepTACT, EPCOT, EPInformer, L2G, ChIPr.
- Mechanism and perturbation: cohesin, CTCF, loop extrusion, caRNAs, ecDNA, differentiation.
- Single-cell, temporal, or multi-condition modeling: scGrapHiC, scCARE-seq, HiC4D, TwinC.
- Reviews and field syntheses on deep learning for 3D chromatin.

## Reusable Top-Journal Pattern

Strong papers in this space usually do more than present a model. They connect model performance to a biological or methodological capability that was previously inaccessible.

Common narrative ladder:

1. A 3D genome measurement is central but limited by cost, sparsity, cell number, resolution, perturbation feasibility, or interpretability.
2. A model, assay, or framework is introduced to solve a sharply defined limitation.
3. Validation is performed on leakage-resistant splits such as held-out chromosomes, cell types, loci, species, perturbations, or assays.
4. The method recovers known structures: compartments, TADs, loops, stripes, enhancer-promoter contacts, insulation boundaries, or aggregate peak signals.
5. The method enables a new analysis: sequence perturbation, variant interpretation, time-course forecasting, target gene assignment, or mechanism testing.
6. The paper ends with a biological insight, not only a benchmark table.

## Figure Rhythm Seen Across the Corpus

Typical main-figure sequence:

- Figure 1: Conceptual problem and workflow. Include data inputs, model/assay structure, prediction target, and output interpretation.
- Figure 2: Primary validation against measured contact maps or independent assays. Include examples plus quantitative summaries.
- Figure 3: Generalization and ablation. Held-out contexts, downsampling, cross-cell or cross-assay tests, model components.
- Figure 4: Biological feature recovery. Loops, TADs, compartments, enhancer-promoter pairs, gene expression, disease loci.
- Figure 5: Perturbation or mechanistic insight. Cohesin/CTCF disruption, motif edits, variant effects, differentiation dynamics.
- Figure 6 or Extended Data: Resource, software, runtime, additional cell types, failure cases, and robustness.

For top-tier venues, push routine benchmark and architecture details into Extended Data when the main story is biological. For methods venues, keep architecture and benchmark evidence prominent but still show biological utility.

## Writing Signals

Effective abstracts and Results openings tend to:

- define the biological or technical bottleneck in one sentence;
- state the named method or experimental strategy only after the problem is clear;
- specify the data modality and prediction target;
- include the strongest quantitative or cross-context validation;
- close with what the approach reveals or enables.

Weak signals to avoid:

- claiming "captures 3D genome organization" without naming which features and at what scale;
- reporting only image-similarity metrics for contact maps;
- using random train/test splits that leak neighboring genomic bins;
- treating enhancer-promoter prediction as solved without orthogonal validation;
- showing visually pleasing heatmaps without distance-stratified quantitative support;
- calling a method interpretable while providing only saliency screenshots.

## Venue Sensibility

Nature, Science, and Cell require a broad biological claim or mechanism. A computational model alone rarely carries the paper unless it unlocks a major biological result.

Nature Methods, Nature Biotechnology, and Genome Biology can foreground a method, but the method still needs convincing generalization, practical availability, and a demonstration that changes what users can do.

Genome Research, NAR, Bioinformatics, PLOS Computational Biology, and BIB can support deeper computational detail, benchmark rigor, and field synthesis, but the manuscript still needs a crisp biological motivation.
