# Introduction

Delivering a packet before a deadline requires more than a high average link success rate. A packet sent over one wireless link can miss its deadline when that link fails, while sending the same packet over two links gives the receiver a second opportunity for timely delivery. This protection has a cost: replication consumes an additional transmission opportunity for the same packet. The relevant question is therefore when the reliability improvement from replication is large enough to justify its transmission cost under a given budget.

The answer depends on how the two links fail together. Shared obstacles can make failures co-occur, reducing the protection offered by a second copy. Consequently, a reliability calculation based on independent failures may overstate the benefit of replication when such dependence is present. Even with the individual link failure probabilities held fixed, different probabilities of simultaneous failure can lead to different reliability benefits. A transmission decision must account for both this joint behavior and the resources available for each packet.

Existing analyses provide useful foundations for this question. The work in \cite{independent_replication} analyzes replication reliability under independent link failures. The work in \cite{correlated_reliability} characterizes correlated failures for a fixed replication configuration, but does not optimize selection under a per-packet transmission budget. These two perspectives motivate examining reliability evaluation and transmission selection together. Our focus is the specific decision between a single-link transmission and two-link replication when the marginal and joint failure probabilities are known and the expected number of transmissions per packet is constrained.

We consider one-shot packet replication within a common deadline. The setting excludes retransmission protocols such as HARQ and does not model queues. The decision can be randomized, allowing the transmission budget to govern how frequently replication is used rather than requiring every packet to receive the same treatment. Within the supplied two-link joint failure model and this restricted action set, the objective is to maximize the probability of delivery by the deadline. The contributions are as follows.

1. We derive the deadline success probability for the supplied two-link joint failure model with known marginal and joint probabilities. This analysis relates the reliability benefit of replication to the probability that both links fail within the deadline.

2. We obtain a selection rule between single-link transmission and two-link replication that maximizes deadline success probability subject to an expected number of transmissions per packet. The rule allows randomized selection, and its optimality is confined to the stated probabilistic model and action set.

3. We evaluate the rule numerically for three values of the joint failure parameter. The results illustrate how the transmission budget determines feasible selection and how the marginal reliability benefit of replication decreases as co-occurring failures become more probable while the marginals remain fixed.

The resulting analysis connects the cost of an additional transmission to the reliability protection it provides under correlated failures. It offers a model-specific basis for deciding how often to replicate packets within an expected transmission budget.

**Author note:** Before submission, supply the joint model, derivation and optimality proof, numerical parameter values and results, and verification of the cited characterizations and broader related-work coverage.
