# Communications claim and evidence checks

Apply the checks relevant to the claim; this is not a mandatory experiment list. Detect inconsistencies and unsupported claims without claiming to certify an entire proof or implementation.

## System and information model

- Identify transmitter/receiver roles, direction of communication, time/resource structure, channel and interference model, synchronization and hardware assumptions where consequential.
- State who observes which CSI, traffic state or feedback, with what error and delay. Distinguish instantaneous, statistical, imperfect and unavailable information.
- Distinguish physical assumptions from analytical simplifications. A simulation with a more detailed model does not change the assumptions of a theorem.
- Name decision variables, domains, constraints and objective. Clarify averages versus instantaneous limits and long-term versus per-slot constraints.
- Check units, dimensions, logarithm base and normalization; distinguish linear SNR and dB. “Power,” “energy,” and “energy efficiency” are not interchangeable.
- Define arrival and service assumptions when analyzing queues or random access; finite-user/binomial, Poisson and backlogged models are not interchangeable.
- For a deployable rule, identify how its required state is obtained. Label perfect-information policies and optimal-load targets as oracle or ideal references when appropriate.

## Mathematical claims

Preserve every material quantifier and condition. Check the original expression before changing its prose.

| Distinction | Writing consequence |
|---|---|
| Exact / approximate / asymptotic | Name the type and the limiting variable; do not erase approximation error or regime |
| Upper / lower bound | Preserve direction and metric; improvement in a bound is not automatically an improvement in achieved performance |
| Achievable rate / capacity | Capacity requires the claimed matching converse or established characterization; an achievable construction alone is insufficient |
| Sum-rate / per-user rate / fairness / outage | A gain in one does not establish a gain in the others |
| Average / per-realization / high-probability / worst-case | Retain the relevant expectation, event or quantifier |
| High-SNR diversity order / finite-SNR error probability | Diversity is an asymptotic slope, not a complete finite-SNR ranking |
| Objective convergence / iterate convergence / stationarity / global optimum | Claim only the property actually established |
| Convex subproblem / convex original problem | Solving a surrogate exactly does not certify the original nonconvex optimum |
| Feasible method / infeasible relaxation / oracle | Distinguish deployable comparisons from performance references |

For an inspected theorem, state what was checked: assumptions, algebraic steps, proof strategy, a limiting case, or the whole supplied proof. Flag a missing justification specifically. Do not infer validity from plausible notation or call simulation a proof. Conversely, lack of simulation does not invalidate a mathematical result.

Do not demand closed form for its own sake. A computable integral, recursion, bound, or characterization can answer the question. Do not strengthen “sufficient” to “necessary and sufficient.” Preserve probability-zero exceptions and ranges of parameters when they matter.

## Algorithms and optimization

- Connect each major operation to the obstacle it addresses. Do not invent post-hoc explanations or claim the method is the only possible solution.
- Check initialization, update information, constraint handling, stopping criterion and failure/edge cases when reviewing implementability.
- Separate per-iteration complexity, number of iterations and total measured runtime. State dependence on dimensions; do not infer wall-clock speed from asymptotic complexity alone.
- Mark centralized information, signaling, pilot, feedback, computation and training costs if they affect the comparison.
- For alternating optimization/SCA/relaxations, identify the proved convergence or feasibility property and any recovery gap. A monotone bounded objective sequence does not by itself prove convergence of iterates or global optimality.

## Learning-based work

- Identify inputs and outputs at training and deployment. Training labels or simulator state may be unavailable online; do not quietly include them in the deployed information budget.
- Describe separation between training, validation and test conditions. Check leakage across related channel/trajectory/user samples when relevant.
- Compare at matched information and resource budgets; report offline training cost and online inference cost separately when making efficiency claims.
- Distinguish in-distribution performance, tested distribution shifts and untested generalization. One channel model does not establish generalization to arbitrary environments.
- Attribute benefit carefully: compare against relevant analytical/optimization baselines and isolate claimed design choices when feasible. Ablation is useful only when it tests an actual component claim.

## Simulations, measurements and comparisons

For a comparative statement recover the metric, units, comparator, operating range, budgets and evidence location. Use a compact comparison table only when needed.

- Match material resources: bandwidth, antennas, time slots, transmit/received power constraints, training/pilot/feedback overhead, coding/blocklength, receiver capability and state information as relevant.
- Distinguish ideal bounds from executable baselines; neither should be silently treated as the other. Identify tuned versus untuned baselines if it affects the conclusion.
- Define throughput units and accounting: bits/s/Hz, successfully delivered packets/slot, and attempted transmissions measure different quantities. Reliability, latency, fairness and energy are separate objectives.
- A percentage gain needs a denominator and matched point/range. Percentage points differ from relative percent. Do not infer precise values from an unread figure; identify digitized values as approximate.
- Agreement of analysis and Monte Carlo tests model/implementation consistency in tested conditions; it is not universal proof or validation of all real-world assumptions.
- Explain mechanisms only to the extent supported by analysis or interventions. Label plausible interpretations as such; correlation or a curve shape alone does not establish causality.
- For random results identify repetitions, seeds, variability measure and evaluation unit if available. Do not invent confidence intervals or p-values. Overlap of error bars alone establishes neither significance nor equivalence; define the bars and use the appropriate actual analysis before making inferential claims.
- Include adverse regimes, model mismatch, saturation and trade-offs when they delimit a headline claim. Do not conceal a conclusion-changing counterexample in an appendix.

## Evidence allocation and reproducibility

Keep the minimum sufficient argument in the main text: central assumptions, theorem statements, decisive evidence and material limitations. Proof details, extended sweeps and implementation details can move to permitted appendices/supplements without breaking that chain. Check the venue and submission stage before relying on supplementary material.

If inputs are incomplete, propose the specific test or clarification that would resolve the claim. Label it as proposed. Reproducibility details should identify enough parameters, algorithms, sources and evaluation settings to interpret the result; do not demand irrelevant parameters for a purely theoretical statement.

Finish by asking internally: Does the wording assert the right property, for the right model, at the right level of certainty? Repair that before improving stylistic force.
