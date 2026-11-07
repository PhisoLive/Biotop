# Defect-class sweep

When a run dies on a single instance of a *class* of defect — a hardcoded assumption about language, backend, platform, schema version or encoding that silently holds only for the original case — fixing the one instance guarantees the next run dies on the next instance. Sweep the whole subject for the class in one pass, then keep the sweep as a test.

Use this when the failure shape is "this code assumed X, and X is no longer universally true": a second language arrives, a second storage backend, a second protocol version, a second tenant.

## Why not one at a time

Each instance costs a full gated run to discover, and a gated run is frequently one-shot (no re-calibration, no re-eichung) — so every instance found this way also burns a run id and whatever was already charged to it. Sweeping costs one static pass plus one execution trace.

## Ordered procedure

1. **Name the class as concrete patterns, not as a concept.** "Assumes Python" is unsearchable. Its patterns are: the `def ` source-text muster, a hardcoded `.py` suffix test, parsing of pytest output, use of the Python syntax tree on subject code. Write each as its own regex with its own label, so each hit carries which assumption it represents.
2. **Trace the live path first.** Execute the real entry points for the new case under a profile/trace hook and record which functions of the subject are actually reached. This is the *cheap* half: it produces a small, certainly-relevant set, and any hit inside it is a real finding rather than a candidate. Expect harmless hits here (a comment, an ignore-pattern list) — read them, do not count them.
3. **Then sweep statically for the patterns the trace could not reach.** Functions that only run mid-campaign (candidate generation, judging, memory, negotiation) cannot be traced cheaply. Enumerate them by parsing the source tree, not by reading files by hand.
4. **Resolve every hit to guarded / unguarded / unreachable.** See the false-positive table below — the raw hit list is a checklist, never a defect list.
5. **Fix the unguarded ones in one commit**, then land the sweep itself as a test so the class cannot silently return.

## A hit is guarded if the switch is anywhere above it

Three distinct causes produce false positives, and each needs a different resolution. Getting this wrong in either direction is costly: reporting all raw hits as defects buries the real one, and suppressing hits by loosening the pattern makes the sweep blind.

| Cause | Signature | Correct resolution |
|---|---|---|
| Language-neutral list | The pattern appears alongside the other cases' patterns — a suffix loop trying `.mjs`, `.js`, `.py` in order | Not a finding. Tighten the pattern so a hit requires the assumption to be the *only* branch: match `endswith(".py")`, not a bare `".py"` anywhere in the body |
| Guard N levels up | The function itself has no switch, but its only caller is selected by one (`if ts: a() else: b()` two frames above) | Not a finding. Resolve the call chain and record the guard's file and line |
| Name collision | A same-named function exists in the new case's own module; text search cannot tell them apart | Not a finding. Resolve names per defining file: a hit in another file counts only if it imports the defining module or qualifies the call with its module name |

Also resolve **unreachable**: a function carrying the assumption that nothing calls cannot kill a run. Do not fix it and do not ignore it silently — list it in an allowlist keyed to its name, so the entry fails when something starts calling it.

## When the chain is beyond text search, use a reviewed exception list

Transitive guard chains (guard two frames up, through a dispatch table, behind a partial) are not reliably resolvable by grep, and stretching the resolver to chase them produces a checker nobody can trust. Stop and write the exception down instead:

- One entry per function, keyed `path::name`.
- Its value is a **justification with a line-level nachweis** — which file and line holds the guard, and why that guard covers this call. A justification that does not name a location is not a justification.
- New hits go into the fix, never into this list. The list is for chains the resolver cannot walk, not for findings that are inconvenient.
- Pair it with a **staleness test**: every entry must still match a current hit. Without it, an entry outlives the function it excused and then silently covers a *new* function that happens to share the name.

## The sweep checker needs both countercases

A checker that reports zero findings and a checker that is blind are indistinguishable from the result alone. Prove sensitivity and selectivity against a throwaway fixture tree, not against the real subject:

| Countercase | Fixture | Required outcome |
|---|---|---|
| Sensitivity | A function using the assumption, called, with no switch anywhere | Reported |
| Selectivity | The identical function with the switch added | Not reported |

Without the second, a checker that flags every match passes the first and is worthless. Build both fixtures as real files in a temporary tree and run the *shipped* sweep function against them.

Take the sweep's parameters (root path, exception list, allowlist) as **arguments**, not module globals read at call time. A checker whose root is a module constant cannot be pointed at a fixture tree without patching internals, and the countercases then silently re-scan the real subject and pass for the wrong reason.

## Reporting

Report the sweep with both denominators — functions reached by the trace and functions scanned statically — and state resolved false positives with their cause rather than dropping them. A bare "no findings" cannot be distinguished from a sweep that searched for the wrong thing.

When your own first-pass resolver produced false alarms, say so and name the three causes: the next person to widen the pattern needs to know which widenings are safe.
