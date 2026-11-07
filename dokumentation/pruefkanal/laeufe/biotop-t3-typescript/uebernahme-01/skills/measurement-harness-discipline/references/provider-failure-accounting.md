# Provider-failure accounting

For campaigns that call paid external models or APIs under a hard budget, where a failed call must never count as a contribution but may still have consumed budget. Two questions are always separate: **did it contribute?** (no, always, for every failure class) and **did it consume?** (unknown until established).

## Classify before reacting

Four classes, decided at the transport layer, carried through to the ledger:

| Class | Example | Retry? | Contribution | Consumption |
|---|---|---|---|---|
| refusal | safety refusal, content filter | never | 0 | per provider usage block |
| empty | valid response, no usable text | never | 0 | per provider usage block |
| timeout | no answer within the deadline | never | 0 | unknown by default |
| infrastructure | transport error, rate limit, 5xx | only if flagged retryable | 0 | unknown unless a usage block arrived |

Refusal and empty are **decisions**, not disruptions — the provider answered, the answer is unusable. Retrying them buys nothing and spends budget. A timeout stays a failure regardless of cause; the request may have been served and the answer lost.

## Retry policy

- **Retry only what the provider explicitly marks retryable.** A rate-limit or overload response that carries its own "retry shortly" indication is a wait condition; a bare 500 is not. Without that marker the call is an outright failure on the first attempt — otherwise every genuine outage costs the campaign its full retry budget before it reports.
- **Fix the cap and the wait before the run, as named constants.** An unbounded or ad-hoc retry turns a provider outage into an unbounded spend and an unbounded wall-clock.
- **Let the wait grow between attempts.** A fixed short wait against a rate limit reproduces the rate limit.
- **Place the retry loop *beneath* the accounting entry point, not around it.** Each attempt must still pass the pre-call budget check and land in the ledger, so a retried call cannot spend past the ceiling while the ledger shows one attempt.
- **Protocol and book every attempt, including the failed ones.** If the provider reported usage for a failed attempt, book it with a distinct purpose suffix so retried calls stay separable from first-time calls in the cost breakdown.
- **The countercase is an error without a retry marker.** A test that only proves "a retryable error is retried" proves the loop exists, not that it is selective. Pair it with an unmarked error that must fail on attempt one, and with a refusal and a timeout that must not be retried at all.

## Unknown consumption blocks further calls — keep that

A failure whose consumption cannot be established must stop the campaign: the provider may have billed a request that produced nothing, and a run that continues past it spends against a ceiling it can no longer compute. The block is correct.

The defect is a block with **no exit**. Without a clearing path the campaign is dead permanently and the pressure lands on loosening the rule.

## Clearing the block — resolve the doubt against the budget

1. **Reconcile the provider's own total against your recomputed ledger.** Take the provider's period usage figure, then recompute every ledger entry for that period at the provider's *published* per-token prices — not at your local price table, which drifts and will manufacture a residual on its own. The difference is the unexplained amount.
2. **Read the residual against one whole prompt, not against a tolerance.** A rejected request transfers the entire prompt or none of it, so a residual that is a *fraction* of the smallest comparable prompt is billing rounding across many entries, not a transferred prompt. Compute the residual in tokens at that model's price and state it as a share of a real prompt for the same purpose.
3. **Do not invent a closeness threshold.** "Within 0.0005 is effectively zero" is a bar you set yourself to pass your own check — the same defect as deriving a noise tolerance from a guessed constant.
4. **Book the maximum case.** Unless the provider's own per-call record proves the failed call consumed nothing, charge the full pre-call reservation as actual consumption. An indication is not a proof; whoever is wrong should be wrong against the budget, never in its favour.
5. **Clear one failure at a time.** Clearing must name the specific call; it must not release other outstanding failures, and re-clearing an already-cleared call must be refused.
6. **Clearing never converts a failure into a contribution.** The contribution count stays zero and the record keeps its failure class. Only the consumption column moves.
7. **The cleared amount counts against the ceiling like any other spend** — if booking it exhausts the budget, the run aborts. A clearing path that cannot bankrupt the run is a bypass, not a clearing path.

## Verification for the clearing path itself

The path is a gate, so it needs both directions executed:

- an outstanding failure blocks the next call;
- clearing it books the full reservation and releases exactly that one;
- a second outstanding failure still blocks;
- clearing a call with no outstanding failure is refused;
- clearing that exceeds the ceiling makes the next call abort on budget.
