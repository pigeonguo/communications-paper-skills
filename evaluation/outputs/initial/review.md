根据你提供的数据，**24% 的相对差值计算正确**：$(12.4-10.0)/10.0=24\%$。但目前能保留的是特定设置下的报告值差异，原文对净吞吐量、统计显著性和泛化的判断均超出了证据。以下自审仅依据作者提供的信息，未独立复现实验，也未查询外部文献。

最重要的问题是：

1. **CSI 信息预算不一致。** 原文将差值归于 “Our method”，但 ours 使用瞬时完整 CSI，baseline 仅使用统计 CSI。相同带宽、天线数和发射功率并不构成信息条件一致的比较，不能据此把 24% 全部归因于算法设计。当前稿应明确两者的 CSI 条件；如需隔离算法贡献，可补充相同 CSI 条件下的比较。
2. **“net throughput” 与实际计量不符。** 两者均未扣除 pilot 和 feedback 开销，现有数值不能称为净吞吐量。以 bit/s/Hz 为单位，宜表述为“未计开销的和频谱效率”，并保留该限定。两种 CSI 方案的获取成本可能不同，不能假设扣除开销后仍有 24% 增益。
3. **“statistically significant” 缺少支持。** 每个方法仅运行一个随机种子，且没有不确定性量化或统计检验。24% 是所报告数值的相对差异，不能替代显著性证据。当前删除显著性措辞；若需恢复该结论，应补充独立重复运行及适当的统计分析，并明确独立评价单位。
4. **“proving its generalization to unseen wireless environments” 不成立。** 全部样本来自同一个信道模型，未提供跨环境测试；随机划分样本也不能排除同一 trajectory 的相邻样本跨训练集、测试集而造成相关性泄漏的风险。这是待核查风险，不能直接断言已经发生泄漏。当前结果不足以建立独立轨迹上的泛化能力，更不能证明对未见环境的泛化。可先按 trajectory 隔离数据重新评估；若要保留跨环境结论，还需明确的环境变化测试。
5. **“state-of-the-art” 未得到所给材料支持。** 当前无法核实该基线的领域地位，修订稿使用 “the baseline”。

可用的英文 Results 段落：

> Under the same bandwidth, antenna count, and transmit power, the proposed method and the baseline yield reported sum spectral efficiencies of 12.4 and 10.0 bit/s/Hz, respectively, corresponding to a relative difference of 24%. These values exclude pilot and feedback overhead and therefore do not represent net throughput. The proposed method uses full instantaneous channel state information (CSI), whereas the baseline uses only statistical CSI; thus, the observed difference cannot be attributed solely to the resource allocation method. Each method was evaluated using a single random seed, with no reported uncertainty estimates or statistical tests to establish significance. All samples were generated using the same channel model and randomly split into training and test sets. Because adjacent samples from the same trajectory may appear in both sets, the split may introduce dependence between training and test data. The reported values therefore describe performance under the evaluated setup, but do not establish generalization to independent trajectories or unseen wireless environments.

上述修订保留了数值及其可复核的相对差异；建议的额外实验均未被写成已完成的工作。
