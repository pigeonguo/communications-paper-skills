# Argument, storyline, and contribution

These are writing heuristics, not required IEEE section templates. Scale them to the supplied evidence and requested task.

## Start from the research question

Recover five items from the material: the system or mathematical problem; what remains uncertain; why that uncertainty matters; what the work establishes; and under which conditions it holds. An algorithm name is not a research question. A new bound, a counterexample, an explanation, or a design criterion may be the main contribution.

Use a provisional anchor when helpful:

> For [problem under assumptions], this work establishes [specific result] through [analysis/design/measurement], providing [bounded insight or capability].

Do not force every paper into one discovery. A central question may have linked subquestions. Do not invent a dramatic conflict when a precise unresolved question is enough.

## Choose a chain that fits the work

| Paper pattern | Useful argument progression |
|---|---|
| Fundamental limits or characterization | Defined object → unresolved property → result and conditions → proof idea → implication or limiting case |
| Performance analysis | Operational uncertainty → tractable model → metric characterization → mechanism/regime → conditional design insight |
| Optimization or algorithm | Decision problem → obstacle in constraints/information/computation → design principle → algorithm → guarantee or evaluation → cost and boundary |
| Learning for communications | Decision and observations → shortcoming of available approaches → learning role → training/deployment contract → evidence of benefit and generalization limits |
| Measurement or experimental system | Practical question → measurement/design choices → observed behavior → supported explanation → deployment scope |
| Survey | Explicit scope and selection basis → taxonomy → critical comparison → unresolved questions grounded in the surveyed material |

Mixed papers can join chains. Explain the bridge: e.g., an analysis identifies an optimal operating load, but a controller additionally needs an observable way to estimate current load. Never treat an analytically optimal target as an implementable policy without explaining this step.

## Build an evidence map before major drafting

Use a small working table:

| Claim | Existing support and location | Conditions | Wording strength | Missing support |
|---|---|---|---|---|
| What is actually established? | Theorem, derivation, figure, table, measurement, verified source | Model, regime, metric, comparator | Proves / derives / evaluates / observes / suggests | Specific open item or none |

Keep exact locations when available, such as Theorem 2 or Fig. 5(a); never manufacture page or line numbers. Mark author-reported support if not inspected. If evidence contradicts the proposed story, revise the story. Do not reinterpret unfavorable results merely to preserve the opening claim.

## Develop the Introduction

Use the shortest progression that answers these reader questions:

1. What technical setting and decision or knowledge problem matters here?
2. What do relevant existing approaches already accomplish?
3. What specific question or capability remains unresolved under the relevant assumptions?
4. Why is that question difficult, and what insight motivates this approach?
5. What does the paper establish, and how will the body support it?

These are functions, not five mandatory paragraphs. A compact conference paper may combine them. A theory paper may introduce the mathematical object early. A full journal Introduction can use explicit numbered contributions. Avoid forcing a Nature-style broad interdisciplinary opening or a fixed eight-paragraph funnel.

Prefer a concrete bottleneck over generic claims about exploding traffic or 6G. For example, explain how delayed channel observations change a resource decision before listing a fashionable architecture. A background sentence must help the reader understand the later question.

## Turn related work into an argument

Group studies by the distinction relevant to this paper: metric, knowledge assumptions, model generality, guarantee, complexity, robustness, or implementation. For each group, state its achievement before its relevant limitation. Verify that each citation supports the adjacent claim.

Distinguish:

- “We did not locate a result for this setting in the sources reviewed” from “No prior work exists.”
- Different problem assumptions from a demonstrated deficiency.
- A closed-form expression from an exact result: an integral or recursion can be exact; a closed form can be approximate.
- A missing analysis from a missing algorithm, and a missing implementation from a missing theoretical guarantee.

Do not call prior work impractical just because it is an oracle or a bound. It may be an informative reference. Do not imply comprehensive search from a few selected papers.

If citations are absent, draft bounded positioning and put specific citation requests outside or at the relevant passage. Do not invent plausible author-year pairs, bracket numbers, or BibTeX keys.

## Write contributions with technical content

Each contribution should identify the result or capability, its distinguishing scope, and its support when useful. Separate dependent contributions without counting every implementation step as novelty.

- Analysis: identify the quantity characterized and assumptions covered.
- Theorem: identify the property, bound direction, tightness/regime, and its consequence when established.
- Algorithm: identify the decision/information structure, guarantee if proved, and meaningful cost.
- Experiment: identify what was demonstrated and under which comparisons.
- Insight: identify a conditional relationship that changes understanding or design.

“We propose a novel efficient framework” is a label, not a contribution. “We derive an outage expression accounting for estimation error” is only appropriate if the derivation actually includes that error. Do not convert numerical improvement into a universal guarantee.

## Reverse-outline a draft

For each paragraph, write its main job and the question it answers. Look for missing links, duplicated background, unsupported transitions, and methods introduced before their purpose. Preserve useful text. Prefer a targeted move, deletion, or connecting sentence over a full rewrite.

Make each transition explicit in substance: an assumption limits a result; a result motivates a design target; a measurement tests an explanation. Adding “therefore” cannot establish a relation absent from the evidence.

For requested outputs, default to a concise diagnosis followed by the revised argument or prose. Show the full evidence map or paragraph map only when requested or when it resolves a substantial ambiguity.
