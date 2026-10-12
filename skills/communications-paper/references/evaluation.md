# Behavioral regression cases

Read this file when evaluating or modifying the skill, not during ordinary manuscript work. These are synthetic editorial tasks created for this package; none reports new scientific findings.

## Procedure

Give a fresh agent the SKILL.md path and a request built from the case input below. Let it load the routed references. Do not provide the evaluation criteria, prior output, source-design discussion or a diagnosis in its task context. Inspect the resulting prose and any actual edits before marking a case passed. Repeat only the cases affected by a change, plus a broader case if the routing or core evidence policy changes.

Judge: request completed; facts and conditions preserved; no invented support; appropriate edit scope; natural readable prose; source/verification status clear. These are behavioral checks, not exact-output snapshots. A correct answer can differ in structure or wording.

## Case 1: Theory without an algorithm or experiments

**Input:** Author notes for a TIT abstract and three contribution bullets: finite-alphabet discrete memoryless channel; fixed input distribution; nonasymptotic achievability lower bound for blocklength n >= n0 and average error constraint 0 < epsilon < 1/2; tighter than the bounds compared in the manuscript only within parameter set S; refined random-coding argument retains a previously relaxed term; proof is in appendix; no converse, coding algorithm or simulations. Formulas and citation keys unavailable. Ask for prose without external search.

**Check:** Deliver an abstract and three bullets. Retain n, epsilon, fixed-distribution and S restrictions. Do not claim capacity, universal superiority, an invented magnitude, citations, algorithm or simulation. Do not demand experiments as a prerequisite for drafting. Flag definitions/comparators that require final manuscript alignment.

## Case 2: Language-only LaTeX with a technical concern

**Input:** Ask for language-only polish while retaining claims, variables and references. Paragraph argues that monotone bounded objective values imply global optimality of Algorithm~\ref{alg:ao} at $\mathbf{W}^{\star}$; reports a 12\% average sum-rate gain at $P=20$ dBm against \cite{baseline2023}, pointing to Fig.~\ref{fig:rate} and (\ref{eq:obj}). Author notes confirm only objective-value convergence has been proved.

**Check:** Preserve citation/reference keys, symbols and the single-point numerical comparison. Do not silently replace the mathematical assertion under language-only scope. Explicitly flag unsupported global optimality and give a separately labeled correction consistent with objective-value convergence; do not certify iterate convergence. Return the polished passage, not only advice.

## Case 3: Reply with completed and unresolved work

**Input:** Reviewer asks for imperfect-CSI experiments and justification of real-time complexity. No imperfect-CSI tests exist and authors have not decided to run them. Supplied revised abstract says “The algorithm improves the simulated sum rate under the assumed perfect CSI.” Supplied Section IV-C says “Each iteration requires O(K^3) arithmetic operations, where K is the number of users. No wall-clock runtime measurements are available.” Author reports removing “real-time” everywhere; full manuscript and final page numbers unavailable. Ask for two English point-by-point replies.

**Check:** Draft both replies. Do not assert or promise unperformed experiments. Distinguish narrowing a claim from satisfying an experiment request. Preserve per-iteration versus wall-clock distinction. Use supplied excerpts accurately, mark full-manuscript removal as author-reported in the handoff, and do not invent pagination or claim full verification.

## Case 4: Learning-paper comparison with unequal information

**Input:** Ask for self-review and one English Results paragraph, with no external search. Reported rates are 12.4 and 10.0 bit/s/Hz under equal bandwidth, antenna count and transmit power. Proposed method has full instantaneous CSI; baseline has statistical CSI. Neither rate includes pilot/feedback deductions. One seed per method; no uncertainty analysis. Samples share one channel model; random sample splitting may place neighboring samples from a trajectory in both training and test sets. Draft claims a statistically significant 24% net-throughput gain over a state-of-the-art baseline and proof of unseen-environment generalization.

**Check:** Preserve and correctly calculate the 24% relative difference. Flag information-budget mismatch, overhead accounting, unsupported significance/SOTA/generalization and potential dependence/leakage. Do not declare leakage proven. Produce usable bounded Results text, with no invented repeat runs, overhead-adjusted rates or future-experiment completion.

## Recorded scope

On 2026-10-11, four separate fresh-context agents executed these four tasks against release 0.1.0. The maintainer inspected their actual outputs; all four met the listed core checks. Structural checks also passed for frontmatter, UI metadata, relative reference links and absence of local/private source paths.

No claim is made about repeat-run reliability, superiority to an unassisted model, acceptance likelihood, complete mathematical verification, or validation on real anonymized review packages. Add further cases when actual usage exposes a specific failure; do not inflate test counts with phrase-presence assertions.

## Additional public-release comparison

On 2026-10-11, two further synthetic requests were each executed in separate fresh sessions with and without reading this skill: a Chinese storyline for energy-constrained sensor control and an English Introduction on budgeted two-link packet replication. The same inherited model configuration and task inputs were used; the ordinary-prompt condition was instructed not to read writing-skill files. Both conditions retained the host's general instructions and catalog metadata, so this was not an isolated API-level ablation.

A separate reviewer received the requests, a five-dimension rubric and condition-blinded A/B outputs, with order counterbalanced between tasks. Both conditions met the coarse rubric on both tasks. The reviewer slightly preferred the skill-enabled storyline and tied the Introductions with a weak stylistic lean toward the skill-enabled version. The maintainer inspected the outputs and review. No substantial or reliable quality gain is established by this one-run-per-condition exercise.

Minor issues remain in the raw skill-enabled outputs: one temporal connector implies an execution order not supplied in the notes, and one Introduction phrase exposes drafting context ("supplied model"). Retain raw outputs when reporting this evaluation; do not silently correct them. The writing rules were not revised after seeing these outputs.

The standalone public-source release includes exact task inputs, all four new outputs, the rubric, the blinded review and reproduction wrappers. Exact model identifier and sampling parameters were not independently exported. Next prioritize human comparison on an anonymized manuscript/expert-revision pair held out from rule creation. More source papers should address a diagnosed weakness rather than serve as a numerical quality threshold.
