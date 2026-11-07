# Read-only inventory and historical reconciliation

Use when the deliverable is an independently measured inventory, not another campaign or a replay of prior completion reports. This procedure covers source size, test populations, operational evidence and evolving ledgers.

## 1. Pin the two questions: which state, which population?

- Record the requested historical boundary separately from the actual current source revision, dirty state and collection timestamp. Through `terminal`, use `git -C <repo> rev-parse HEAD` and `git -C <repo> status --porcelain=v1`; retain both outputs.
- Identify the primary databases and earlier manifests/ledger exports before collecting numbers. Prefer preserved row IDs or a snapshot over a narrative subtotal.
- Do not silently roll the current system back to make it resemble the requested earlier state. Read the historical revision separately and label current and historical evidence throughout.
- When parallel repair changes the working tree during a historical audit, preserve the drift rather than reverting it. Pin source evidence to Git blobs and report the frozen database separately; an unchanged HEAD does not mean an unchanged working tree.
- Bound event-to-record joins by the record's creation/lifetime as well as its ID. Deleted fixtures can free numeric IDs for reuse while their append-only events remain, so an earlier abort bearing the same ID may belong to a different object.

## 2. Make observation non-mutating

- Inspect application connection helpers and check scripts with `read_file` before importing or executing them. Constructors can create schemas, enable journals or seed accounts; test cleanup can stop a process while leaving changed credentials or real records behind.
- Capture file hashes/mtimes and consumption counters before collection. Keep audit code, exports and scratch copies outside the measured repository.
- Open SQLite directly with `sqlite3.connect('file:' + str(db_path) + '?mode=ro', uri=True)`. Use its backup API into a private scratch database when consistent repeated queries are needed; query that copy read-only. Do not substitute a raw copy of a live main file for a WAL-consistent snapshot.
- Treat SQLite read-only as a database access mode, not a promise of unchanged filesystem metadata. A WAL-mode read can touch a `-shm` file's mtime while its bytes, the main database and the logical rows remain unchanged. Compare existence, size, hash and timestamps separately before/after, disclose any metadata-only delta, and never restore timestamps merely to manufacture an unchanged-state claim.
- If importing a proven read-only function, disable bytecode writes (`python3 -B`) and pass it the read-only connection explicitly. Reuse the original derivation rather than implementing a second approximate checker.

Completion criterion: the measured state and private snapshot are identified, and no inspection helper has acquired an unintended write path.

## 3. Count mutually exclusive populations

- Enumerate tracked source with `git -C <repo> ls-files -z`, parse the NUL-delimited output in Python, and save one row per file before aggregating. Treat tracked files as one defined population, not as proof that no untracked source exists.
- Partition the full filesystem separately: own tracked files, untracked source, dependencies, generated files/caches, nested Git internals, subject copies, archives and database sidecars. Count a path in exactly one category. Do not inflate authored scope by adding snapshots and their extracted copies.
- State the line metric. `len(text.splitlines())` counts physical lines including a final unterminated line; tokenizer-derived code/documentation lines are a different metric. Preserve both rather than calling either simply "LOC".
- Report database main-file length, WAL and SHM lengths separately. Distinguish logical length from allocated blocks; record table counts and integrity-check output without publishing authentication tables.

Completion criterion: every per-file and per-table breakdown recomputes to its declared total, with unreadable paths and excluded populations explicit.

## 4. Inventory tests and operating state without manufacturing evidence

- Classify tests by what they exercise: the system itself, the subject it improves, or the audit harness. Count generated test source inside strings separately from actual collected test cases.
- Inspect setup first, then run collection only in an isolated environment where imports cannot modify the original database or source. For pytest, capture command, stdout, stderr and return code for `python -m pytest --collect-only -q -p no:cacheprovider <target>`.
- Interpret pytest exit 5 with clean collection output as no tests collected in those targets. A nonexistent or inaccessible target is a setup failure, not the same finding. Print-only examples remain examples even when their command exits zero.
- Map each conceptual component to its implementation and reachable entry point. Use event IDs for historical exercise and live process/service/port evidence for current operation; attach a timestamp and scan denominator. Never start an inactive service merely to support the claim that it was running at the inventory cutoff.
- Before calling a helper dead, inspect imports, CLI dispatch, scripts and dynamic entry points. Distinguish superseded-but-manually-callable code from code with no observed caller in the inspected population.

## 5. Reconcile changing ledgers before explaining discrepancies

1. Export individual rows with their IDs, run/section IDs, timestamps, purpose, amounts and request linkage. Retain the query and use `Decimal(str(stored_amount))` for repeatable summation; this is arithmetic on stored values, not independent verification of an invoice.
2. Recover each historical report's membership from its explicit IDs or cutoff snapshot. If only per-run counts survive, an earliest-row reconstruction is a hypothesis: validate available IDs, dates, purposes and subtotals, and still label its limits. Do not present a rounded match as proof of the exact historical population.
3. Form historical, later and current sets. Verify historical plus later equals current for both row count and amount. Publish added-row IDs and purposes; do not silently reassign old charges to make section budgets agree.
4. Compute the sum of rounded section totals and the rounded sum of raw rows separately. Show the rounding residual independently of the later-booking delta. Do not call the whole discrepancy rounding when the row sets differ.
5. Reconcile request attempts against booked responses, explicit errors and unresolved attempts by request ID, not event order. Keep unresolved cost unknown rather than treating absent usage as zero.
6. Check whether calibration subtotals describe rows already included in the main ledger before adding them. A separate cost register is not necessarily a disjoint expense population.

Completion criterion: the requested run table has every requested ID, named status/subject, precisely defined cost columns, reconciled totals and an explicit unknown bucket where needed.

## 6. Close the evidence boundary

- Repeat the initial state and consumption checks and explain every difference before describing the inventory as read-only.
- Preserve failed setup attempts alongside corrected captures, but use only the valid observation for the measured conclusion.
- Verify hash chains against the original private data using the original checker. If the public export redacts record contents, disclose that its original chain cannot be recomputed from the redacted export alone; a successful private verification is not a fully reproducible public proof.
- Export byte-equality evidence directly from the source byte stream, not from rendered tool stdout. Text transports may strip the final newline; compare the exported artifact with the Git blob or original bytes before sealing it.
- Validate an earlier report's reconciliation against identifiers and creation times before inheriting its explanation. A proposed common verdict cannot contain an operation completed before its candidate existed; keep the count discrepancy explicit when request-to-candidate linkage is absent.
- Deliver new measurements and source-linked findings, with earlier reports linked only where needed to reconstruct a boundary or reconcile a figure. Do not convert incomplete code review into a claim that every deviation has been found.
