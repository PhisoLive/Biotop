# Self-check battery

Use this procedure before trusting a measured decision or a repaired harness. A candidate rejected by the system and a calibration assertion returning false are different observations: prove both sides of the assertion, not merely that rejection is possible. Measure the battery's cost; do not infer sandbox runs or model calls from the number of probe names.

## Ordered procedure

1. **Pin and isolate the subject.** Record its identity and checksum. Use a private database/work copy for probes that can write; preserve the real population and exclude explicitly marked fixtures from learning stores.
2. **Define the exact assertion.** Name the rule, observation, and required result fields. Require evidence that the intended path executed. For a norm check, require the identified test's norm classification, zero credited gain, and exclusion from the admitted test set; an empty norm list proves none of these.
3. **Construct a probe and a countercase for each assertion.** The probe must make the assertion true; the countercase must make that same assertion false. Keep unrelated prerequisites valid and vary the property under test. A countercase need not be accepted by the entire system: it must lack the specific mechanism asserted by this calibration check.
4. **Check structure before meaning.** Access required fields explicitly and validate their types and evidence cardinality. Missing result objects, misspelled keys, absent numeric values, and empty required observations must fail closed, not fall through to `{}`, `[]`, or zero defaults. Test these malformed-result cases separately from valid negative controls.
5. **Execute both cases through the shipped checker.** Keep `executed/valid` distinct from `verdict`. An unexecuted probe, setup failure, missing subject, or infrastructure exception cannot satisfy the expected-false control. Capture command, return code, stdout, stderr, and machine-readable test results. Read the mechanism in both outcomes.
6. **Verify the suite from the repository root, with consequential regressions first.** Prioritize scoring rules and per-item regression checks that caused costly historical failures before ancillary checks; verify the collected order rather than relying on filenames. Run the focused repair test red then green, then the complete suite. A larger green-test count never substitutes for the required executed probe/countercase pairs. Report unit checks, real sandbox executions, stored-data replays, and new natural runs separately.
7. **Account for all attempts and publish the evidence.** Keep the latest acceptance result per probe while retaining every attempt's raw output and charged cost. Release no campaign on a partial, invalid, or missing pair.

## Four paired probes

Run side-effect before regression because the latter reuses its damage.

| Assertion | Probe: assertion must be true | Countercase: assertion must be false |
|---|---|---|
| Side-effect detection | Improve one area and damage another; verdict names the damaged neighbour | Remove that neighbour damage while keeping the fixture valid |
| Individual regression detection | Add passing checks while breaking a named previously passing check; verdict names that exact check | Retain the passing additions without breaking the existing check |
| Norm/opinion exclusion | A test fails before and passes after, but proves neither a subject crash nor a declared-contract violation; it is explicitly classified as norm and not credited or admitted | Use a valid crash- or contract-backed case that must not be classified as mere norm |
| Contract enforcement | Change the boundary guarantee and consumer use without adapting the provider; verdict names the contract rule | Supply the matching adaptation so that this specific contract violation is absent |

Do not implement countercases by negating a cached success flag or by feeding malformed fixtures. Prove that the input changed the targeted condition and that the same checker ran again.

### Building executable named-target witnesses

1. Verify that the original consumer passes on the unchanged baseline, then select an existing test that actually exercises the intended consumer. Reject unsupported fixture contexts explicitly rather than guessing how to call them.
2. Preserve the test's full module context in a separate namespace. For a parameter-free, undecorated test, a generated wrapper can call `runpy.run_path(test_path)[test_name]()` **inside the existing test sandbox**. Do not load foreign test modules on the host during AST inspection. Copying only imports and the function loses constants/helpers; pasting all globals into the contract can overwrite its names or invalidate future imports.
3. Execute both the consumer and the generated, specifically named contract through the shipped JUnit path for the unadapted and adapted variants. Retain the exact test identities and raw outcomes; do not substitute a parallel parser or the aggregate verdict.
4. Validate the named witnesses before evaluating the shared predicate. The positive witness must identify the intended subject/contract violation; the countercase must actually execute and pass that same target. An `all(...)` becoming false because the consumer recovered while the contract still crashes is not a repaired control.
5. Exercise setup errors, collection errors, skipped/xfail targets, missing targets, and missing witness fields separately. Absence of JUnit failure/error is not execution: preserve `<skipped>` explicitly and prove that a genuinely skipped named target is rejected through the original parser and validity consumer. Keep these cases invalid/unexecuted as appropriate, never successful negative controls. Use a disposable validator mutant to establish the sensitivity of added characterization tests, without claiming those tests preceded the fix.

## Building valid probes

- Derive edits from the syntax tree and the sealed subject, not source-text anchors; accepted rewrites otherwise silently retarget the check.
- Obey the subject's naming and layout conventions; unrelated validation failures can make a negative test falsely green.
- Include the consumer-side use in a boundary-change probe; changing only the declaration may be rejected as a no-op before the contract rule runs.
- Mark fixtures at creation and enforce their exclusion at learning-store write points; names alone do not prevent contamination.
- Preserve source and database before/after evidence; exercising a real rule against a real store can otherwise alter the population being audited.
- Build norm witnesses against an already importable function or method, not a function introduced by the candidate; a baseline import failure never proves the opinion-classification path. For a zero-default bug, also run the same behaviour change without presenting a norm test to the classifier: an explicitly measured zero and absent norm entry must produce false even when external witnesses still run.
- Validate a countercase's prerequisite witnesses even when its later measurement deliberately omits their test. A valid downstream measurement cannot retroactively prove that the earlier before/after witness pair ran; skipped, removed or aborted prerequisites must invalidate the countercase itself, separately from its expected-false verdict.
- Check cross-area fixture gains after dependency propagation, not before it. Provider damage can erase a consumer gain; strengthen the isolated baseline fixture and keep the exact gain/loss predicate, rather than relaxing it or silently changing the sealed pair.
- Preserve the full canonical identity of every compared test, including its relative module path, class hierarchy and parameter identity. Exercise two classes with identically named methods: fixing one while breaking the other must remain a new regression even if the total failure count falls. A basename-and-method key can erase that regression from a set comparison.
- Require failure-location evidence before classifying an exception as a subject crash. Error/Exception words in failure text do not distinguish a test-internal NameError from an exception inside the subject. Keep the executed failure, its validity as a witness, and any resulting status promotion separate; a synthetically proved wrong flag is not proof that a real stored record was promoted.

## Discoverable tests and sensitivity checks

For pytest projects, keep tests of the harness separate from embedded tests of the subject and from historical runner scripts. An explicit root configuration can contain:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
```

Use the project's test interpreter with `terminal`, for example:

```python
terminal(command="<test-python> -m pytest --collect-only -q", workdir="<repository>")
terminal(command="<test-python> -m pytest tests/test_gate.py -q --junitxml=<evidence-dir>/red-01.xml", workdir="<repository>")
terminal(command="<test-python> -m pytest tests/test_gate.py -q --junitxml=<evidence-dir>/green-01.xml", workdir="<repository>")
terminal(command="<test-python> -m pytest -q --junitxml=<evidence-dir>/suite-01.xml", workdir="<repository>")
```

Assign each runner an explicit working directory, import path, and temporary root; this prevents inherited worker settings from mixing code copies or evidence. Use distinct filenames for every attempt and retain stderr, not just the test summary. Isolate database writes and paid-call boundaries, including subprocesses used by tests.

For already-correct behaviour, label newly added tests as characterization rather than claiming a bug-repair red phase. Test their sensitivity with a small deliberate code mutant in a disposable source copy. Require an assertion failure for the intended rule, not a collection/import error, then verify that the original source is unchanged. A unit double or constructed mutant proves only the exercised mechanism; it does not substitute for a real-stock or natural-run acceptance criterion.

## Integrating independently built gates and probes

- Verify the delivered manifest and each changed file's base checksum before applying a patch; accept only an explicit path allowlist. Apply the test portion first with `git apply --check --include='<test-path>' <patch>` followed by the same command without `--check`; reproduce the intended assertion failure with the parent's interpreter and import path. Then apply only the approved product portion, rerun that exact test green, and compare the integrated bytes with the delivery. This proves both applicability and the red/green transition at the integration boundary, rather than trusting a child's isolated result.
- Merge optional model-free probe branches without dropping the normal path's provenance arguments (candidate IDs, current-declaration IDs, admission context). Re-run the real paired probes and the stored-data replay against the combined source tree; isolated green suites do not prove compatible integration.
- Re-run deliberately damaging positive probes when strengthening execution-validity guards. A new guard can correctly invalidate their setup or requested reference workload even though its own isolated tests pass. Preserve the required true verdict and the execution rule, report the integration failure, and stop at the owner's retry limit; do not turn an unmeasurable positive into a successful negative control or quietly choose another subject. Distinguish the observed blocking reason from an isolated root cause.
- Exercise the real CLI gate once on a fresh private run with the actual calibration, reclassification and paired probes. Keep model networking disabled, count sandbox calls at the execution boundary, reconcile them with the gate ledger, and verify the resulting next-stage permission. Label mocked lifecycle tests separately; neither those nor a probe-only battery demonstrates the complete gate.
- Require semantic prerequisite success, not merely a completion event. Check the relevant latest attempt, a positive denominator, and consistent achieved/target counts; an earlier success must not hide a newer failed or unfinished attempt. Pair a failed-prerequisite route that cannot freeze or write downstream with a genuinely successful route.
- Revalidate the sealed subject's current identity and bytes at pre-freeze entry points, not only when the calibration ends. A valid historical hash chain does not prove the present file still matches it. Keep this prerequisite binding distinct from legitimate later, explicitly accepted evolution so the guard does not ban normal changes indiscriminately.
- Preserve both the full-suite sandbox count and the narrower battery count. A suite includes setup, witness and repeated fixture executions; its total must not be relabeled as the number required by one gate or one battery.

## Accounting and release

Apply the scope rule in SKILL.md to the delivery: retain the owner's decision, map every earlier finding to a current blocker or an explicitly unresolved backlog entry, and state the exact boundary of the new review. Report technical execution, independent review, and final sealing as separate completion states; a green parent suite does not imply that the latter two have finished.

Keep the search boundary separate from the repair boundary. A wide inventory does not authorize fixing every match: trace each proposed change to the retained core's execution or result-consumption path, quarantine out-of-scope partial fixes, and keep confirmed outside findings on a named unresolved follow-up list with their original evidence. Separate unverified source hints from confirmed findings. Report completed, uninspected and interrupted search coverage explicitly; an empty finding set from an incomplete search cannot support an absence claim.

Sample sandbox, model-call, cost, and elapsed-time counters around each probe/control pair, including nested calls. Keep calibration and campaign subtotals distinct, but include both and every retry in the hard task budget. Replacing a displayed result must never erase a charged attempt.

Report probes reaching the expected true verdict, controls reaching the expected false verdict, and invalid/unexecuted cases as separate populations with denominators. Read every recorded reason before declaring the battery complete. Preserve failed development attempts and name their cause; do not present a corrected run as the first attempt.
