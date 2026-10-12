**Reviewer 1, Comment 2**

> The method assumes perfect CSI, but the claimed robustness is not justified. Please include imperfect-CSI experiments.

**Response:** Thank you for highlighting this issue. We agree that results obtained under perfect CSI do not justify a claim of robustness to arbitrary channel errors. We have therefore replaced the phrase “robust to arbitrary channel errors” in the Abstract with wording that explicitly states the perfect-CSI assumption. The revised sentence reads:

> The algorithm improves the simulated sum rate under the assumed perfect CSI.

We have not conducted imperfect-CSI experiments, and the current results do not establish the method’s robustness to CSI errors. The revised abstract limits the performance claim to the assumed perfect-CSI setting. We acknowledge that this correction addresses the unsupported claim but does not provide the imperfect-CSI evaluation requested by the reviewer.

**Reviewer 1, Comment 3**

> Clarify the computational complexity and avoid calling the method real-time without runtime evidence.

**Response:** Thank you for this comment. We have added the following statement to Section IV-C to clarify the per-iteration computational complexity:

> Each iteration requires O(K^3) arithmetic operations, where K is the number of users. No wall-clock runtime measurements are available.

This complexity statement describes the arithmetic cost of a single iteration; it does not establish the total execution time or real-time capability. Since no wall-clock runtime measurements are available, we have removed the term “real-time” throughout the manuscript.

使用说明：以上已写成英文回复信正文。Comment 2 中的摘要修改和 Comment 3 中的复杂度表述依据你提供的摘录；全文删除 “real-time” 依据你的完成说明，尚未独立核查全文。未承诺开展尚未决定的实验，也未把 imperfect-CSI 实验请求表述为已经解决。位置暂用 Abstract 和 Section IV-C，未虚构页码。提交前仍需决定如何处理 Comment 2 的实验请求，并核对全文修改及最终页码。
