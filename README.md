# policyglass

`policyglass` explores security tooling with a small Python codebase and local fixtures. The technical goal is to lint access policies for broad grants and shadowed conditions.

## Use Case

The point is to make a small domain rule concrete enough that a reader can change it and immediately see what broke.

## Policyglass Review Notes

For a quick review, compare `policy width` with `claim drift` before reading the middle cases.

## Highlights

- `fixtures/domain_review.csv` adds cases for trust boundary and claim drift.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/policyglass-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `policy width` and `claim drift`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Code Layout

The core code exposes a scoring path and the added review layer uses `signal`, `slack`, `drag`, and `confidence`. The domain terms are `trust boundary`, `claim drift`, `replay exposure`, and `policy width`.

The Python addition stays small enough to inspect in one sitting.

## Run The Check

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Regression Path

The check exercises the source code and the review fixture. `recovery` is the high score at 234; `stress` is the low score at 128.

## Future Work

The fixture set is small enough to audit by hand. The next useful expansion is malformed input coverage, not extra surface area.
