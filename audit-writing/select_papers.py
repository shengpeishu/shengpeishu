#!/usr/bin/env python3
"""Pick five corpus papers before a draft.

Match on article_type and topic_tags. If more than five match, keep the
five most recent. If fewer than five match, fill with the most recent
papers of the same article_type. Full text is read from raw/ when the
corpus is mounted. catalog.json is metadata only.

Examples:
  python3 select_papers.py --type experiment --tag managers --tag earnings
  python3 select_papers.py --type archival --tag audit-quality
  python3 select_papers.py --write-catalog
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

STORE = Path(
    "/cursor/stores/bc-9e0b7196-c6a4-4919-8ab2-808ee1529814/docs/audit-writing-dna"
)
TYPES = ("experiment", "archival", "field", "review")


def script_dir() -> Path:
    return Path(__file__).resolve().parent


def find_corpus(explicit: str | None) -> tuple[Path | None, Path]:
    """Return (corpus_or_none, catalog_json_path)."""
    here = script_dir()
    catalog = here / "catalog.json"
    if explicit:
        return Path(explicit).resolve(), catalog
    if (here / "_meta").is_dir():
        return here, catalog
    if (STORE / "_meta").is_dir():
        return STORE, catalog
    return None, catalog


def load_records(corpus: Path | None, catalog: Path) -> tuple[list[dict], str]:
    if corpus is not None and (corpus / "_meta").is_dir():
        records = []
        for path in sorted((corpus / "_meta").glob("*.json")):
            data = json.loads(path.read_text())
            stem = path.name[: -len(".json")]
            raw = corpus / "raw" / f"{stem}.md"
            data["_stem"] = stem
            data["_raw"] = str(raw) if raw.is_file() else ""
            records.append(data)
        if records:
            return records, "meta"
    if catalog.is_file():
        records = json.loads(catalog.read_text())
        for data in records:
            data.setdefault("_raw", "")
            data.setdefault("_stem", data.get("stem", ""))
        return records, "catalog"
    raise SystemExit(
        "No _meta/ directory and no catalog.json. Mount the corpus or pass --corpus."
    )


def blob(record: dict) -> str:
    tags = " ".join(record.get("topic_tags") or [])
    return " ".join(
        [
            record.get("title") or "",
            tags,
            record.get("notable") or "",
            record.get("_stem") or "",
        ]
    ).lower()


def select(records: list[dict], article_type: str, tags: list[str]) -> list[tuple[dict, str]]:
    pool = [r for r in records if r.get("article_type") == article_type]
    pool.sort(key=lambda r: r.get("date") or "", reverse=True)
    if not pool:
        raise SystemExit(f"No papers with article_type={article_type}.")
    needles = [t.lower() for t in tags if t.strip()]
    if needles:
        matched = [r for r in pool if any(n in blob(r) for n in needles)]
    else:
        matched = list(pool)
    matched.sort(key=lambda r: r.get("date") or "", reverse=True)
    chosen: list[tuple[dict, str]] = []
    seen = set()
    for record in matched[:5]:
        chosen.append((record, "match"))
        seen.add(record.get("_stem"))
    if len(chosen) < 5:
        for record in pool:
            if record.get("_stem") in seen:
                continue
            chosen.append((record, "fill"))
            seen.add(record.get("_stem"))
            if len(chosen) == 5:
                break
    return chosen


def write_catalog(records: list[dict], catalog: Path) -> None:
    public = []
    for record in sorted(records, key=lambda r: r.get("date") or ""):
        public.append(
            {
                "stem": record.get("_stem"),
                "title": record.get("title"),
                "date": record.get("date"),
                "author": record.get("author"),
                "column": record.get("column"),
                "article_type": record.get("article_type"),
                "topic_tags": record.get("topic_tags"),
                "word_count": record.get("word_count"),
            }
        )
    catalog.write_text(json.dumps(public, indent=2, ensure_ascii=False) + "\n")
    lines = [
        "# Corpus catalog",
        "",
        "Metadata for selecting five papers. This file does not contain the articles.",
        "Full text, when mounted, is in `raw/` beside `_meta/`. Do not copy findings,",
        "means, stimuli, or bylines into a draft.",
        "",
        "| Date | Type | Tags | Title |",
        "| --- | --- | --- | --- |",
    ]
    for record in public:
        tags = ", ".join(record.get("topic_tags") or [])
        title = (record.get("title") or "").replace("|", "/")
        lines.append(
            f"| {record.get('date')} | {record.get('article_type')} | {tags} | {title} |"
        )
    lines.append("")
    catalog.with_name("CATALOG.md").write_text("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser(description="Select five corpus papers for a draft.")
    parser.add_argument("--corpus", help="Directory that contains _meta/ and raw/.")
    parser.add_argument("--type", choices=TYPES, help="article_type to match.")
    parser.add_argument(
        "--tag",
        action="append",
        default=[],
        help="Topic needle. Repeat for OR matching against tags, title, and notes.",
    )
    parser.add_argument(
        "--write-catalog",
        action="store_true",
        help="Write catalog.json and CATALOG.md from _meta/.",
    )
    args = parser.parse_args()
    corpus, catalog = find_corpus(args.corpus)
    records, source = load_records(corpus, catalog)
    if args.write_catalog:
        if source != "meta":
            raise SystemExit("--write-catalog needs the _meta/ directory.")
        write_catalog(records, catalog)
        print(f"Wrote {catalog} and {catalog.with_name('CATALOG.md')} ({len(records)} papers).")
        if not args.type:
            return
    if not args.type:
        raise SystemExit("Pass --type, or pass --write-catalog.")
    chosen = select(records, args.type, args.tag)
    print(f"source: {source}")
    print(f"type: {args.type}")
    print(f"tags: {', '.join(args.tag) if args.tag else '(none; five most recent of this type)'}")
    print(f"count: {len(chosen)}")
    if len(chosen) < 5:
        print(
            "note: this article_type has fewer than five papers in the catalog. "
            "Use this shorter list. Do not invent papers to fill it."
        )
    for index, (record, reason) in enumerate(chosen, start=1):
        tags = ", ".join(record.get("topic_tags") or [])
        print(f"{index}. [{reason}] {record.get('date')} {record.get('article_type')}")
        print(f"   title: {record.get('title')}")
        print(f"   tags: {tags}")
        raw = record.get("_raw") or ""
        print(f"   raw: {raw or '(full text not mounted; use catalog metadata only)'}")


if __name__ == "__main__":
    main()
