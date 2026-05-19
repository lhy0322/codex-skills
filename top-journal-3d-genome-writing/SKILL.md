---
name: top-journal-3d-genome-writing
description: Top-tier scientific manuscript and figure support for 3D genome, chromatin conformation, Hi-C/Micro-C, enhancer-promoter regulation, sequence-to-structure prediction, and computational genomics papers. Use when drafting, restructuring, polishing, reviewing, or planning Nature/Science/Cell/Nature Methods/Nature Genetics/Nature Biotechnology/Genome Biology/Genome Research/NAR-style papers, abstracts, titles, results sections, figure legends, graphical models, benchmark figures, response-to-reviewer materials, or publication-quality figure plans for 3D genome research.
---

# Top Journal 3D Genome Writing

Use this skill to turn 3D genome results into a high-standard manuscript and figure story. Favor precise claims, strong evidence chains, and publication-ready visual logic over generic "AI method" or "omics analysis" language.

## Quick Workflow

1. Identify the target journal tier, paper type, central claim, available results, and missing evidence. If the user has not provided them, infer cautiously and mark unknowns as `[VERIFY]`.
2. Choose the paper arc:
   - Method paper: bottleneck -> model/assay -> benchmark -> biological utility -> generalization -> availability.
   - Biological discovery: unresolved mechanism -> perturbation/data -> structural change -> regulatory consequence -> model.
   - Resource/atlas: scale -> quality control -> major patterns -> examples -> reuse.
   - Review/perspective: conceptual map -> field tension -> synthesis -> future tests.
3. Build an evidence ladder before writing: data quality, leakage-safe validation, baseline comparison, ablation, cross-context generalization, biological validation, reproducibility.
4. Plan figures before prose. Each Results section should earn one main figure or one clear extended-data support package.
5. Draft in high-level scientific English unless the user asks for Chinese prose. It is fine to reason with the user in Chinese.
6. Do not invent results, citations, methods, p-values, or dataset details. Use `[VERIFY]` placeholders for facts that need confirmation.

## Reference Loading

Load only what the task needs:

- For manuscript structure, titles, abstracts, introductions, results, and discussion: read `references/manuscript-architecture.md`.
- For main figures, panel design, figure legends, and graphical abstracts: read `references/figure-design.md`.
- For validation, reviewer-risk auditing, and 3D genome evidence requirements: read `references/evidence-checklist.md`.
- For patterns derived from the local 3D genome PDF corpus: read `references/corpus-notes.md`.

## Common Outputs

When the user asks for planning, return a compact plan with:

- one-sentence central claim;
- target journal fit and risk;
- main figure sequence;
- Results section headings;
- missing experiments or analyses.

When the user asks for writing, return polished manuscript prose plus a short note on assumptions and `[VERIFY]` items.

When the user asks for figures, return a figure-by-figure plan with panel labels, data inputs, plot type, visual encodings, expected takeaway, and caption skeleton.

When the user asks for review, lead with weaknesses that could block a top-tier paper: claim/evidence mismatch, leakage, weak baselines, missing orthogonal validation, unsupported mechanism, unclear figures, or overbroad language.

## Style Rules

- Make the first sentence of each paragraph carry the scientific point.
- Prefer concrete nouns: chromatin contact maps, loop extrusion, compartment switching, insulation score, enhancer-promoter pairing, variant effect, held-out chromosomes.
- Quantify whenever possible: resolution, cell types, chromosomes, loci, effect size, confidence interval, replicate count.
- Separate performance from discovery. A model outperforming baselines is not itself a biological advance.
- Avoid empty intensifiers: novel, powerful, comprehensive, robust, significant, state-of-the-art. Use them only when supported by specifics.
- Keep figure legends interpretive but not speculative: what was measured, how it was compared, what the panel shows, and what conclusion follows.

## Script

Use `scripts/extract_pdf_signals.py` to mine a local paper folder for reusable context:

```bash
python scripts/extract_pdf_signals.py "F:/path/to/papers" --out corpus_signals.json --markdown corpus_signals.md --limit 10
```

The script extracts section names, figure-caption starts, and claim-like sentences from PDFs. Use the output as orientation, not as text to copy.
