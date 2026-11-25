# End-to-end test: experiment abstract

Run on 2026-11-25. Genre: experiment abstract. Venue: unnamed. The source is a rough paragraph supplied for this system. The five papers were read for cadence. None of their findings are in the draft.

## Selection

```text
python3 select_papers.py --type experiment --tag managers --tag earnings --tag motivated --tag tone --tag justification
```

All five were matches. None was a fill.

1. 2022-08-16. You Have Been Forewarned! The Effects of Risk Management Disclosures and Disclosure Tone on Investors' Judgments.
2. 2013-12-09. When the Use of Positive Language Backfires: The Joint Effect of Language Sentiment, Readability, and Investor Sophistication on Earnings Judgments.
3. 2012-08-26. Fair Value Accounting and Managers' Hedging Decisions.
4. 2009-07-14. Investors' Reactions to Management Earnings Guidance: The Joint Effect of Investment Position, News Valence, and Guidance Form.
5. 2000-01-01. Effects of the preparer's justification on the reviewer's hypothesis generation and judgment in analytical procedures.

## Shared cadence

The five abstracts open on the joint setting, with "We investigate," "We conduct," or "We report the results of an experiment." The result is one comparison sentence: the effect holds when one condition is present and does not hold when it is absent. A later sentence bounds a prior result ("we extend this research by showing that ... is conditional on"). The 2012 abstract is the one that says "two experiments" up front and then separates what the second experiment changed. The 2000 abstract is shorter on the close ("Implications of the results are discussed"). The later ones put the boundary in the abstract itself. One design clause is allowed. Short sentences are not stacked.

## Checklist

- [x] Five DNA files read before the draft.
- [x] article_type: experiment.
- [x] Five papers listed above, all matches.
- [x] Cadence stated before the prose.
- [x] Full text of the five abstracts was read. The draft does not use their results.
- [x] Every claim below is in the source paragraph.
- [x] No catalog byline.
- [x] The result is conditional on an optimistic goal, and it is absent for a pessimistic goal.
- [x] The cells are not mirrored. The source signed only the optimistic side.
- [x] The mechanism stays at the source's strength ("entails," "allows"). It is not upgraded to a tested path.
- [x] No citation. The source named none. Left uncited on purpose.
- [x] "We." Not "I."
- [x] "Managers," the noun the source used. "Participants" was not added, because no pool was supplied.
- [x] Six sentences: 23, 34, 13, 22, 23, and 23 words. The 34-word sentence is the comparison. The 13-word sentence follows it and states the mechanism contrast. They are not stacked shorts, and there are not three long sentences in a row.
- [x] "Algorithmic advice" is repeated. It is not renamed "this outcome."
- [x] "Find" and "show" carry the results. No "associated with."
- [x] No "importantly," no "very," no exclamation, no rhetorical question, no bold.
- [x] MEMORY.md read. Venue unnamed, so no citation mark was chosen. There is no citation to punctuate.
- [x] The close names businesses and other settings in which the decision maker has algorithmic advice and a directional goal.
- [x] No limitation paragraph. The source did not include one.
- [x] Tell-cleanup already applied to this paragraph. The "when / but not when" contrast was kept. That contrast is the result. It is not a straw-man reversal.

## Source

In this study, we experimentally investigate how financial managers make earnings forecasts based on algorithmic advice versus human advice under different directional goals. Across two experiments, we find that managers are less likely to follow algorithmic advice relative to human advice when their goal is to forecast optimistically, but not when their goal is to forecast pessimistically. This is because the optimistic goal entails a stronger need for justification than the pessimistic goal, and the ambiguity inherent in algorithmic advice allows managers to justify their biased forecasts by underweighting algorithmic advice relative to similar human advice. Our study enriches the cross-disciplinary conversation of algorithm aversion by showing that algorithm aversion is stronger when the decision setting involves a greater need for justification. Our findings carry implications for not only businesses but also other decision contexts where both algorithm-powered technologies and directional goals play a role.

## Draft

We conduct two experiments to examine how financial managers make earnings forecasts based on algorithmic advice versus human advice under different directional goals. Across the two experiments, we find that managers are less likely to follow algorithmic advice than human advice when their goal is to forecast optimistically, but not when their goal is to forecast pessimistically. An optimistic goal entails a stronger need for justification than a pessimistic goal. The ambiguity inherent in algorithmic advice allows managers to justify their biased forecasts by underweighting algorithmic advice relative to similar human advice. We extend research on algorithm aversion by showing that algorithm aversion is stronger when the decision setting entails a greater need for justification. Our findings have implications for businesses and for other decision settings in which decision makers use algorithmic advice and hold a directional goal.

138 words. Inside the 120–220 band.

## Left out on purpose

No citation, no cell mean, no participant pool, no second-experiment manipulation, and no author from the five papers. "Enriches the cross-disciplinary conversation" and "not only businesses but also" were the source's framing. The draft keeps the boundary and both audiences and drops that framing.
