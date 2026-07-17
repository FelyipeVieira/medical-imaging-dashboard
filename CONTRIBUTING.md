# Contributing

Discuss major changes first. Use de-identified synthetic fixtures, preserve
physical image geometry, document clinical assumptions, and add focused tests.

```bash
pip install -e ".[dev]"
ruff check src tests
pytest
```

Plugins must implement documented protocols, fail safely, avoid global mutable
state, and declare dependencies. Security and privacy issues should not include
real patient data in reports or screenshots.

