# Language DNA

> L1 surface-language analysis of a mixed-author corpus. These 20 papers are not one person's style. The patterns below are what survives across journal experiments, three archival papers, one field study, and one review. Paper-specific nouns (jargon, CSR, fair value, busy season) are topic vocabulary. Do not import them into a new paper.

## How the counts were made

There is no upstream statistics script. Counts were taken from the Markdown after dropping image dumps, SSRN and JSTOR boilerplate, and page furniture, and after rejoining hard-wrapped lines. Sentences were split with NLTK's English tokenizer and kept only when they had at least five alphabetic words and were not mostly numbers.

The core sample is 8,658 sentences and 222,181 words. Two cuts failed often enough to matter. On several SSRN files the references and appendices are not a short heading, so some bibliography lines and variable lists entered the sample. Table rows sometimes survived as one very long "sentence" (maximum 795 words, a variable-definition block). That inflates both the short-sentence share and the mean. The median is the number to write to. Rates for "we find," "however," and "consistent with" are safer, because those phrases are rare in reference lists.

Rendered journal and SSRN pages were used as a check on rhythm. They agree with the median and disagree with the tails.

## Recurring Vocabulary

### Voice markers, not topic nouns

Rates are per 1,000 words of the core sample.

| Marker | Per 1,000 words | What it does |
| --- | ---: | --- |
| we | 8.8 | Default authorial subject. Sentence-initial "We" is 3.2 per 1,000 words. |
| our | 5.1 | "Our results," "our participants," "our theory." |
| also | 2.5 | The additive connective. A second result, a second design feature, a second proxy. |
| may | 1.5 | Hedge on a mechanism, not on a result you already tested. |
| likely | 1.5 | Prediction language: "more likely to." The trigram "more likely to" occurs 129 times. |
| significant / significantly | 2.1 | Tied to a test. Never a loose intensifier. |
| respectively | 0.6 | Pairs two numbers with two conditions, in that order. |
| however | 0.8 | Sentence-initial contrast. 170 hits. |
| consistent with | 0.9 | Links a result back to a named theory or a prior paper. 193 hits. |
| we find | 0.8 | The result move. "we find that" as a trigram: 119. |
| specifically | 0.5 | Narrows the claim you just made. |
| thus / therefore | 0.5 / 0.3 | Closes a derivation. "Thus" is the more common of the two. |
| prior research / prior studies | 0.6 | The thing this paper bounds. |
| for example | 0.3 | Introduces one stimulus sentence or one standard, then stops. |
| e.g. / i.e. | 1.2 / 0.8 | Inside parentheses. "e.g." for an instance, "i.e." for a restatement. |
| suggest / suggests | high among verbs | Theory and interpretation. Results "show" or "find"; theory "suggests." |

Verbs that carry the voice, in descending order of the tagged sample: find, provide, make, suggest, examine, indicate, assess, expect, show, test, consider. "Associated" belongs to the archival papers. Do not write "associated with" in an experiment unless you are citing an archival result.

"Participants" (870) is the later word. "Subjects" (319) is the earlier word, still normal in the 1995–2000 papers. In a new paper, pick one and keep it. "Auditors," "investors," "managers," and "analysts" name the decision maker. Do not call them "users" or "stakeholders" unless the sentence is about a standard.

### Topic nouns to leave behind

The hundred most frequent common nouns are dominated by whatever a long paper was about: audit, performance, auditors, participants, investors, earnings, risk, condition, disclosure, jargon, effect, firm, results, knowledge, management. Jargon, CSR, readability, fair value, and inspection risk are single-paper spikes. A new paper on a different question should not sound like it.

Stable nouns that do travel: effect, effects, results, evidence, condition, conditions, information, judgments, research, study, task. "The effect of" (172) and "the effects of" (146) are the corpus's favorite noun phrase. Titles use them. So do hypotheses.

### Adjectives that do work

positive / negative, higher / lower, high / low, significant, consistent, prior, greater, different. "One-tailed" is a method adjective, not a flourish. "Good" and "bad" appear as technical labels in the jargon paper ("good jargon," "bad jargon"), not as praise.

### What the lexicon refuses

No exclamation in the body. One title uses one ("You Have Been Forewarned!"). No "very" as a habit (it is not in the top adverbs). No "importantly" as a paragraph opener (the word is rare). No "delve," "landscape," "robust" as a compliment, or "it is important to note." "Robust" does appear, and when it does it means a sensitivity test in an archival paper.

## Sentence and Paragraph Patterns

| Measure | Value | How to use it |
| --- | --- | --- |
| Median length | 22 words | The target. |
| Mean length | 25.7 words | Pulled up by table run-ons. Do not chase the mean. |
| Interquartile range | 13 to 33 words | Write most sentences inside 18–33. |
| 90th percentile | 45 words | A hypothesis or a result-plus-statistic sentence may go here. |
| Share at or under 12 words | 23% measured | Inflated by reference fragments and headings. Real short sentences exist; they are not the rhythm. |
| Share at or over 35 words | 22% measured | Inflated by tables. On the page, roughly one sentence in five is legitimately long. |
| Share at or over 50 words | 7% | Almost always a hypothesis, a regression "where" clause, or a table. Do not write three of these in a row. |
| Paragraph median | 5 sentences, about 160 words | From 765 detected paragraphs. Means are higher because some PDF conversions never marked a paragraph break. |

Per-paper medians sit between 19 and 27 words. The 2007 materiality paper and the internal-control paper run longer (medians 27.5 and 25). The 1995 memory paper runs shorter (median 20) and is the only paper that says "I."

The rendered pages show the actual breath. A theory paragraph is four to eight sentences. The first states the causal claim. The middle sentences carry the citations and the boundary. The last sentence says what that implies for this setting. Then a short sentence is allowed: "This discussion suggests the following hypothesis." The hypothesis itself is its own paragraph.

Short sentences that are real, and worth copying, do one job:

- Name the design. "A 2×2 factorial design was used."
- Land a limitation. "Lastly, our participants are Canadians."
- Hand off to the hypothesis. "Hence, we predict that:"

They follow a long sentence. They are not stacked. Three short sentences in a row is not this corpus.

Long sentences earn their length by holding a comparison inside one grammatical frame: "more X when A than when B, and this difference is larger when C." They do not earn it by chaining "and" onto a new idea. If the sentence grows a second claim, start a new sentence with "We also find" or "In contrast."

### Moves, in the order a section uses them

1. Gap. "Prior research indicates that [established result]. We extend this research by showing that the result is conditional on [moderator]."
2. Prediction. "We predict that..." or "This suggests that..." Then the labeled hypothesis, with no statistic in it.
3. Result. "We find that..." or "Our results show..." Then the pattern in words, then the numbers in parentheses.
4. Alignment. "Consistent with [theory or paper], ..." Use this only when you can name what the result is consistent with.
5. Contrast. "However," or "In contrast," at the start of the sentence. "Although" is less common and usually sits inside the sentence.
6. Narrowing. "Specifically," when the next sentence is a simple effect, a proxy, or a stimulus example.
7. Addition. "We also ..." for the second dependent variable or the second experiment. This is the corpus's ordinary way to add, which is why "also" is the top adverb.
8. Close of a derivation. "Thus," or "Taken together," sparingly. "Taken together" is real but uncommon. Do not make it the default last line.

Hypothesis form, taken from the papers rather than from the frequency table:

> Hypothesis 1. Without risk materialization, the presence versus absence of risk management disclosures will have a positive effect on investors' stock valuations. This effect is more positive when the corresponding risk disclosure is made with a positive versus negative tone.

The label is "Hypothesis 1." or "H1." The sentence names both factors, uses "more," "less," "greater," or "only when," and does not contain a p-value. If the interaction needs a second sentence, give it a second sentence. Do not bury the interaction in a subordinate clause after a main effect.

Result form:

> We find that participants are more likely to forgo an economically desirable hedge when both the economic impact and the fair value accounting impact are presented than when only the economic impact is presented.

Then the test, in parentheses or the next sentence: means, the contrast or F, and whether the p-value is one-tailed. "Respectively" pairs the means with the conditions already named, in the same order.

Roadmap sentence, near the end of the introduction, one sentence, not a menu:

> The rest of the paper is organized as follows. The next section develops the hypotheses to be tested, while the third section discusses the research method.

Limitation form:

> The following limitations of this study should be noted. First, ... Second, ...

Each limitation is one or two sentences and ends by saying what future research would vary. It does not apologize.

### Person

"We" examines, predicts, finds, uses, conducts, and contributes. "We" is the voice in 19 of the 20 papers, including single-experiment papers with two authors and archival papers. The 1995 memory paper is the exception: it is single-authored and says "I investigate," "I also assess," "I examined." Copy "I" only when the new piece is genuinely single-authored. Do not mix "I" and "we" in one paper.

"This paper" and "this study" both appear, at low rates (about 0.2 per 1,000 words each). "In this paper, we investigate" is the ordinary opening of the second or third paragraph, not of the first sentence.

## Punctuation and Formatting

Per 1,000 words in the core sample: about 56 commas, 21 opening parentheses, 7 colons, 4.6 semicolons, 0.5 question marks, and no exclamation points in running text.

Parentheses are the default aside. They hold four things, and little else:

- Author-year citations.
- Abbreviations at first use: "internal controls over financial reporting (ICFR)."
- Scale endpoints and statistics: "(means = 0.38 and 0.12; p = 0.018, one-tailed)."
- A short "e.g." or "i.e." gloss.

The em dash is the other aside, and it is for apposition in the prose, not for citations. Clean pages use it as a pair: "one such feature — the preparer's justification for a conclusion made — affects..." The Markdown often stores that dash as `--` because of conversion, so a raw dash count overstates hyphenation and understates the em dash. Write a real em dash, with a space or without, and use it once or twice in a section, not in every sentence. Parentheses outnumber clause-level dashes. If you are choosing, choose parentheses.

Semicolons join two closely related independent clauses or separate items in a list that already contains commas. Colons introduce a hypothesis, a variable list, or a "where" block under a regression. They do not introduce a one-word dramatic reveal.

Quotation marks are for scale labels ("absolutely willing to invest"), for a word used as a word ("warnings"), and for a short phrase from a press account or a standard. They are not for sneer quotes. Question marks belong in a title or in a labeled research question. A labeled RQ is allowed when the prediction is not directional:

> RQ: Will the use of data analytics differ between auditors prompted with a growth mindset and those prompted with a fixed mindset when inspection risk is low?

Do not write a rhetorical question in the middle of a theory paragraph.

### Citation punctuation is not stable, and that is the point

The corpus crosses journals and decades, so the year-mark moves:

- Older JAR and the 1995–1999 papers: Libby and Trotman [1992], with the year in brackets, "and" rather than "&."
- The 2000 AOS paper: (Libby & Trotman, 1993), with a comma and an ampersand.
- Later SSRN manuscripts: (Li 2008) or (Davis, Piger, and Sedor [2012]), and both occur.

Pick the convention of the venue you are writing for and do not blend them in one manuscript. The stable habit is the placement: the citation sits inside the sentence, immediately after the claim it supports, often two or three to a sentence. A paragraph of theory with no citation is not this corpus. A citation with no claim attached to it is not this corpus either.

### Headings

Where the source marks headings, they are numbered and short: "1. Introduction," "2.1. Subjects," "4.1. Hypothesis Testing," "Participants," "Manipulation checks." One to six words. The Markdown heading mean is not usable: most papers never became `#` headings, and one conversion glued the heading onto the following sentence. On the page, a heading does not repeat the hypothesis. It names the block.

Bold, on the page, marks "Hypothesis 1.", a research-question label, a table title, and an occasional word inside a stimulus ("slightly volatile"). It does not mark whole sentences in the argument. The Markdown `**` hits are almost all significance stars in regression tables (`**`, `***`), not emphasis. Do not bold for emphasis in the prose.

There are no block quotes, no colored words, and no pull quotes. Footnotes hold a design aside, a citation the sentence could not carry, and the standing rule "All p-values are two-tailed unless noted." That rule is said once.

### Mixed language

The prose is English. Tickers, standard numbers (SFAS No. 157, SAB No. 99, Regulation S-K Item 105), and variable names (SPEC, BUSY, DA) stay in Latin capitals. There is no Chinese, and no playful code-switching. A stimulus may quote a manager; the quote is then plain corporate English, not dialect.

### Register

Formal, concrete, and unembarrassed about repeating the dependent variable's name. The same noun ("investment willingness," "book-or-waive decision") returns in the hypothesis, the measure, the result, and the conclusion. Pronouns do not replace it. Humor is absent. Metaphor is absent, except when a theory already has a name ("affect-as-information," "configural"). The warmth in the paper is in the acknowledgment footnote, not in the argument. Do not import that warmth into the introduction.
