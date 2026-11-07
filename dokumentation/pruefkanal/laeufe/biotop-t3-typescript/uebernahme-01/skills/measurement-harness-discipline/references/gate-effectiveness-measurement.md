# Measuring a gate, filter or suppressor

For interventions whose job is to **stop things from being produced**: a duplicate blocker, a rate limiter, a
pre-flight check, a relevance filter. These are systematically mismeasured by the metric that motivated them.

## The self-defeating denominator

The metric that justified building the filter is usually a residual share among the items that were produced
("duplicates as a share of produced artifacts", "bad responses as a share of served responses"). A filter that
suppresses production removes items from that denominator. So:

- the better the filter works, the fewer items carry the number;
- at strong suppression the sample is too small to resolve the threshold at all;
- at perfect suppression the denominator is zero and the metric is undefined.

A reading of "0 % from 2 items" against a 20 % bar is not a pass. Only 0 %, 50 % and 100 % exist at n = 2 —
no outcome could have landed near the bar, so the bar was never tested.

**Keep the residual-share gate** — it is still the right acceptance criterion for the *system*, and it should be
measured on a subject where the filter is not acting on the denominator (a subject with enough genuine defects
that production continues). **Measure the filter itself on its own decisions.**

## The two numbers that do measure a filter

Both against the population of **all decisions the filter made**, not against the survivors.

| Number | Definition | Target |
|---|---|---|
| False positive | suppressed items that were not actually of the suppressed kind | 0 of n |
| Leak-through | produced items that were of the suppressed kind | 0 |

Set both targets **before** the measurement and record that they were set before; a threshold chosen after seeing
the data is not a threshold.

### Reconstructing the baseline per decision

Leak-through is where audits quietly measure themselves. The produced artifact normally writes its own key into
the same store the audit queries, so a naive "was this key already known?" check against the **end state** flags
every artifact as a repeat and reports total failure.

For each decision, rebuild the store as of that moment:

- entries that existed before the run (imports, prior history), **minus the artifact's own entry**;
- plus decisions recorded earlier in the same run, ordered by the log's sequence number.

The same applies to false positives: a suppression is correct if the key was present *at suppression time*, not
if it is present now.

**Scope the question to the whole store, not to the item's own declaration.** Having fixed the end-state trap it
is easy to overcorrect into asking only "did this artifact repeat *its own* announced key?" — a narrower question
with a different answer. Measured on the same run: zero by the narrow reading, two by the correct one, and the
narrow reading is what allowed the gate to be reported as passing. The question is always: was this key held by
**anything** in the population the gate protects, at the moment of the decision.

The figure therefore runs a characteristic path: wrong (end state) → wrong (too narrow) → right. Two compensating
errors can also make the first value numerically correct, so a revision is a fresh claim rather than a
confirmation — give each revision its own pass and fail case before publishing it.

## Separating declaration from execution

When the producer occupies an adversarial or advocacy role ("find the flaw", "argue the case"), instructing it to
abstain does not work: the role compels a finding. Measured: zero honest "nothing to report" answers across an
entire campaign despite an explicit permission to give one.

Splitting the step does work. Ask first, in a separate cheap call, **what** it intends to assert; decide
mechanically whether that assertion is wanted; only then commission the expensive work. The decision moves out
of the model. Measured after the split: roughly a quarter of calls declared nothing to assert.

Two requirements come with this design:

1. **The gate must consult both stores** — what the system already holds *and* what has been declared earlier in
   the current run. Against a freshly created subject the persistent store is empty, and without the run-local
   half the same declaration passes twice in a row.
2. **Declaration and execution must be reconciled afterwards.** The gate rules on the declared intent; nothing
   binds the producer to it. Compare each produced artifact's actual key against its declared key and publish the
   divergence rate — an unreconciled pre-declaration gate has a hole exactly the size of that rate.

## Two gates, two jobs, two metric lines

The divergence above is not a defect to be patched out of the declaration gate — it is inherent to it. A gate
sited at a declaration asks a model to state its intent and then trusts it; it can make no promise about what
ends up in the store. Rejecting whatever diverges would also discard the genuine finds the producer turned up
while working, which is a worse outcome than the duplicates.

Use two gates with different natures and measure them separately:

| | Declaration gate | Admission gate |
|---|---|---|
| Sits at | before the expensive call | at every write into the store |
| Keyed on | the announced intent | the artifact actually produced |
| Nature | best-effort, model-dependent | deterministic, a property of the core |
| Buys | saved calls, saved sandbox runs, honest abstentions | the guarantee that no repeat is admitted |
| Measured by | suppression count, false-positive rate, abstention share | leak-through (target 0) |

The deterministic gate is what the acceptance criterion should hang on; a target of zero is only reasonable for a
check that cannot vary. Leaving a zero-tolerance target on the model-dependent gate guarantees a failed criterion
for reasons nobody can fix.

**Wire the admission gate into every write path.** Secondary intakes — the "rejected but retained" bucket, a
quarantine or norm category, anything filed as not-counting — usually still deposit a key that later decisions
read against, so an artifact arriving there is downstream indistinguishable from one admitted through the front
door. Measured: half the leak-through entered through exactly such a side path while the primary path was clean.
Enumerate the write sites in the code before calling the gate complete.

**A reconstruction is not a measurement.** Replaying a finished run's records against the new gate shows that the
mechanism would have caught the known cases — useful, and worth publishing — but it is not the gate running in
the live path, and the calibration cases it yields are constructed, not observed. Say which of the two you have;
the acceptance criterion asking for cases "from the real run" is not satisfied by a replay.

## Calibration cases from the real run

A filter measurement needs one case of each kind, and the strongest pair is the **same key at two points in
time**: first occurrence must pass, later occurrence of the identical key must be suppressed. Prefer such a pair
from the production log over an injected one; injected cases prove the wiring, real pairs prove the behaviour.

If only green cases exist, the measurement is not yet evidence — a filter that never fires and a filter that is
switched off are indistinguishable from green rows alone.

## Cost accounting

A pre-declaration gate costs one cheap call per decision and saves one expensive call per suppression. Report:

- cost per gate decision and cost per suppressed operation, both measured, not assumed;
- the balance in money **and** in sandbox runs / wall time separately — a gate can be money-neutral and still a
  clear win in runtime, and the ratio flips once the suppressed operation uses a more expensive model.

A negative money balance is not an argument against the gate until the runtime figure is stated beside it.

## Separating declaration from execution

When the producer occupies an adversarial or advocacy role ("find the flaw", "argue the case"), instructing it to
abstain does not work: the role compels a finding. Measured: zero honest "nothing to report" answers across an
entire campaign despite an explicit permission to give one.

Splitting the step does work. Ask first, in a separate cheap call, **what** it intends to assert; decide
mechanically whether that assertion is wanted; only then commission the expensive work. The decision moves out
of the model. Measured after the split: roughly a quarter of calls declared nothing to assert.

Two requirements come with this design:

1. **The gate must consult both stores** — what the system already holds *and* what has been declared earlier in
   the current run. Against a freshly created subject the persistent store is empty, and without the run-local
   half the same declaration passes twice in a row.
2. **Declaration and execution must be reconciled afterwards.** The gate rules on the declared intent; nothing
   binds the producer to it. Compare each produced artifact's actual key against its declared key and publish the
   divergence rate — an unreconciled pre-declaration gate has a hole exactly the size of that rate.

## Keys and matching

Derive the key from the substance (target function plus kind of assertion, extracted from the syntax tree), never
from the location or the name. Filter out incomplete keys — a key with an empty half matches indiscriminately and
suppresses unrelated work.
