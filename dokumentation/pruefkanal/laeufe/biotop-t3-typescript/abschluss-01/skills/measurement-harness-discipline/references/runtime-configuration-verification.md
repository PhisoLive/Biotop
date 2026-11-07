# Verifying which configuration is actually in effect

For the question "which model / provider / credential / setting is this live system really using?".
The recurring failure is answering it from the configuration file, a status command, or a
catalog warning — all of which describe intent, not the request that went out.

## The evidence ladder, weakest to strongest

| Source | What it proves | Trap |
|---|---|---|
| Config file / `config get` | The declared default | Silent when a narrower scope overrides it |
| Status / doctor output | The declared default plus reachability | Reports what is *configured*, not what a running conversation resolved to |
| Persisted per-conversation state | The override actually attached to that conversation | Often stores only some fields; absence is not "unset" |
| Usage/accounting row per conversation | The name the system billed under | Written after the fact; carries no per-request parameters |
| Runtime resolver called in-process | What the next request will resolve to | Still a prediction; does not prove the call was made |
| **Outgoing request payload** | **What actually went on the wire** | Requires a request to be made — costs one call |

Publish which rung the claim stands on. A claim from rung 1–2 is "configured as", never
"is running on".

## Procedure

1. **Read the global default and the per-scope override separately.** Record both, and say
   which one the running conversation is currently bound to. A user report of "the setting
   keeps snapping back" is nearly always a scope question, not a broken write.
2. **Find the reader, not the writer.** Locate the code that consumes the key — the resolver,
   the transport, the point where the value is placed on the request. Name it in the report.
3. **Call the resolver in-process** with the real configuration loaded, so the predicted value
   comes from the same function the request path uses rather than from your reading of the file.
4. **Check the value against the target's accepted vocabulary.** Call the clamp/normalize
   function with the concrete target and assert the value comes back unchanged.
5. **Make one real call with request dumping enabled** and read the dumped payload. That is the
   only artifact-level proof. Book it as a deliberate call with its cost.
6. **Publish per-rung**, and mark anything only shown by code reading as *read, not run*.

## Rules

- **A setting with conversation scope outranks the global default and is cleared on conversation
  reset, not on change.** "It reverts every time I start fresh" therefore means the global
  default still holds the old value while the override was only ever per-conversation. Fix the
  global default; a per-conversation switch does not persist across a reset by design.
- **A writer's "unrecognized key" warning is evidence about the writer's catalog, not about
  whether the key is read.** Settle it on the reader: find the consuming function, confirm the
  key already carried a live value before your edit, and find the in-product command that writes
  the same path. Three independent confirmations beat one warning; do not rename a working key
  because a catalog is incomplete.
- **A value accepted by the configuration layer can still be downgraded at the transport
  boundary.** Each backend declares its own vocabulary and silently clamps to the nearest weaker
  level. Claiming a level is in effect requires the clamp call for that exact target, or the
  wire payload.
- **A field present in one execution path's persisted state and absent in another's is not
  proof the setting differs** — it is proof that path does not persist it. Say the value is
  unmeasured on that path and name what would measure it, rather than inferring from the
  richer path.
- **When the only instrument for a value requires changing the run, put the choice to the
  owner.** Enabling request dumping means restarting the service, which makes the restart part
  of the measurement and destroys the very question "does the change take effect without a
  restart?". Present both options with what each can and cannot show; do not quietly perform the
  intervention, and do not quietly substitute a proxy for the unmeasurable value.
- **A reset that changes the conversation identity also resets every conversation-scoped
  override.** Before promising "after the reset it will use X", check whether X lives in
  conversation scope; if it does, the promise is false.

## Credential-pool reading

- **A credential listed for a provider is not a credential in use.** Entries can be present as
  metadata with no usable secret attached, and selection skips them. Check the field the
  selector actually reads (the resolved runtime key), not the presence of a row or a
  fingerprint, before reporting that a key is "back" or that it displaces another.
- **An exhaustion marker is a timed cooldown unless a hard-dead status says otherwise.**
  Compute the expiry from the recorded timestamp plus the applicable time-to-live and report
  the wall-clock end, distinguishing a provider-supplied reset time from the default. "Blocked"
  and "blocked until HH:MM" are different findings.
- **Read OAuth validity from the token's own claims, offline.** The expiry sits in the token;
  it needs no network call and no model call. Distinguish the credential used for requests from
  the identity token issued at login — the latter expiring says nothing about whether calls work.
