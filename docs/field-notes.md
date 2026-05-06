# Field Notes

`policyglass` is easiest to review by starting with the fixture, not the prose.

The domain cases cover `trust boundary`, `claim drift`, `replay exposure`, and `policy width`. They sit beside the smaller starter fixture so the project has both a compact scoring check and a domain-flavored review check.

The widest spread is between `policy width` and `claim drift`, so those are the first two cases I would preserve during a refactor.

The language-specific addition keeps the review model in plain dataclasses and unittest checks.
