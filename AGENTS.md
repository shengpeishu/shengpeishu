# Agents

This repository holds two different jobs. Tell them apart before you edit.

The profile page is `README.md`. Leave it alone unless the task is the GitHub profile.

Accounting and auditing drafts use the writing system in `audit-writing/`. The style is a mixed-author corpus. Copy the moves. Do not copy findings, means, stimuli, cases, or bylines, and do not sign a draft with any name in the catalog.

## Before a draft or a revision

Follow `audit-writing/PROMPT.md` in order.

1. Read `audit-writing/dna/Writing-DNA.md`, `language-dna.md`, `structure-patterns.md`, `cognitive-framework.md`, and `visual-style-guide.md`.
2. Read `audit-writing/MEMORY.md` for venue, length, and citation defaults.
3. Select five papers. From `audit-writing/`:

   ```text
   python3 select_papers.py --type experiment --tag <needle>
   ```

   `article_type` is experiment, archival, field, or review. Repeat `--tag` for an OR match. More than five matches keeps the five most recent. Fewer than five fills from the same type. If that type has fewer than five papers, use the shorter list. Read those papers for cadence only.
4. If `raw/` is not mounted, select from `audit-writing/CATALOG.md`, say the full text was unavailable, and do not invent articles. The articles live with the project store copy of this system, not in this public repository.
5. Draft from the matching file in `audit-writing/templates/` when the piece is an experiment abstract, an introduction, a hypothesis block, or a method outline. Archival and review pieces use the matching section of `structure-patterns.md`.
6. Fill `audit-writing/CHECKLIST.md` in the reply, then give the prose.
7. In a second turn, clean listed AI tells. Where a tell-rule and the DNA conflict, the DNA wins.

Priority: the assignment, then the genre template, then language and visual rules, then the cognitive frames. A venue named in the assignment overrides citation punctuation. `MEMORY.md` holds the default when no venue is named.

## What not to commit

Do not add the twenty source articles, or a `raw/` directory of those articles, to this repository.
