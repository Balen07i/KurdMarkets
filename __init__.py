"""Core shared modules: configuration, database, cache, logging, exceptions.

Every other package (bot, worker, providers, reconciliation, monitoring,
history) depends on `core` — `core` must never import from them.
"""
