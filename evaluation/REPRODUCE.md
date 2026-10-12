# Reproduce or extend the editorial checks

## Structural check

From the repository root:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
```

This checks release files, frontmatter, UI metadata, local link targets and obvious environment-specific paths. It does not access a model, fetch external URLs, validate scientific claims or test host UI discovery.

## New task pairs

Use a fresh session for each condition and each task. Give both conditions the same model, output budget, tools and exact input file where those settings are controllable. Replace the paths below with actual local paths; the placeholders are not runnable shell commands.

**Skill condition wrapper:**

```text
Use communications-paper at <repository>/skills/communications-paper/SKILL.md
to complete the writing task in <task-file>. Read only the task file, skill
entry and references relevant to the requested writing task. Do not read
maintenance/evaluation/provenance files, a scoring rubric, or other outputs.
Write the complete response to <output-file>. Do not modify the skill.
```

**Ordinary-prompt condition wrapper:**

```text
Complete the writing task in <task-file> using your ordinary writing ability.
For this task, do not invoke or read a research-writing skill or its references,
and do not read other files beyond the task. Write the complete response to
<output-file>. Do not modify other files.
```

Use [storyline.md](prompts/storyline.md) and [introduction.md](prompts/introduction.md) as the two task files. These synthetic notes intentionally supply all substantive evidence; no web lookup is needed or requested.

## Review procedure

Preserve outputs before inspecting or correcting them. Relabel the two candidates A/B and keep the mapping out of the reviewer's context. Randomize or counterbalance order; the recorded run used opposite orders for the two tasks. Give a separate reviewer only the original task, the two outputs and [RUBRIC.md](RUBRIC.md).

Request dimension scores with passage-level justification, critical failures, measured length and a preference or tie with uncertainty. Reveal condition labels only after the review has been saved. Read the actual prose yourself rather than relying solely on numeric scores.

For the initial four cases, use the case inputs in [the evaluation reference](../skills/communications-paper/references/evaluation.md). Construct an execution prompt from the input only; keep that file's checks and prior results hidden from the generation session.

Record the skill version or commit, date, available model/settings, exact prompt, tools actually used and output. If a setting is unavailable, say so. Repeat across tasks and seeds when needed to resolve a real remaining question. A future release may improve a failure case, but do not overwrite the initial record or call a training example a held-out test.

## Human comparison

For a manuscript you have permission to use, keep the expert's revision hidden during generation. Ask the expert to compare the candidates without condition labels. In addition to the rubric, record concrete edits still needed and whether either candidate changed scientific meaning. Keep private manuscript outputs outside the public release unless permission to publish them has been obtained.
