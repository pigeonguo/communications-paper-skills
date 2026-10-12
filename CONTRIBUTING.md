# Contributing

Prefer a focused change motivated by a concrete writing failure. Open an issue with the task, the observed problem and the desired behavior; provide only text you have permission to share.

## Development workflow

1. Read `skills/communications-paper/SKILL.md` and the reference relevant to the change.
2. Identify whether the proposed rule is a general workflow, a paper-type option, an exemplar observation, a current venue requirement or an author preference. Keep these categories distinct.
3. Edit the narrowest appropriate file. Keep the entry file short and avoid repeating instructions across references.
4. Add an original, synthetic or permission-cleared input demonstrating the failure. Include a case on another topic and, where relevant, one where the rule should not apply.
5. Run `python3 scripts/validate.py` after installing `requirements-dev.txt`.
6. For behavioral changes, run the affected drafting tasks in fresh sessions and inspect the actual outputs. Do not give the generation session a scoring rubric, intended answer or earlier output.
7. Describe the change, evidence, remaining limits and any regression in the pull request. Update the changelog for a released change.

Do not publish manuscript drafts, reviewer identities, private comments, full copyrighted papers or credentials in examples or issue reports. A paper's published status does not authorize copying its full text into this repository. Prefer a citation plus original analysis and a short located excerpt only when necessary and permitted.

## Review expectations

- Preserve evidence type, notation, citation keys and requested editing scope.
- Avoid turning a successful example into a universal manuscript template.
- Do not claim a rule improves acceptance chances or guarantees mathematical correctness.
- Keep tests representative. A script detecting phrases cannot grade causal reasoning or scientific validity.
- Record model/session details when known; mark unavailable details as unknown instead of inventing them.
- Keep runtime dependencies out of an instruction-only skill unless a task clearly requires them.

Contributions are made under this repository's Apache-2.0 license. Third-party sources retain their own rights.

## 中文简要说明

一次修改解决一个可复现的问题。提交“问题输入—原来哪里不好—修改了哪条规则—换一个题目后的结果”，比追加大量抽象要求更有用。涉及真实文稿时先匿名化并确认可以公开；导师批注和审稿信不默认属于可公开材料。不要为了让测试通过而把标准答案交给执行测试的助手。
