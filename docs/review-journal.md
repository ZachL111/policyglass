# Review Journal

The repository goal stays the same: lint access policies for broad grants and shadowed conditions. This note explains the added review angle.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its security tooling focus without claiming live deployment or external usage.

## Cases

- `baseline`: `trust boundary`, score 178, lane `ship`
- `stress`: `claim drift`, score 128, lane `watch`
- `edge`: `replay exposure`, score 173, lane `ship`
- `recovery`: `policy width`, score 234, lane `ship`
- `stale`: `trust boundary`, score 175, lane `ship`

## Note

A future change should add new cases before it changes the scoring rule.
