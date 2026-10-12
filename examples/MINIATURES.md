# Original miniature examples

All examples below are fictional and serve only to demonstrate editing choices. They are not quotations from the two exemplar papers and not new scientific findings.

## A reason before a method name

**Supplied facts:** A wake-up decision changes current transmission opportunities and future battery level. DQN is implemented, but alternatives have not been compared.

**Weak:** “We use DQN because it is an advanced algorithm and improves the system.”

**Revised:** “Wake-up decisions affect both current transmission opportunities and the energy available in later slots. We therefore use a controller that accounts for future consequences, with DQN as one implementation of this approach.”

**Why:** The temporal decision motivates a class of methods; it does not establish that one named algorithm is uniquely appropriate or best.

## A result with the right scope

**Supplied facts:** Rates of 12.4 and 10.0 bit/s/Hz; unequal CSI; no signaling deductions or significance test.

**Weak:** “The method proves a statistically significant 24% net-throughput improvement.”

**Revised:** “The reported spectral efficiency is 12.4 bit/s/Hz, compared with 10.0 bit/s/Hz for the baseline, a relative difference of 24%. The methods use different CSI, and the rates do not deduct signaling overhead.”

**Why:** The arithmetic survives; unsupported statistical, causal and net-throughput claims do not. If the task permits language changes only, flag this as a separate technical correction rather than silently changing the claim.

## A conditional design insight

**Supplied facts:** A two-link model holds marginal failure probabilities fixed and varies their joint failure probability. No channel measurement is supplied.

**Weak:** “Packet replication guarantees reliability in realistic environments.”

**Revised:** “Within the two-link model, replication provides less additional reliability as simultaneous failures become more probable with the marginal failure probabilities fixed.”

**Why:** The result identifies a mechanism under stated conditions. It does not claim measured reliability or universal validity.
