# Noise-floor calibration

Concrete recipe for step 2 of the procedure: establish how much a measurement moves when **nothing changes**, and derive the threshold from that.

## Recipe

1. Run the harness **five times** against the unchanged subject, per area/subject being gated.
2. Each run is itself the **median of three repetitions** (aggregation happens inside a run; calibration happens across runs). Require exactly five finite, positive timing values; booleans, missing values, and invalid measurement results are not samples.
3. Discard any run whose value exceeds **5× the median of the five**. Identify it by its original value or sample ID, never by a rounded display value. Log each discard and remeasure each missing sample **once**.
4. Validate again after replacement. Require five usable values and no outstanding outlier/replacement condition. A missing or still-outlying replacement blocks that area; do not accept a plausible tolerance merely because no other warning was set, and do not retry until green.
5. Only after validation, **drop the highest and lowest** and compute the relative range over the middle three: `(max - min) / min`.
6. Tolerance = `1 + range + 0.10`, floored at **1.15** and capped at **2.00**. If the result exceeds **1.5**, emit a measurement-problem finding and skip that area instead of using the number as a tolerance.
7. Exercise the actual decision consumer with the calibrated factors and area exclusions. Choose a case where the measured factor permits a candidate but the fixed fallback rejects it, and the converse boundary case. Preserve semantic neighbour checks while excluding only untrustworthy timing decisions.
8. Derive affected areas from the final applied changes, including negotiated companion changes, and expand their dependency scopes. A stored scope based only on the initiating candidate can omit a blocked dependency of its companion; skipping that area's timing then admits a change the exclusion was meant to stop. Pair a three-area negotiation case (allowed initiator, allowed companion, blocked companion-dependent) with an unchanged blocked-area control.
9. Exercise invalid samples through the calibration collector, not only the numeric helper. Preserve types until validation, and turn a per-area validation error into that area's blocked record while retaining valid areas and incurred-work evidence; a newly raised helper exception must not silently discard the whole batch.

## Why each step

| Step | Without it |
|---|---|
| median of three inside a run | a single scheduler stall becomes the run's value |
| calibrate across five runs | you measure the smoothing, not the variability |
| discard > 5× median | one container stall inflates the tolerance to absurdity, and real regressions pass forever after |
| remeasure after a discard | the sample silently shrinks and downstream count-conditioned guards switch off |
| drop high and low | a single borderline value sets the tolerance for the whole campaign |
| floor 1.15 | a perfectly stable subject would otherwise get a zero-width band and fail on the first microsecond |
| cap 2.00 | beyond this the gate cannot fail, so it is not a gate |
| report above 1.5 | that is a broken harness or a non-deterministic workload — a finding, not a setting |

## Self-check cases

Run these through the tolerance function before trusting it on real data. Each asserts one rule.

| Input values | Expected |
|---|---|
| `[1.31, 1.51, 35.22, 1.40, 1.45]` | `35.22` discarded as hiccup, remeasure flagged, tolerance ≈ floor |
| `[7.90, 8.15, 8.24, 8.31, 8.46]` | stable subject → tolerance at the floor, no finding |
| `[1.6, 1.9, 2.2, 2.5, 2.4]` | ~26 % range → tolerance ≈ 1.36, below report threshold, no finding |
| `[1.3, 1.4, 1.5, 40.0, 38.0]` | both extremes discarded, too few left → remeasure |
| `[1.0, 1.0, 1.6, 1.7, 1.2]` | ~60 % range → tolerance > 1.5 → measurement-problem finding |
| `[1.0, 1.0, 3.0, 3.0, 2.0]` | cap applies, and the cap itself triggers the finding |
| `[5.0, 5.0, 5.0, 5.0, 5.0]` | zero range → floor, no finding |

These are tolerance-function checks, not completed calibrations: an outlier case may produce a provisional number but must remain unusable until replacement succeeds. After discarding two outliers, three survivors do not meet the five-sample contract; checking whether trimming still runs is not sufficient.

Add regression cases for the validity and replacement path:

- Incomplete and oversized sample lists must not become valid calibrations merely because a range can be calculated.
- Zero, negative, non-finite, and boolean timing values must fail explicitly.
- Feed a fractional outlier whose displayed rounding differs from the original value; assert that the exact sample is removed and a replacement is actually requested.
- Return a valid replacement and verify restoration of the required sample count.
- Return a missing value or another outlier on the permitted replacement and verify that the area is blocked, its factor is withheld, and no further retry occurs.
- Test the warning threshold at equality and just above it, and the outlier threshold at equality and just above it; this proves the inequalities rather than a distant easy case.

## Sizing the calibration workload

The tolerance can exceed the report threshold because the *workload is too small*, with nothing wrong with the subject or the machine. Below roughly ten milliseconds per sample, timer resolution and scheduler granularity are a large fraction of the reading, so the relative range stays high however stable the subject is — and the calibration then blocks areas whose only defect is that they are fast.

- **Read the median before reading the range.** A blocked area whose median sits in the sub-millisecond to low-single-digit-millisecond band is a workload-sizing finding, not a subject finding. Two areas blocked at ~1.5 with medians of 1 ms and 2 ms, while slower areas on the same machine calibrate at the floor, is the signature.
- **Fix it by enlarging the workload, never by raising the threshold.** Repeat the reference load inside each `last_<area>()` until the sample lands in the tens of milliseconds. Record the repetition counts in the load file itself so the sizing is inspectable. The report threshold is the maßstab and stays untouched — same figure as "change the producer, not the limit" in SKILL.md, applied to the measuring load.
- **Scale the timing load only; leave the behaviour raster byte-identical.** Where the same reference file serves both the laufzeit measurement and the equivalence/observation checksum, these are two different jobs: `last_<area>()` must be big enough to out-measure jitter, `beobachten()` must stay small and unchanged because its output *is* the behavioural baseline. Growing both together silently moves the equivalence raster and makes every later comparison incomparable with the sealed one.
- **Re-probe standalone after resizing, before opening a gated run.** Run the identical five-measurement calibration outside any run id and publish the before/after tolerances per area with their medians, so the improvement is attributed to the sizing change rather than to a quieter machine. Call **the gate's own calibration function** (the one the run invokes), not the measurement helper underneath it: the gate adds outlier replacement, sealing, history and the verdict, and a dry-run one layer below omits exactly the logic that decides. A pre-probe on the lower layer that comes out green while the gate then blocks is the expected result of that shortcut, not bad luck.
- **Enlarging the workload alone may not clear the gate — check whether the blocked set moved.** If a second attempt blocks *different* areas than the first (rather than fewer), the instability is in the measurement procedure, not in the areas it names: an area-stable defect blocks the same area every time. Treat a shifting blocked set as the signature of a within-measurement sampling defect and go to the next section before resizing anything further.

## Within-measurement sampling

The calibration collapses repetitions inside each measurement before the spread is formed across measurements. How those repetitions are taken decides whether the across-measurement spread is the subject's or the harness's.

- **Warm up before the first timed repetition.** The first call into a function carries one-time cost — JIT compilation, first allocation, lazy module init — that is not the subject's steady-state behaviour; measured on a JS runtime: 0.98 ms on the first call against 0.12 ms on the third, an 8× difference inside one measurement. Run every area's load a fixed few times untimed, then start timing. Record the warm-up count beside the measurement count so the sample is self-describing.
- **Three repetitions is not enough to survive one stall.** A median over three tolerates an extreme only while it lands at a rank edge; a stall hitting the middle repetition becomes the measurement's value outright, and across five measurements that produces a spread with no defect anywhere in the subject. Take an odd count of at least five and take the true median of them.
- **Do not explain an across-measurement spread with a first-call effect without the ranks in hand.** A first-call outlier at rank 1 of 3 is *discarded* by the median, so it cannot be what moved the value — the outliers that move a median sit mid-rank. Check where in the ordering the extreme actually fell before naming the mechanism; the plausible explanation and the arithmetic disagree more often than not.
- **Persist the raw repetitions, not only the collapsed value.** Calibration stores routinely keep one number per measurement and drop the repetitions behind it, so the first question asked after a block — *was a cold first call involved?* — has no answer for the very run that raised it, and the only raw values left belong to some other stage. Either write the repetition list with each measurement or state plainly in the report that the raw values do not exist; do not reconstruct them from a neighbouring measurement and present the result as this one's.

## Probe construction

To test that the calibration detects instability, the injected variation must occur **between** measurements, not between repetitions inside one. Perturbing every other repetition produces five stable medians and proves nothing — the harness smoothed it away exactly as designed. Key the perturbation on the measurement index instead.

Drive the probe through the real code path (call the actual detector, supply only the inputs), so the check exercises the shipped logic rather than a parallel reimplementation of it.

Build the fixture's intervention **from the subject's own structure** (parse it and edit the parsed form) rather than from text snippets or hand-written literals. A snippet-built fixture breaks on house conventions that have nothing to do with what is being tested — a file-naming rule, a layout check, a lint gate — and the subject then rejects it for the wrong reason while the self-check records a pass.

A negative fixture must be **complete enough to reach the rule under test**. Touching only the declaration side of a contract (the specification file, the schema, the interface) is often classified as "changes nothing" and never reaches the consistency check: the fixture must also contain the consumer-side use of the new declaration, with the provider side deliberately left unimplemented. Read the recorded rejection reason of every passing negative fixture and confirm it names the rule you meant to exercise.

When a verdict depends on history as well as values, hold the values constant across the cases and vary only the history — identical inputs with different timestamps proves the timestamps are what changed the reading, which a pair of differing inputs cannot.

## Sealing the calibration subject

The probe needs something to act on. Pin it per gated system:

1. On the first run, select deterministically from what exists (e.g. largest/most-connected candidate, ties broken alphabetically) and record the choice **with its rationale and a content checksum**.
2. On every later run, verify the checksum before calibrating. Unchanged → reuse silently.
3. Changed or missing → emit a finding naming both checksums, retire the old entry with its reason, seal a replacement, and log the substitution. Comparisons across the substitution boundary are not valid and must say so.
4. No candidate exists at all → report that the calibration has no subject and stop. A self-check with nothing to check on passes vacuously, which is worse than not running it.

Anchoring a probe to source-text snippets instead of a sealed identifier is the recurring failure: any accepted change shifts the text, the probe silently retargets, and it keeps reporting success about something else.
