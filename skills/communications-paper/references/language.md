# Language, translation, and local revision

Aim for readable technical English with explicit logical relations. Do not imitate distinctive sentences from an exemplar. Preserve the author's technical meaning and requested level of intervention.

## Choose the editing level

- **Language-only:** grammar, terminology, local clarity and concision. Retain claims and structure; flag technical concerns separately rather than silently correcting the research.
- **Structural revision:** reorganize the authorized passage to repair logic and evidence flow, then polish sentences. Explain consequential changes.
- **Translation:** preserve mathematical meaning, citation keys and uncertainty; use natural target-language syntax. Translate “证明,” “验证,” “分析” and “表明” according to the actual evidence, not a fixed word substitution.

When a literal translation would overstate an unverified claim, preserve the intended meaning as far as possible and flag the issue. Offer a bounded alternative when support permits. Never turn an editorial fix into a new result.

## Paragraph flow

Give each paragraph a clear main message. Its sentences can define, qualify, compare or support that message. Move from known context to the new point. Use a transition when it identifies a real relation; remove empty connector chains.

Prefer a concrete subject and verb over “It can be easily observed that…” Explain why a method is needed before enumerating modules. Split overloaded sentences, but retain dependencies and conditions. Do not impose a maximum sentence length or ban all passive voice.

## Precision before intensity

- Use “derive,” “prove,” “characterize,” “estimate,” “evaluate” and “observe” when they identify the actual contribution.
- Use “suggests,” “is consistent with,” or “may” for interpretations that are not established; do not add hedging to a proved theorem merely to sound cautious.
- Delete unsupported “first,” “unprecedented,” “universally,” “optimal” and “significantly” or replace them with a verified, bounded statement.
- Preserve distinctions such as optimal/near-optimal, rate/throughput, spectral/energy efficiency, feasible/stationary, and asymptotic/finite-regime.
- Use “respectively” only when the mapping is unambiguous. Avoid vague “this,” “it” or “which” where multiple technical objects are possible.
- Define an acronym at its needed first occurrence and reuse one canonical term. Do not rename a scheme for variety.

## Mathematics and source integrity

Treat equations, variables, citation commands, macros and cross-references as protected content during language-only edits. Do not rename variables, remove conditions or change `$...$`, `\cite{...}`, `\ref{...}` or labels casually.

Flag ambiguous symbols, units or missing definitions separately. If the user authorizes technical corrections, make each consequential change traceable and recheck dependent prose. Never claim LaTeX compiled from visual inspection of the source alone.

## Original miniature examples

These are hypothetical editing examples, not claims about published research.

**Evidence: objective values form a convergent sequence; no global-optimality proof.**

Overstated: “The algorithm converges to the globally optimal solution.”

Bounded alternative: “The objective value converges under the stated update conditions.”

Note: this changes a technical claim; for language-only editing, flag it and present it as an alternative.

**Evidence: lower simulated outage in tested cases; no real-world evaluation.**

Overstated: “The framework guarantees reliable communication in practical networks.”

Bounded alternative: “The method reduces simulated outage in the evaluated settings.”

**Evidence: delay changes the available CSI.**

Wordy: “Due to the fact that the channel information is outdated, it is necessary to take the uncertainty into consideration.”

Clearer: “Delayed CSI introduces channel uncertainty, which the resource allocation must account for.”

Do not copy any example into a manuscript unless its conditions match the supplied work.

## Output

Return the clean revised passage first for a local edit. Add a small change table only if requested or useful for technical meaning: original issue, revision, reason. Do not explain every grammar correction or produce three alternatives by default.

Keep uncertain factual questions separate from completed prose. If the supplied content is already clear, make minimal changes rather than rewriting to display effort.
