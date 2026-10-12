# Section jobs and drafting choices

Use these as functions, not a fixed manuscript skeleton. Match the requested section, paper type and target instructions. Theory papers need not have an algorithm or experiment section; communications papers need not have a separate Discussion.

## Title

Name the central object/problem and distinguishing result or approach. Avoid unsupported superlatives, acronym chains, and fashionable technologies absent from the actual contribution. Do not advertise “optimal” unless its objective, domain and guarantee warrant it. A colon or question title is a choice, not a rule.

## Abstract

Make the paper understandable on its own: precise problem, approach or result, decisive support, and bounded takeaway. Use a compact progression; do not prescribe a universal sentence count or word limit.

- State what was established, not just “simulations are performed.”
- A theorem-led abstract can emphasize characterization, bound or scaling law rather than numerical gains.
- Include a numerical result only when supplied and meaningful with metric, comparator and conditions. Do not require a percentage merely to sound persuasive.
- Keep consequential conditions adjacent to the result. Remove low-value implementation detail before dropping the qualification.
- Define unfamiliar abbreviations when necessary; minimize citations and symbols according to the target instructions rather than inventing a blanket rule.
- Draft or revise after the main claim is stable. Cross-check each abstract promise against the body.

## Introduction

Use the argument workflow. Establish the question early; include enough background for communications researchers outside the narrow subtopic. Explain the obstacle before detailing machinery. End with bounded contributions and an optional brief organization paragraph if helpful or conventional for the target.

Contribution lists are allowed. Prefer a few distinct, supportable items over repeated versions of the same algorithm. Related work may be integrated or separate; avoid duplicating the same literature summary in both places.

## Related work

Organize around distinctions that explain this paper's question. Represent earlier achievements fairly and compare assumptions. A survey requires an explicit coverage basis; an ordinary Introduction need not pretend to be systematic. Do not turn a writing task into unsolicited exhaustive literature search unless novelty verification requires it.

## System model and problem formulation

Introduce entities, notation, observations, assumptions, variables and metrics in the order needed to understand the question. An initial verbal model helps readers interpret equations. Place each assumption where it enters the model or derivation.

Define objective and feasible set; clarify time scales, instantaneous/average quantities, CSI and resource constraints. Explain why the formulation captures the stated question. Avoid repeating every symbol in a long notation table when local definitions suffice; use a table when dense recurring notation makes it useful.

Preserve supplied LaTeX, indices, equation labels and definitions. Mark ambiguous notation rather than guessing. Do not silently change a mathematical model during prose editing.

## Analysis, theorems and proofs

Before a result, tell readers which question it answers and under what setting. State the theorem with complete material conditions. Afterward, give a short interpretation: what changes, why it matters, and which regime or metric controls it.

Explain the proof strategy where useful; keep derivation details accessible without narrating every algebraic step. Distinguish an exact expression from an approximation and a theorem from an empirical conjecture. A corollary or limiting case should add insight rather than duplicate the statement.

Do not invent missing proofs. A proposed proof sketch must be labeled and checked as far as the available material permits. Preserve appendix pointers and keep the main text understandable if detailed proofs are moved.

## Method or algorithm

Move from obstacle to design principle to operations. State inputs, outputs and available information; describe the major operations; then present guarantee, complexity or evaluation as supported. Pseudocode should clarify execution without repeating prose line by line.

Explain approximation and relaxation choices and any recovery step. Separate algorithm design from proved guarantees. A practical controller derived from an analytical optimum needs a way to observe or estimate the controlling state.

## Numerical results or experiments

Organize by research question, not the order in which experiments were run. A useful result paragraph contains a claim, evidence pointer, bounded interpretation, and condition or exception when consequential. It need not contain all four as separate sentences.

Use only relevant evidence functions:

- Validate an analytical expression or implementation.
- Compare against appropriate methods or bounds.
- Explain a mechanism through a meaningful variation.
- Test a component or design choice.
- Establish cost, sensitivity, robustness or deployment limits.

Do not require every paper to include all of these. Give setup detail once, point to figures precisely, select decisive values, and explain what the reader learns. Avoid a figure-by-figure catalogue of curve colors or “the proposed scheme is superior.”

If a figure is not accessible, request or mark the missing values; do not infer its contents from a caption alone. Separate observed tendencies from their proposed explanation.

## Captions and figure discussion

Identify the plotted quantity, independent variable, important conditions and meaning of lines/markers/error bars. Put enough information in the caption to interpret the plot without duplicating an entire paragraph. Cite the source of reused data/graphics where applicable.

Claims in captions must match the body. Do not label an estimated or simulated curve “theoretical” unless that is what generated it. Preserve axis units, normalization and panel labels.

## Discussion and conclusion

Synthesize the answer and its implication instead of repeating the abstract or listing all figures. Separate established design insights from prospective applications. Tie limitations and future work to a named boundary: imperfect CSI, different channel family, unproved converse, limited testbed scale, or another actual unresolved issue.

A short conclusion can combine answer, conditional implication and one meaningful open direction. Do not invent a limitation merely to fill a template or broaden a result to all networks.

## Compression and journal/conference adaptation

Identify the central contribution and shortest evidence chain. Remove repeated motivation, generic background, redundant plots and verbose setup before removing model conditions or decisive evidence.

For a shorter conference paper, narrow the claim and scope when necessary rather than promising an unavailable journal-sized study. Never assume a fixed page limit, extra-page allowance, anonymization policy, appendix permission or “30% new material” rule. Check current official instructions for the exact venue, year, track, article type and stage.

For a conference-to-journal extension, describe the actual added question, result, evidence and relation to the earlier work, with verified citations/disclosure as required. More pages or renamed sections do not demonstrate a substantive extension.

## Cross-section pass

Trace each main contribution to the body; check abstract and conclusion strength against it. Check names, numbers, parameter ranges, comparison sets, theorem conditions and figure references. A local edit needs the affected checks, not a mandatory manuscript-wide overhaul.
