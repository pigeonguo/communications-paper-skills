# Communication-paper exemplars

Use this reference when learning from a source paper, shaping a storyline, or checking whether a revision preserves the logic behind a result.
The two papers below supply writing patterns, not a required research topic, method, or verdict on any venue's house style.
Their NOMA settings do not restrict this skill to multiple access.
All commentary here is original analysis; consult the cited paper for its equations and complete assumptions.

## How to annotate a reference paper

Select a few passages that perform difficult writing jobs; do not summarize every paragraph.
For each, record its location, reader question, rhetorical move, supporting evidence, and transfer limit.
Separate what the source explicitly establishes from your interpretation of why the presentation works.
Extract a reusable decision rule, then demonstrate it using a different topic.
Borrow the organization of reasoning rather than distinctive wording, domain claims, or citation lists.
Do not turn an example into an inflexible template merely because its authors used it successfully.

## Exemplar 1: A design choice whose answer depends on its constraints

**Source:** Zhiguo Ding, Pingzhi Fan, and H. Vincent Poor, “Impact of User Pairing on 5G Nonorthogonal Multiple-Access Downlink Transmissions,” *IEEE Transactions on Vehicular Technology*, vol. 65, no. 8, August 2016.
**DOI:** [10.1109/TVT.2015.2480766](https://doi.org/10.1109/TVT.2015.2480766).

### Most valuable move: make a small design question carry the paper

Section I, pp. 6010–6011, connects the multiple-access setting to a concrete pairing decision.
An accessible two-user example makes the resource-sharing mechanism understandable before detailed rate expressions appear.
The need to form groups then makes partner selection relevant to system performance.
The resulting question concerns which users to pair, rather than whether NOMA is generally useful.

**Transfer:** narrow a broad technology theme to a decision whose answer changes achievable performance, knowledge, or design practice.
Explain only the mechanism needed to see why that decision matters.
For a theory paper, the corresponding focus may be a condition, scaling law, or boundary rather than a controllable decision.

### Second move: organize analysis as a sequence of distinct questions

Section II-A asks about the probability that fixed-power NOMA has a lower sum rate than the orthogonal benchmark.
Section II-B examines the high-SNR sum-rate gap.
Section II-C considers individual user rates.
This progression separates how often an advantage occurs, how large it is, and how its benefits are distributed.
It gives closely related derivations different purposes instead of presenting them as an undifferentiated theorem list.

**Transfer:** introduce each result by the question it resolves; explain its implications after stating the result.
Keep probability of improvement, average improvement, worst-case guarantees, and fairness distinct.
Do not replace one metric with another while making prose shorter.

### Third move: use a changed constraint to explain a changed conclusion

Section III introduces cognitive-radio-inspired NOMA, where the weaker user's QoS constrains the power available to the stronger user.
Sections I and IV-B explain why pairing preferences differ from the fixed-power setting.
The stronger user's performance can be limited by the partner's channel through the admission constraint.
For the studied comparison with the strongest user fixed, the ergodic-rate discussion favors a different partner than the fixed-power comparison.

**Transfer:** when two plausible results appear to disagree, inspect the objective, feasible set, information, and operating regime before claiming a contradiction.
Present the changed assumption and the mechanism it changes together.
Conditional design guidance is a valuable contribution without a universal winner.

### Evidence and wording boundaries

- Section II-A, after Theorem 1, explicitly cautions that fixed-power NOMA does not always outperform orthogonal access.
- High-SNR expressions remain asymptotic statements; do not silently promote them to exact finite-SNR results.
- Sum rate, individual rate, outage probability, diversity order, and ergodic rate support different claims.
- The analyzed two-user, ordered-channel setting is not a proof of a globally optimal multiuser pairing algorithm.
- Section V identifies dynamic pairing/grouping design as future work; do not describe that algorithm as already delivered.
- Section IV compares analytical expressions and numerical behavior; use agreement to support the stated model, not every possible deployment.

**Annotation prompt:** Which premise makes the preferred partner change, and which exact metric supports that recommendation?

## Exemplar 2: An analysis result that creates an implementable control problem

**Source:** Wenjuan Yu, Chuan Heng Foh, Atta Ul Quddus, Yuanwei Liu, and Rahim Tafazolli, “Throughput Analysis and User Barring Design for Uplink NOMA-Enabled Random Access,” *IEEE Transactions on Wireless Communications*, vol. 20, no. 10, October 2021.
**DOI:** [10.1109/TWC.2021.3073326](https://doi.org/10.1109/TWC.2021.3073326).

### Most valuable move: turn an analytical optimum into a reason for the next section

Section I, pp. 6298–6300, moves from access contention to maximum throughput and the offered load that attains it.
Section III-B characterizes the throughput-maximizing load under the analysis model.
Bursty traffic makes maintaining that load a control problem rather than a static numerical exercise.
Section IV then needs an estimate of the current load because the receiver lacks direct knowledge of the active-user count.
Each stage supplies a reason for the next: characterization, target selection, state estimation, and access regulation.

**Transfer:** when an analysis produces a useful design target, explain what a real decision maker must observe and control to use it.
State whether the result gives a target, a guarantee, a heuristic, or only a diagnostic.
Do not append an algorithm merely to make an analytical paper look more complete.

### Second move: locate the gap along technical comparison axes

Section I distinguishes the packet-count throughput metric from achievable sum rate, different arrival assumptions, limited versus general numbers of power levels, and exact analysis versus bounds or approximations.
These comparisons let the reader see which question remains open in the considered model.
The analytical scope is therefore more informative than a vague statement that earlier work is insufficient.

**Transfer:** compare the closest works along the dimensions that matter to the current claim.
Prefer a specific missing characterization or capability over a long catalogue of topics.
Verify any novelty claim independently; a source paper's historical novelty assertion is not evidence of novelty for a new manuscript.

### Third move: expose an information ambiguity before adding a measurement

Sections III-C and IV-A explain that a throughput value alone can correspond to light or heavy traffic.
The additional idle-level observation helps resolve that ambiguity using receiver feedback.
This motivates the measurement through an identifiable limitation of the first observable.
Section IV-B then uses the estimate to adjust access probability.

**Transfer:** for each feedback signal, estimator, or feature, identify the uncertainty it resolves and how the decision uses it.
Distinguish an observable statistic from the latent state it estimates.
An extra input needs a role in the argument, not just an architectural label.

### Evidence and wording boundaries

- Here throughput counts successfully transmitted packets; do not relabel it as bit/s/Hz without a justified conversion.
- Section III-C defines an “idle channel” through an idle power level observed during decoding, before collision stops the process or decoding finishes. It does not mean that the entire channel is empty.
- Exact throughput expressions are exact within the stated analytical model, including its arrival and decoding assumptions.
- The perfect-SIC assumption in Section II and physical-layer limitations acknowledged in Section VI must travel with theoretical claims.
- Section V-A validates throughput calculations; Section V-B includes the capture-effect baseline; Section V-C investigates performance gain.
- Section V-D studies barring in an ideal environment; Section V-E (3GPP Macro Propagation) adds channel variation and decoding failures. These simulations do not remove the theorem's original assumptions.
- Throughput near the analytical maximum in tested conditions is not an unconditional closed-loop optimality or stability theorem.

**Annotation prompt:** What must the receiver know to use the optimal-load result, and which evidence shows that the proposed observable supplies that information?

## General principles distilled from the supplied storyline guide

Use an argument chain: setting → consequential question → relevant limitation → insight or hypothesis → analysis or method → evidence → scoped conclusion.
Adapt the chain to the work; a theoretical gap or puzzling observation can motivate research without an engineering tradeoff.
Keep the contribution, implementation, and evidence distinguishable even when they appear in one paragraph.
Give each paragraph a clear role and explain why its successor is relevant.
A proposed mechanism should answer an established need, while acknowledging reasonable alternatives.
Use a claim–evidence table; proofs, counterexamples, derivations, measurements, and simulations can each supply appropriate evidence.
Missing support should weaken, defer, or remove a claim rather than trigger invented results.
Let contradictory evidence change the storyline when necessary.
Avoid prescribing a fixed paragraph count, a mandatory algorithm, or a universal three-item contribution list.

## Two original transfer exercises

Both examples below are hypothetical writing exercises, not reported findings or literature claims.

**Finite-blocklength coding:** A project compares two decoding schedules under a fixed latency budget. A useful question is which error events dominate after the schedule is shortened. A proposed storyline can connect the latency constraint to the altered decision rule, then to a predicted error mechanism and its test. Until the analysis or experiment exists, write “We investigate whether shortening the schedule changes the dominant error events,” not “The schedule achieves optimal reliability.” Evidence should separate block error probability, latency, and decoding work.

**Beamforming with delayed CSI:** A project combines a channel predictor with robust precoding. Begin with the decision affected by CSI age, then explain which uncertainty prediction reduces and which uncertainty remains. A suitable evaluation plan compares prediction only, robustness only, and the combined design under matched information and resource budgets, with CSI-age variation. Before results exist, describe this as a plan; do not assert that both components are necessary or that the design works for arbitrary mobility.

In either exercise, retain the writing move while replacing the original paper's system, assumptions, and evidence.
