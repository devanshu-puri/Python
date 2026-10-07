# Python Mental Bridge Modules

This is a small first-pass collection: eight case studies that connect familiar
Python building blocks to backend and AI/LLM work. Each module is intentionally
an introduction, not a production implementation. Use a module as a short
practice session; revisit its extensions later in a real project.

## Suggested order

1. [A tiny user directory](01-user-directory.md) — lists, dictionaries, loops,
   comprehensions, `zip()`, and `enumerate()`.
2. [A simple access check](02-access-check.md) — sets, membership, and the
   difference between identifying a user and checking a permission.
3. [Clean and group event records](03-event-records.md) — functions, filtering,
   sorting, grouping, counting, JSON, and errors.
4. [A typed order service](04-typed-order-service.md) — classes, composition,
   dataclasses, types, and validation.
5. [A small request pipeline](05-request-pipeline.md) — function composition,
   callbacks, decorators, configuration, logging, and API-style results.
6. [Prepare documents for search](06-document-preparation.md) — file iteration,
   generators, chunks, metadata, and retrieval.
7. [Build a safe assistant tool call](07-assistant-tool-call.md) — messages,
   tool definitions, permissions, structured results, and fallback.
8. [Make repeated work safer](08-reliable-work.md) — caching, idempotency,
   queues, retries, rate limits, and observability as concepts.

## Topic coverage map

The 75 ideas from the original topic list are deliberately grouped rather than
turned into 75 separate tutorials. Numbers below refer to that original list.

| Module | Original topics represented |
|---|---|
| 01 | 1-8 |
| 02 | 2, 20, 22, 43-44, 65, 75 |
| 03 | 9-11, 19-25 |
| 04 | 26-32, 40 |
| 05 | 12-18, 45-49 |
| 06 | 19, 25, 33-39, 53-55 |
| 07 | 56-64, 73-75 |
| 08 | 46, 49-52, 65-72 |

Topics recur where the same simple pattern naturally appears in more than one
case. Async, distributed systems, and production security are labeled as later
topics; this collection only shows the connection.

## How to work through a module

Read sections 1-5 and try the task before looking at section 6. Then trace the
data, explain the result in your own words, and attempt the questions before
checking the answers. The code in the examples uses small local data and does
not need a web framework, database, or AI package.
