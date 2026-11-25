# Master prompt

Use this for every draft or revision. Paste it into Grok or another chat, or follow it inside Cursor. The five DNA files and this prompt have to be in the same turn. A memory of them is not enough.

```text
Read these five files before you write, in this order. They sit next to
this prompt, or in dna/ beside it:

1. Writing-DNA.md
2. language-dna.md
3. structure-patterns.md
4. cognitive-framework.md
5. visual-style-guide.md

Then select five raw papers. Run:

  python3 select_papers.py --type <experiment|archival|field|review> --tag <needle>

Repeat --tag for each needle. Tags are OR. article_type is required.
If more than five match, the script keeps the five most recent.
If fewer than five match, it fills from the same article_type.
If that type has fewer than five papers, use the shorter list and say so.
Read those five papers for cadence only: sentence length, how a paragraph
turns, and where a short sentence is allowed. State that cadence in a few
lines before the draft. Do not import their findings, means, stimuli, cases,
or bylines.

If raw/ is not mounted, use catalog.json or CATALOG.md for the same
selection, say that the full text was unavailable, and draft from the five
DNA files and the matching template. Do not invent stand-in articles.

Priority if rules conflict:
1. The assignment in this message (genre, length, venue, what to keep).
2. The structure template for this genre (templates/ if it exists;
   otherwise the matching section of structure-patterns.md).
3. language-dna.md and visual-style-guide.md.
4. cognitive-framework.md (stance and what may be claimed, not sentence shape).

Venue punctuation overrides the corpus. Read MEMORY.md before you choose
a citation style. If this message names no venue, use the unnamed-venue
default in MEMORY.md and say that you did.

This is a mixed-author corpus. Copy the moves. Do not sign any author
from the catalog. Write "when," not "in general." First person plural
unless the assignment says the paper is single-authored. Median sentence
about 22 words. Most sentences 18–33. One sentence may reach about 45
words if it holds one comparison. A sentence under 12 words is allowed
after a long one, to name a design fact or to hand off. Do not stack
short sentences. Do not write three long sentences in a row.

Then draft. Fill CHECKLIST.md in the reply, then give the prose.
Keep every claim I supplied. Do not add citations, means, participants,
or mechanisms I did not supply. If a mechanism has no citation, leave it
uncited and mark that on the checklist.

After the draft, in a second turn, apply lieflat-less-ai-tone. Read
language-dna.md first. Where a tell-rule and the DNA conflict, the DNA
wins. Change only listed tells. Do not add facts.

Assignment:
Genre:
Venue (or "unnamed"):
Length:
Task:
```
