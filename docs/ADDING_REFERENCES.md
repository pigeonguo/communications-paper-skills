# Extending the reference set / 补充材料的方法

Add a source to fix a diagnosed weakness or expand a missing paper type. A larger PDF collection is not itself a better skill. The files here define instructions; they do not train model weights.

## Start with a failure

| Observed weakness | High-value material | What to extract |
| --- | --- | --- |
| Theorems appear as a list without meaning | A theory paper with clear explanations before and after results | Question answered, conditions, proof idea, consequence and limits |
| Methods appear before their reasons | An algorithm paper with a strong problem-to-design progression | Which obstacle motivates which design choice; reasonable alternatives |
| Results repeat figure values without interpretation | An experimental or systems paper with convincing comparisons | Test question, matched budgets, uncertainty, explanation and deployment scope |
| A short paper loses its argument during compression | A concise ICC/GLOBECOM paper or permission-cleared long/short pair | What remains essential and what can be moved or removed |
| The writing remains hard to read | An anonymized original paragraph, expert revision and explanation | Specific sentence or paragraph changes and the problem each resolves |
| The skill overstates novelty | Closest primary literature and a corrected positioning paragraph | Precisely scoped prior achievement and remaining question |

These are material-selection heuristics, not empirical guarantees. One carefully explained revision can diagnose a failure better than several unrelated papers.

## Minimal annotation record

For each source, record:

1. **Identity and access:** title, authors, venue/year, DOI or public URL; which sections were actually read.
2. **Located move:** section, paragraph opening or figure; use a short excerpt only if necessary and permitted.
3. **Reader's question:** what the reader needed to understand at that point.
4. **Technique and effect:** what the authors did and why it helped, in your own words.
5. **Transfer boundary:** which paper types and evidence conditions make this useful; where it would be misleading.
6. **Proposed change:** one conditional rule and its destination file.
7. **Transfer test:** a new topic plus a case where the rule should not apply.

Do not automatically append every new source to the always-loaded entry file. Update the relevant module or exemplar reference and keep provenance separate from instructions.

## A practical next round

For the current version, the highest-value next test is a real, anonymized storyline or Introduction that was not used to write the rules. Keep an expert revision or comments hidden while generating two candidates under matched conditions. Ask a human to compare factual fidelity, causal flow, readability and editing effort before revealing which condition used the skill.

Then add only the material that addresses the observed weakness. If no failure is apparent, diversify with one theory and one experimental example and check whether the existing rules transfer. Four to six additional papers is an optional coverage plan, not a minimum or a claim that performance improves with paper count.

Keep development material separate from held-out evaluation material. Once an example has shaped the rules, it no longer provides an independent test of transfer. Preserve unfavorable outputs as well as favorable ones.

## 中文操作建议

先用现有版本改一段真实稿件，再判断最费人工修改的是哪里。若是故事线，给“原稿—修改稿—原因”；若是定理的动机与意义，给一篇理论范文；若是结果解释，给一篇比较设计清楚的实验论文。

每次只提炼几条有适用条件的规则，并在另一个主题上检查。用来提炼规则的材料和用来验收的材料分开。不要把一篇范文中的段落数量、贡献数量、算法名称或句式提升为所有通信论文必须遵守的格式。

私人稿件、导师批注和审稿信应留在私人测试中。公开仓库只收录已获许可的内容、匿名化片段或原创合成例子；参考文献可保留引用和原创分析，无须附全文 PDF。
