# Evidence Checklist

Use this checklist when planning, reviewing, or strengthening a 3D genome manuscript for a top journal.

## Data And Assay

- Specify assay: Hi-C, Micro-C, Capture Hi-C, promoter-capture Hi-C, HiChIP, ChIA-PET, SPRITE, single-cell Hi-C, imaging, RNA-seq, ATAC-seq, ChIP-seq, CRISPR, or perturbation data.
- Report cell type, species, genome build, replicate count, resolution, sequencing depth, normalization, filtering, and quality controls.
- Show replicate concordance and library complexity when the claim depends on contact-map quality.
- Distinguish training data, validation data, held-out test data, and independent biological validation.

## Leakage-Safe Validation

Avoid validation designs that let nearby genomic bins, homologous loci, or the same cell type leak into both training and test.

Prefer:

- held-out chromosomes;
- held-out cell types or tissues;
- held-out loci or genes;
- held-out perturbation conditions;
- held-out species when claiming cross-species generality;
- independent assays for the same regulatory claim.

For sequence models, audit reverse complements, overlapping windows, nearby bins, and duplicated genomic regions.

## Metrics

Use metrics that match the claim:

- contact-map similarity: SCC/HiCRep, GenomeDISCO, Pearson/Spearman by genomic distance, MSE, MAE, SSIM;
- loop recovery: precision-recall, AUPRC, F1, APA score, anchor-level enrichment;
- TAD/boundary recovery: insulation score, boundary overlap, directionality index;
- compartment recovery: PC1 concordance, saddle strength, A/B switching;
- regulatory prediction: AUROC/AUPRC, calibration, enrichment in eQTL/CRISPR/ChIA-PET/HiChIP/PCHi-C, expression association;
- perturbation effects: differential contact strength, effect size, replicate consistency, dose or time response.

Do not rely on a single global correlation for contact maps. It can be dominated by genomic distance and coverage.

## Baselines And Ablations

Include:

- simple baselines: genomic distance, coverage, interpolation, sequence-only, epigenome-only, random forest/logistic regression when appropriate;
- prior methods that address the same task;
- ablations for key model components, data modalities, loss terms, and resolution levels;
- runtime, memory, input requirements, and practical failure modes.

Ablations should test claims, not merely remove arbitrary layers.

## Biological Validation

Top-tier claims need orthogonal support:

- known CTCF/cohesin orientation or loop anchors;
- TAD and compartment consistency;
- enhancer-promoter contact support from capture assays;
- gene expression or nascent transcription changes;
- eQTL, GWAS, variant, or CRISPR evidence;
- perturbation experiments such as CTCF motif editing, cohesin depletion, degron systems, enhancer deletion, or RNA perturbation;
- imaging or independent 3D genome assays when feasible.

Use cautious verbs for model-only results. A predicted contact nominates a mechanism; it does not prove one.

## Reviewer Risk Register

High-risk issues:

- central claim is broader than data scope;
- model is benchmarked only on random splits;
- improvement is visual but not statistically or biologically quantified;
- comparison lacks strong current baselines;
- contact-map metrics ignore genomic distance;
- downstream biological examples are cherry-picked;
- interpretability is asserted without perturbation or validation;
- no code, data, trained model, or reproducible pipeline;
- figure panels do not distinguish measured data from predictions;
- method cannot be used by other labs.

When revising a manuscript, convert each risk into either an analysis, a limitation sentence, or a narrowed claim.

## Response To Reviewers

For reviewer responses:

- answer the scientific concern before describing edits;
- cite the new figure or table;
- state whether the claim was strengthened, narrowed, or moved to Discussion;
- avoid defensive language;
- add quantitative evidence whenever a reviewer questions visual interpretation.
