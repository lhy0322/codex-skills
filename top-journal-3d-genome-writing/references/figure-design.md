# Figure Design For 3D Genome Papers

## Main Principle

A top-journal figure is not a collection of plots. It is a visual argument. Each panel should either establish the system, validate the measurement/model, quantify an effect, or interpret a mechanism.

## Main Figure Blueprint

For each figure, define:

- Figure title as a claim, not a topic.
- Panel A as orientation: workflow, locus schematic, perturbation design, or model input-output.
- One representative example: contact map, genome browser track, loop pileup, or locus view.
- One population-level quantification: box/violin/dot plot, calibration curve, precision-recall, distance-stratified correlation, or aggregate score.
- One interpretation panel: regulatory model, variant effect, pathway consequence, or mechanism schematic.

Keep architecture details proportional. If the architecture is not the conceptual advance, move layers, hyperparameters, and training details to Extended Data.

## Contact Map Rules

- State assay, cell type, chromosome/locus, bin size, normalization, and color scale.
- Use identical genomic coordinates and color scales when comparing conditions.
- Show observed, predicted, target, and residual maps when evaluating models.
- Include distance-stratified metrics because nearby bins dominate raw correlations.
- Pair visual examples with aggregate analyses: APA for loops, insulation score for TADs, saddle plots for compartments, or pileups around anchors.
- Mark loops, boundaries, compartments, or viewpoints directly on maps when they are discussed in the text.

## Plot Types By Task

Hi-C or Micro-C enhancement:

- low-coverage input vs prediction vs high-coverage target;
- residual or error map;
- SCC/HiCRep, Pearson/Spearman by distance, SSIM, MSE, loop F1/AUPRC;
- downsampling curve;
- cross-cell-type and cross-chromosome generalization;
- loop/TAD/compartment recovery.

Sequence-to-3D prediction:

- sequence window and model overview;
- predicted vs measured contact maps at multiple genomic scales;
- motif or variant perturbation maps;
- saliency or contribution scores with careful uncertainty language;
- held-out chromosome/species/cell-type performance;
- examples connecting structural change to gene regulation.

Enhancer-promoter or target-gene prediction:

- candidate pair construction;
- score distribution and validation against independent assays;
- eQTL, CRISPR, expression, or ChIA-PET/HiChIP support;
- disease-locus case study;
- network or locus-level summary with clear target gene labels.

Single-cell or dynamic 3D genome:

- cell/time experimental design;
- embedding or trajectory with structural features, not only clusters;
- representative contact maps along pseudotime or condition;
- quantified loop, TAD, compartment, or contact changes;
- uncertainty or replicate consistency.

Mechanistic perturbation:

- perturbation design and quality controls;
- differential contact map;
- aggregate loop/stripe/TAD effects;
- transcription or chromatin-state consequence;
- concise model explaining causality and limits.

## Captions

Use this caption structure:

1. Panel subject: what each panel shows.
2. Data and comparison: assay, cell type, condition, genomic window, sample size, or split.
3. Statistical treatment: test, replicate definition, correction, and error bars.
4. Takeaway: the conclusion supported by the panel.

Do not hide critical methods only in captions. Do not let captions become miniature Methods sections.

## Visual Style

- Use colorblind-safe palettes; avoid red-green dependence.
- Use one accent color per condition and reserve strong colors for focal comparisons.
- Keep labels short but complete: assay, resolution, condition, metric.
- Use vector output for diagrams and text; use high-resolution raster for heatmaps.
- Align panel widths and scales; inconsistent axes undermine trust.
- Avoid decorative graphics. In 3D genome papers, real contact maps, tracks, loci, and perturbation schematics carry the authority.

## Figure Audit

Before finalizing, ask:

- Can a reader understand the claim by reading only the figure title and panel labels?
- Does every representative locus have a cohort-level quantification?
- Are color scales and genomic windows comparable?
- Are baselines and negative controls visible?
- Are model outputs visually distinguished from measurements?
- Are limitations or failure modes moved somewhere credible, such as Extended Data?
