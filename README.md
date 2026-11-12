# self-healing-demo

A tiny repo with a deliberately failing test (`add` subtracts). CI fails on `main`; the
self-healing workflow should diagnose it and open a pull request with the fix.
