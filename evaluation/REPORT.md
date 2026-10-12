# Evaluation report — 0.1.0

Date: 2026-10-11. All tasks in this release are synthetic editorial exercises. Numbers and scientific scenarios in their inputs are fictional. Outputs are saved as generated, including limitations and minor defects; they are not model answers to copy into manuscripts.

## What can be concluded

The initial checks found no material invented evidence or loss of the main technical conditions in the inspected outputs. The new storyline/Introduction comparison produced good answers in **both** conditions. A separate reviewer expressed a slight preference for the skill-enabled storyline and a tie on the Introduction, with only a weak stylistic lean toward the skill-enabled version. These results do **not** establish a substantial or reliable quality gain from the skill.

The package is suitable for trying on real writing tasks and for further controlled evaluation. It is not validated as a universal communications-journal style, a proof checker or a route to publication acceptance.

## Initial four behavioral checks

Four separate fresh-context sessions executed the cases specified in [the skill's evaluation reference](../skills/communications-paper/references/evaluation.md). The original maintainer inspected the outputs for the listed core checks. No control condition was run for this initial set.

| Case | Main behavior checked | Recorded outcome | Raw output |
| --- | --- | --- | --- |
| Theory abstract | Retain fixed-distribution, blocklength, error and comparison-regime conditions without requiring an algorithm or experiments | Core checks met on this run | [theory.md](outputs/initial/theory.md) |
| Language-only LaTeX | Preserve symbols and keys; flag unsupported global optimality separately | Core checks met on this run | [polish.md](outputs/initial/polish.md) |
| Reviewer response | Separate performed changes from undecided experiments and reported removal from independently verified removal | Core checks met on this run | [response.md](outputs/initial/response.md) |
| Learning-paper results | Preserve the 24% arithmetic while flagging unequal CSI, omitted overhead and unsupported significance/generalization | Core checks met on this run | [review.md](outputs/initial/review.md) |

These tasks test bounded behavior and fidelity, not whether the prose is better than a competent baseline. The case descriptions are retained; the complete original generation-session wrapper prompts and full tool traces are not included, so this is a case-level record rather than a byte-for-byte reproduction package for that first set.

## New matched comparisons

Two new task inputs were written and fixed before generation. Each was given to two separate fresh-context agents using the same inherited model configuration: one was instructed to use the installed skill and its relevant writing references; the other was instructed to use ordinary writing ability and not read a writing skill. No external literature search was used. Neither generation condition received the scoring rubric or the other output.

| Task | Input | Ordinary prompt | With skill |
| --- | --- | --- | --- |
| Chinese storyline: energy-constrained sensor control | [Request](prompts/storyline.md) | [Output](outputs/comparison/storyline-baseline.md) | [Output](outputs/comparison/storyline-with-skill.md) |
| English Introduction: budgeted two-link packet replication | [Request](prompts/introduction.md) | [Output](outputs/comparison/introduction-baseline.md) | [Output](outputs/comparison/introduction-with-skill.md) |

The task inputs explicitly describe uncertainty, unavailable evidence and scope constraints in both conditions. This is a demanding instruction-compliance check but may make it difficult to demonstrate an additional benefit from the skill.

### Separate review

A separate fresh-context agent saw only the requests, [rubric](RUBRIC.md) and candidates labeled A/B. The labels were counterbalanced: storyline A = ordinary prompt, B = with skill; Introduction A = with skill, B = ordinary prompt. The reviewer did not receive this mapping. The maintainer read the raw outputs and the resulting [blind review](BLIND_REVIEW.md) before preparing this report.

| Finding | Storyline | Introduction |
| --- | --- | --- |
| Critical fabricated-evidence or condition-loss failure found | None identified in either output | None identified in either output |
| Ordinal rubric result | Both received 2/2 on all five dimensions | Both received 2/2 on all five dimensions |
| Preference | Slight preference for the skill output, low confidence | Tie; weak stylistic lean toward the skill output |
| Useful distinction in skill output | Separates a state-aware controller's benefit from evidence that DQN specifically is needed; asks whether the energy budget is enforced | More focused opening and explicit proof/source-verification note |
| Minor defect in skill output | “随后” implies an execution order absent from the input | “supplied ... model” sounds like drafting context rather than final manuscript prose |

All requested length ranges were met by the reviewer's recorded counts: ordinary/skill storylines were 948/973 nonwhitespace characters (851/874 Han characters); skill/ordinary Introductions were 456/485 words. Counting conventions are documented in the blind review.

The perfect coarse rubric scores are a ceiling of this small evaluation, **not** a claim that all four outputs are flawless. A refined task set and human editing-effort assessment would be more discriminating. The noted minor defects remain in the raw outputs; changing those files would erase the evaluation record.

## Limits and next evidence needed

- One run per condition on each of two tasks; no repeat-run reliability or statistical analysis.
- One model-based reviewer, followed by maintainer inspection; no independent human expert judgment.
- The platform inherited model settings across agents, but exact model identifier, sampling parameters and token budgets were not independently exported. No claim of exact reproducibility across hosts is made.
- Both conditions shared the host's general instructions and available-skill catalog metadata. Only the enabled condition was instructed to read the skill contents. This is not an isolated API-level ablation of every possible skill-related cue.
- Both tasks are outside the NOMA topics of the two published exemplars, but this does not establish coverage of all theory, systems, coding or network research.
- No real anonymized manuscript/expert-revision pair was tested in this round. No author editing time, acceptance outcome or theorem validity was measured.
- The rule set was not changed after seeing these new outputs. Keeping this version fixed avoids reporting revised outputs as if they were the original held-out run.

Recommended next step: use a permission-cleared real Introduction or storyline held out from rule creation, hide an expert revision during generation, and compare candidates anonymously on reasoning, fidelity, readability and the amount of editing needed. Use the resulting specific failure to decide whether another paper, an annotated revision or a narrower rule is needed.

中文结论：目前支持“可试用、能守住关键证据边界”，尚不支持“明显优于普通模型”。本轮两项对照中普通提示词也表现良好。下一步应优先使用未参与规则提炼的真实稿件和专家修改意见，而不是先追求论文数量。
