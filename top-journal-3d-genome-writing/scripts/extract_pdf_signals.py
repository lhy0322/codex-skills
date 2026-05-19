#!/usr/bin/env python3
"""Extract lightweight writing and figure signals from a folder of PDFs."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable

try:
    from pypdf import PdfReader
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Missing dependency: install pypdf or use Codex bundled Python.") from exc


SECTION_NAMES = (
    "Abstract",
    "Introduction",
    "Results",
    "Discussion",
    "Methods",
    "Data availability",
    "Code availability",
    "Acknowledgements",
)


def compact_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def pdf_text(path: Path, max_pages: int) -> tuple[int, str]:
    reader = PdfReader(str(path))
    page_texts: list[str] = []
    for page in reader.pages[:max_pages]:
        try:
            page_texts.append(page.extract_text() or "")
        except Exception:
            page_texts.append("")
    return len(reader.pages), "\n".join(page_texts)


def find_sections(text: str) -> list[str]:
    compact = compact_text(text)
    found = []
    for section in SECTION_NAMES:
        if re.search(r"\b" + re.escape(section) + r"\b", compact, re.IGNORECASE):
            found.append(section)
    return found


def find_figure_captions(text: str, max_captions: int) -> list[str]:
    compact = compact_text(text)
    captions: list[str] = []
    pattern = re.compile(
        r"(?:^|\s)(Fig(?:ure)?\.?\s*[1-9][\w-]*[\.:]\s*.{80,900})",
        re.IGNORECASE,
    )
    next_caption = re.compile(
        r"\s+(Fig(?:ure)?\.?\s*[2-9][\w-]*[\.:]|Extended Data Fig|Supplementary Fig|References|Methods)\s+",
        re.IGNORECASE,
    )
    for match in pattern.finditer(compact):
        caption = match.group(1).strip()
        caption = next_caption.split(caption)[0].strip()
        if len(caption) > 60 and caption not in captions:
            captions.append(caption)
        if len(captions) >= max_captions:
            break
    return captions


def find_claim_sentences(text: str, max_claims: int) -> list[str]:
    compact = compact_text(text)
    claims: list[str] = []
    claim_pattern = re.compile(
        r"\b(we (develop|present|show|demonstrate|find|reveal|introduce)|"
        r"our (model|method|framework|analysis)|enables|outperform|predict)\b",
        re.IGNORECASE,
    )
    for sentence in re.split(r"(?<=[.!?])\s+", compact):
        sentence = sentence.strip()
        if 80 <= len(sentence) <= 280 and claim_pattern.search(sentence):
            claims.append(sentence)
        if len(claims) >= max_claims:
            break
    return claims


def iter_pdfs(root: Path) -> Iterable[Path]:
    if root.is_file() and root.suffix.lower() == ".pdf":
        yield root
        return
    yield from sorted(root.rglob("*.pdf"))


def build_markdown(records: list[dict]) -> str:
    lines = ["# PDF Signal Summary", ""]
    lines.append(f"PDFs analyzed: {len(records)}")
    lines.append("")
    for record in records:
        lines.append(f"## {record['file']}")
        if "error" in record:
            lines.append(f"- Error: {record['error']}")
            lines.append("")
            continue
        lines.append(f"- Pages: {record['pages']}")
        lines.append(f"- Sections: {', '.join(record['sections']) or 'none detected'}")
        if record["claims"]:
            lines.append("- Claim-like sentences:")
            for claim in record["claims"]:
                lines.append(f"  - {claim}")
        if record["captions"]:
            lines.append("- Figure-caption starts:")
            for caption in record["captions"]:
                lines.append(f"  - {caption}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf_path", help="PDF file or directory containing PDFs.")
    parser.add_argument("--out", default="pdf_signals.json", help="Output JSON path.")
    parser.add_argument("--markdown", help="Optional Markdown summary path.")
    parser.add_argument("--max-pages", type=int, default=12, help="Pages to scan per PDF.")
    parser.add_argument("--max-captions", type=int, default=5, help="Captions to keep per PDF.")
    parser.add_argument("--max-claims", type=int, default=5, help="Claim-like sentences to keep per PDF.")
    parser.add_argument("--limit", type=int, help="Limit the number of PDFs for a quick scan.")
    args = parser.parse_args()

    root = Path(args.pdf_path)
    pdfs = list(iter_pdfs(root))
    if args.limit is not None:
        pdfs = pdfs[: args.limit]
    if not pdfs:
        raise SystemExit(f"No PDFs found: {root}")

    records: list[dict] = []
    for pdf in pdfs:
        try:
            pages, text = pdf_text(pdf, args.max_pages)
            records.append(
                {
                    "file": pdf.name,
                    "path": str(pdf),
                    "pages": pages,
                    "sections": find_sections(text),
                    "claims": find_claim_sentences(text, args.max_claims),
                    "captions": find_figure_captions(text, args.max_captions),
                }
            )
        except Exception as exc:
            records.append({"file": pdf.name, "path": str(pdf), "error": str(exc)})

    out_path = Path(args.out)
    out_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.markdown:
        Path(args.markdown).write_text(build_markdown(records), encoding="utf-8")

    print(f"Analyzed {len(records)} PDF(s). Wrote {out_path}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
