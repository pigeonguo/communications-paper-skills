# Sources, authority, and extension

Package: communications-paper. Initial release: 0.1.0, 2026-10-11. The instruction prose and hypothetical examples were written for this package. Sources supply design inspiration, scoped paper analysis and venue facts; this is not an official IEEE or Nature product.

## Design source

[Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills), inspected at commit [`e605b35611ab2849af46d0cf7831aefdcf85be07`](https://github.com/Yuan1z0825/nature-skills/tree/e605b35611ab2849af46d0cf7831aefdcf85be07).

Relevant inspected components:

- `skills/nature-writing/SKILL.md`, `manifest.yaml`, and `static/core/{stance,workflow}.md`.
- `skills/nature-polishing/SKILL.md` and `static/core/failure-modes.md`.
- `skills/nature-reviewer/SKILL.md` and its source-basis, technical-concern and consistency references.
- `skills/nature-response/SKILL.md`, manifest, core workflow, action mapping, package audit and evaluation materials.
- `skills/nature-shared` terminology, consistency, Introduction and main-text guidance.
- Repository validation and instruction-contract tests.

Adapted design ideas: small task router; references opened on demand; evidence and terminology before wording; localized revision; traceable review concerns; revision status tied to actual work; structural and behavioral evaluation distinguished.

Communications-specific changes: one self-contained entry point; paper types separate from venues; explicit contribution lists allowed; model/information/metric budgets; theorem and asymptotic boundaries; theory-to-control transitions; no mandatory experiments for theory papers; no broad interdisciplinary-significance requirement; no universal Nature manuscript structure. Error-bar overlap is not treated as evidence of statistical equivalence or nonsignificance.

Upstream is licensed under Apache-2.0. This package includes an Apache-2.0 license and a design acknowledgement in NOTICE. No upstream executable code, journal PDFs, figures, or private guide document is bundled.

## Writing sources

Two user-selected papers are analyzed in `exemplars.md`:

1. Ding, Fan and Poor, *Impact of User Pairing on 5G Nonorthogonal Multiple-Access Downlink Transmissions*, IEEE TVT, 2016. DOI: [10.1109/TVT.2015.2480766](https://doi.org/10.1109/TVT.2015.2480766).
2. Yu, Foh, Quddus, Liu and Tafazolli, *Throughput Analysis and User Barring Design for Uplink NOMA-Enabled Random Access*, IEEE TWC, 2021. DOI: [10.1109/TWC.2021.3073326](https://doi.org/10.1109/TWC.2021.3073326).

These provide examples of question-driven analysis, conditional design insight and analysis-to-control reasoning. They do not establish a universal communication-journal style or the current state of the field. One exemplar is TVT, not TWC/TCom/TIT; do not mislabel its venue.

A user-supplied storyline guide informed the general argument and evidence workflow. Only original high-level synthesis is included; the private source is not redistributed and is not needed to run the skill. Venue sources, dates and access limits are recorded in `profiles.md`.

## Authority categories

Keep these separate when applying or extending the package:

- **Editorial rule:** verified current official instructions for the exact target.
- **Manuscript fact:** supplied or inspected research evidence, with verification status.
- **Exemplar observation:** a writing move found in a located passage of a particular paper.
- **Writing heuristic:** a proposed reusable decision rule; overridable by task and evidence.
- **Author preference:** tone, language or structure requested by this user; not a rule for all users.

No citation quantity can turn an unverified claim into a proven one. Generality comes from appropriate conditional rules, not collecting an indiscriminate pile of PDFs.

## Add a reference or modify the skill

When asked to learn from another source:

1. Read the actual supplied/accessible source. Record identity, relevant locations and what was inspected. Disclose access limits.
2. Annotate a few valuable moves: reader question, technique, effect, support and transfer boundary. Explain source content in original words; do not import full papers or private draft text.
3. Propose a conditional rule and identify where it belongs: core, paper-type option, venue rule, exemplar or author preference. One example usually supports an optional pattern, not a universal mandate.
4. Test the rule on a different topic and on a case where it should not apply. Update examples if needed; avoid adding a large dependency for a prose rule.
5. Check for conflict with evidence preservation, user scope and existing references. Update the relevant file rather than duplicating rules across modules.
6. Validate paths/frontmatter and run fresh behavioral tasks after material changes. Record the release and evaluation scope; persist through the host's skill-saving workflow. Reading a paper during ordinary manuscript work does not itself authorize changing the installed skill.

Useful behavioral tasks include a theory abstract without simulations, a local LaTeX polish, a learning-paper comparison with mismatched information, a response containing both completed and planned work, and reference analysis outside NOMA. Judge actual outputs: factual fidelity, preserved conditions, fulfilled task, appropriate scope, readable prose, and no invented evidence. Static phrase checks alone cannot establish writing quality.

The initial release was forward-tested on four fresh-context tasks covering theory drafting, local LaTeX polishing, revision responses and learning-paper result review. All four met their stated fidelity and task-completion checks on the inspected run. See `evaluation.md` for reproducible case specifications and limits. This is a small synthetic evaluation, not a writing-quality benchmark or a validation on real submission outcomes.
