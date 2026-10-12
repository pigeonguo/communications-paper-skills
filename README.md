# Communications Paper Skills

[中文说明](README.zh-CN.md) · [Installation](docs/INSTALLATION.md) · [Examples](examples/README.md) · [Evaluation](evaluation/REPORT.md)

An open-source research-writing skill for communications and information theory: build a coherent argument, draft and revise sections, preserve mathematical meaning, and respond to reviewers using the evidence actually available.

**Status: v0.1.0, experimental.** The package is ready to inspect and install as a folder. Its writing quality is not established by a large benchmark or submission outcomes. See the raw tasks, outputs and limitations in the [evaluation report](evaluation/REPORT.md).

## What it helps with

| Task | Intended output |
| --- | --- |
| Storyline and positioning | A question-driven argument connecting the problem, limitation, approach and evidence |
| Introduction and contributions | Relevant related work, explicit reasoning bridges and bounded contribution statements |
| Section drafting | Abstract, model, analysis, method, results, conclusion and captions at the requested scope |
| Polish and translation | Readable prose with notation, citations, quantifiers and technical meaning preserved |
| Review and response | Located concerns, actionable revisions and replies that distinguish completed from planned work |
| Learning from papers | Annotated writing moves, explanations of their effect and conditional transfer rules |

The scope includes theory, performance analysis, optimization, learning and experimental systems. Venue profiles cover **IEEE TWC, TCom, TIT, ICC and GLOBECOM**. These profiles are writing guidance, not official journal templates. The skill does not require a particular technology, an algorithm in every paper, or experiments for a purely theoretical result.

## Quick start

1. Download or clone this repository.
2. Install the entire [`skills/communications-paper`](skills/communications-paper) folder using the [host-specific instructions](docs/INSTALLATION.md). Copying only `SKILL.md` loses the reference modules.
3. Give the assistant a manuscript excerpt or research notes, the intended task and any scope restrictions.

For Codex CLI/IDE:

```text
Use $communications-paper to revise the Introduction below for a communications
journal. First identify the central question and missing reasoning links, then
return the revised Introduction. Preserve citation keys and supported claims.
Treat the supplied results as author-reported; do not add experiments or citations.
```

For Chinese discussion and an English manuscript:

```text
使用 communications-paper。先用中文解释这份提纲的逻辑问题，再写英文 Introduction。
每个方法选择都要先说明它解决什么问题；保留公式和引用键，不补造研究结果。
```

No API key, training process or runtime library is required by the skill itself. A host capable of reading skill files is required; reading PDFs, editing Word or searching literature may use that host's separate tools. Local installation and the ChatGPT Work Skills management page have different discovery mechanisms; this repository does not claim to repair a missing UI entry.

## Design

One compact entry file routes each task to only the relevant references. The detailed rules cover argument, sections, rigor, language, review responses, venue profiles and exemplars. This keeps everyday use focused while making the reasoning inspectable.

The workflow is: establish the requested scope → identify evidence and assumptions → construct or revise the argument → draft the prose → check technical consistency. The assistant should produce the requested text, not stop at a checklist.

| Repository location | Purpose |
| --- | --- |
| [`skills/communications-paper/SKILL.md`](skills/communications-paper/SKILL.md) | Agent instructions and routing |
| [`skills/communications-paper/references`](skills/communications-paper/references) | Nine task-specific reference modules |
| [`docs`](docs) | Installation, publication and reference-expansion guidance |
| [`examples`](examples) | Reusable prompts, input brief and original miniature examples |
| [`evaluation`](evaluation) | Synthetic requests, actual outputs, rubric and assessment |
| [`scripts/validate.py`](scripts/validate.py) | Structural and local-link validation; does not grade prose |

## What “learning from papers” means

This is an instruction package, not a trained model or a paper database. Adding a PDF does not update model weights or automatically improve the skill. A useful update extracts a specific writing move, records its limits, changes a relevant instruction and checks the result on another task.

Two initial exemplars provide patterns for conditional design insight and analysis-to-control reasoning. Both concern NOMA; one is a TVT paper and one a TWC paper. This narrow source sample does **not** establish coverage of all communications writing. The rules are designed to transfer more broadly, and the evaluation deliberately includes other topics.

Start with real failures. If the problem is a weak proof narrative, add a carefully annotated theory paper. If methods appear before their motivation, add a strong problem-to-method example or an anonymized before/after revision. A previously suggested four-to-six-paper expansion is an optional way to diversify the sample, not a quality threshold. See [how to extend the skill](docs/ADDING_REFERENCES.md).

## Validation and contribution

With Python 3.10 or later and PyYAML:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
```

These dependencies are for repository validation only. Behavioral evaluation is a separate reading and drafting exercise, documented in [evaluation/REPORT.md](evaluation/REPORT.md). Do not interpret a successful structural check as proof of writing quality.

Contributions are welcome as focused changes with a concrete motivating failure and a transfer test. Read [CONTRIBUTING.md](CONTRIBUTING.md). To publish your own copy, follow [the GitHub guide](docs/PUBLISHING.md); the export contains no owner-specific remote URL.

## Sources and license

The modular workflow was inspired by [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills), inspected at commit `e605b35611ab2849af46d0cf7831aefdcf85be07`. The communications-specific instructions and examples were written for this project. See [NOTICE](NOTICE) and the [source record](skills/communications-paper/references/provenance.md).

Licensed under [Apache-2.0](LICENSE). Source papers, figures and private manuscripts are not redistributed and retain their own rights. This project is independent of IEEE, Nature and the upstream contributors; it makes no acceptance guarantee.
