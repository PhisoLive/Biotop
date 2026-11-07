# Sealing a generated candidate population

For harnesses whose headline number is a detection rate over a generated set: mutation testing, fuzz corpora, injected-regression probes, adversarial banks. The number is only as honest as the order in which the set and the rate were produced.

## Order (do not reorder)

1. **Generate deterministically.** Fix the traversal order of the subject (sorted paths), fix the per-unit cap, fix the seed, and record the generator's identity with the output. A candidate set that cannot be regenerated cannot be audited.
2. **Drop no-ops.** A "mutation" whose result is byte-identical to the original is not a candidate. Compare against the current file content, not against a cached copy taken earlier in the run.
3. **Deduplicate on content, not on index.** Key on a hash of (unit identifier, produced content). Different generation rules routinely emit the same artifact, and an index-keyed set counts it twice.
4. **Screen with the real toolchain, in the real sandbox.** Compile / load / validate each candidate the way the subject is actually built. A static plausibility check is not a screen: it admits candidates the detector never gets to see and inflates the denominator.
5. **Take the first N that pass, in generation order.** Not the N that look interesting, not a random N drawn after the fact. Record how many screening attempts it took — attempts, admitted and rejected are three separate figures.
6. **Seal before measuring.** Write the admitted set, the per-candidate screening evidence, the subject's file checksums from before and after the pass, and the rate field explicitly as *not measured*. Only then run the detector.

## Rules that survive contact with a bad result

- If step 5 cannot reach N, the gate is red. Do not lower N and do not widen the generator to fill the gap after seeing the rate.
- A candidate rejected in step 4 is neither caught nor missed. Publish generated / deduplicated / screened out / admitted as four numbers, never as a two-way split.
- **Screening is not class-neutral — publish the per-class composition before and after it.** A real toolchain screen rejects some kinds of candidate far more than others, so the admitted set is a differently shaped population than the generated one, and a single headline rate over it silently answers a question nobody asked. Measured on a statically typed subject: comparison-operator mutants rejected 26 of 48 (54 %) by the type checker, numeric-boundary mutants 0 of 65 (0 %) — boundary candidates rose from 54 % of generated to 65 % of admitted while comparison candidates fell from 32 % to 22 %. Tabulate generated / screened / rejected / admitted **per class**, report the detection rate **per class**, and state the aggregate only with the skew named. When one class is heavily screened out, say that the screen and the detector overlap in what they cover rather than presenting the leftover rate as the detector's reach.
- Keep one real screener message per rejected class in the sealing record. The rejection reason is what distinguishes "the toolchain forbids this construct" from "the generator emitted nonsense", and only the first is a finding about the subject's language.
- Equivalence — a candidate that genuinely cannot be detected — is never concluded from agreement on a finite input grid alone. Missing code-level evidence stays conservatively in the denominator, and the resulting rate is published as a conservatively bounded figure, not as a statement about the whole population.
- The subject must be byte-identical before and after screening. Checksum it both times and publish the comparison; a screen that edited the subject has measured something that no longer exists.
- Screening cost is real cost. Count every sandbox or compile run against the task's ceiling, rejected candidates included.
