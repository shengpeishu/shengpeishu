# Project memory

Venue, length, and citation defaults for drafts in this system. Sentence shape still comes from the five DNA files. A line here wins on punctuation and length only when it names a venue or a count. Confirmed 2026-11-25 (Asia/Shanghai).

## Corpus on file

`raw/` has 20 articles and `_meta/` has 20 records, paired by filename.

| article_type | n |
| --- | ---: |
| experiment | 15 |
| archival | 3 |
| field | 1 |
| review | 1 |

`article_type` is the genre token in the filename (experiment, archival, field, review). `topic_tags` are the subject needles. Select with `select_papers.py`. Do not select on the old value `analysis`; that label was replaced because it could not separate an experiment from an archive.

Full text stays in `raw/` on the project store. It is not copied into the public repository. `catalog.json` and `CATALOG.md` are the metadata index.

## Length

These are the corpus rules. No personal override is on file. If an assignment gives a count, use that count.

| Piece | Rule |
| --- | --- |
| Abstract | 120–220 words. If the assignment gives no count, stay inside that band, near 160. Four moves, in order. At most one citation. Keywords are a semicolon list of constructs. No roadmap. |
| Sentence | Median about 22 words. Most sentences 18–33. One comparison sentence may reach about 45. |
| Paragraph | Four to eight sentences, about 160 words. The hypothesis is its own paragraph. Each numbered limitation is its own paragraph. |
| Introduction | Five paragraphs is typical. Do not open with "In this paper." |
| Heading | Numbered, one to six words. |

## Citation punctuation inside this corpus

These are the marks on the pages that were distilled. They are not a journal's current guide. When the assignment names a venue, follow that venue's current guide for punctuation only.

| Where it appeared | Mark | Example shape |
| --- | --- | --- |
| JAR papers from 1995–1999, and some later JAR sentences | Year in brackets. "and", not "&". | Libby and Trotman [1992] |
| AOS, 2000 | Parentheses, ampersand, comma before the year. | (Libby & Trotman, 1993) |
| CAR, 2007, and the AJPT review, 2005 | Parentheses, no comma before the year, "and", not "&". | (Petty and Cacioppo 1986); (Libby and Frederick 1990) |
| Later SSRN manuscripts in this set | Mixed. Both (Author Year) and (Author, Author, and Author [Year]) occur, sometimes in one literature. | Do not copy the mix. |

Placement does not change with the venue. The citation sits immediately after the claim. Two or three citations in a sentence is normal. A theory paragraph with none is not this corpus, unless the assignment supplied no sources. Then leave the claim uncited and say so. Do not invent a paper.

## Unnamed venue

If the assignment names no journal, use one mark for the whole draft and say which: parentheses, no comma before the year, "and" rather than "&", as in the CAR 2007 and AJPT 2005 pages. Do not mix in brackets or ampersands. Replace that default as soon as the venue is named.

## Voice defaults when the assignment is silent

- "We," not "I." Use "I" only if the assignment says the paper is single-authored.
- "Participants," not "subjects," in a new paper.
- "All p-values are two-tailed unless noted." Say that once, in a footnote, when there are tests. One-tailed only for a directional prediction, marked at the test.
- The closing reader is whoever the assignment names. If it names none, name the decision maker in the study (managers, auditors, investors, analysts) and stop. Do not add a regulator the design did not speak to.

## Overrides on file

None yet. Add a dated line when a journal guide or the user states a length, a citation mark, or a required section. Example of a line that belongs here: "2026-11-25: TAR submissions use the TAR style guide for citations; abstract stays 120–220 words."
