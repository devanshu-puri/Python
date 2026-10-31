# 🐍 01 · Python

<!--AUTO:START-->
> The core language, from strings and dictionaries to decorators, generators and async, plus small projects.

**Progress:** `██████████████████░░` **92%** · 35 of 39 topics done

## 🧭 How to use this folder

Go through the chapters in numeric order. Every file is a small, runnable script: read it, run it, change the inputs, break it on purpose. When a chapter feels comfortable, try the applied exercises, which combine several concepts into realistic problems. Mental models and write-ups live in [`docs/`](../docs).

## 📚 Chapters at a glance

| Chapter | What it covers | Topics | Progress |
| --- | --- | :-: | :-: |
| [`01-basics/`](01-basics)<br>**Data, Logic & Functions** | The raw material every program is made of: data types, control flow and functions. | 8/8 | 100% |
| [`02-modules-and-files/`](02-modules-and-files)<br>**Modules, Libraries & Files** | Splitting code into modules, using the standard library, and reading and writing files. | 3/4 | 75% |
| [`03-oop/`](03-oop)<br>**Classes & Abstraction** | Bundling data and behaviour into objects. | 6/7 | 93% |
| [`04-intermediate/`](04-intermediate)<br>**Real-world Plumbing** | The language features that frameworks are built on. | 8/10 | 85% |
| [`05-applied-exercises/`](05-applied-exercises)<br>**Mental-Bridge Applications** | Ten small scenarios that connect syntax to systems. | 10/10 | 100% |

## 🔍 Inside each chapter

### 01 · Data, Logic & Functions

_The raw material every program is made of: data types, control flow and functions._ · 8/8 topics done

| # | | Topic | Source | What you practise | Why it matters later |
| :-: | :-: | --- | --- | --- | --- |
| 01 | ✅ | **Strings** | [`01_strings.py`](01-basics/01_strings.py) | slicing, f-strings, methods | Prompt templates and text cleaning for LLM inputs |
| 02 | ✅ | **Numeric data** | [`02_numeric_data.py`](01-basics/02_numeric_data.py) | int/float, operators, conversion | Token counts, scores, and metrics |
| 03 | ✅ | **Lists, sets, tuples** | [`03_list_set_tuple.py`](01-basics/03_list_set_tuple.py) | mutability, membership, ordering | Batches of documents, permission sets, immutable configs |
| 04 | ✅ | **Dictionaries** | [`04_dictionaries.py`](01-basics/04_dictionaries.py) | lookup, nesting, iteration | JSON payloads and API records |
| 05 | ✅ | **Conditionals & booleans** | [`05_conditionals_booleans.py`](01-basics/05_conditionals_booleans.py) | if/elif/else, truthiness | Request routing and guardrail checks |
| 06 | ✅ | **Loops & iterators** | [`06_loops_iterators.py`](01-basics/06_loops_iterators.py) | for/while, iter/next | Streaming tokens and retry loops |
| 07 | ✅ | **Comprehensions** | [`07_comprehensions.py`](01-basics/07_comprehensions.py) | list, dict, set | Fast data shaping in ETL and feature prep |
| 08 | ✅ | **Functions** | [`08_functions.py`](01-basics/08_functions.py) | args/kwargs, return values, scope | Service handlers and agent tool functions |

### 02 · Modules, Libraries & Files

_Splitting code into modules, using the standard library, and reading and writing files._ · 3/4 topics done

| # | | Topic | Source | What you practise | Why it matters later |
| :-: | :-: | --- | --- | --- | --- |
| 01 | ✅ | **Modules & imports** | [`01_modules_library.py`](02-modules-and-files/01_modules_library.py)<br>[`my_module.py`](02-modules-and-files/my_module.py) | `import`, `from ... import`, your own module | Package layout of real services |
| 02 | ✅ | **Standard library tour** | [`02_modules_library_2.py`](02-modules-and-files/02_modules_library_2.py) | stdlib modules, third-party packages | Stdlib in real services |
| 03 | ✅ | **Reading & writing files** | [`03_read_write.py`](02-modules-and-files/03_read_write.py) | `open()`, file modes, `with` blocks, copying files | Config files, logs, and dataset loading |
| 04 | ⬜ | **Logging** | — | — | Observability in services and agents |

### 03 · Classes & Abstraction

_Bundling data and behaviour into objects._ · 6/7 topics done

| # | | Topic | Source | What you practise | Why it matters later |
| :-: | :-: | --- | --- | --- | --- |
| 01 | ✅ | **Classes & instances** | [`01_classes_instances.py`](03-oop/01_classes_instances.py) | `__init__`, instance attributes | Models, clients, and service objects |
| 02 | ✅ | **Class variables** | [`02_class_variables.py`](03-oop/02_class_variables.py) | shared state, class vs instance attributes | Shared config and registries |
| 03 | ✅ | **Class & static methods** | [`03_classmethods_staticmethods.py`](03-oop/03_classmethods_staticmethods.py) | `@classmethod`, `@staticmethod` | Alternate constructors, e.g. Model.from_config() |
| 04 | ✅ | **Inheritance** | [`04_inheritance.py`](03-oop/04_inheritance.py) | `super()`, overriding | Base provider classes for LLM vendors |
| 05 | ✅ | **Special methods** | [`05_special_methods.py`](03-oop/05_special_methods.py) | `__repr__`, dunder methods | Readable logs and debuggable objects |
| 06 | ✅ | **Property decorator** | [`06_property_decorator.py`](03-oop/06_property_decorator.py) | `@property`, getters and setters | Validated fields, as in Pydantic |
| 07 | 🟡 | **Composition** | — | has-a vs is-a | Agents composed of tools, memory, and a model |

### 04 · Real-world Plumbing

_The language features that frameworks are built on._ · 8/10 topics done

| # | | Topic | Source | What you practise | Why it matters later |
| :-: | :-: | --- | --- | --- | --- |
| 01 | ✅ | **First-class functions** | [`01_first_class_functions.py`](04-intermediate/01_first_class_functions.py) | functions as values, passing functions around | Pluggable model and tool strategies |
| 02 | ✅ | **Closures** | [`02_closures.py`](04-intermediate/02_closures.py) | enclosing scope, factory functions | Configured clients and per-request handlers |
| 03 | ✅ | **Decorators** | [`03_decorators.py`](04-intermediate/03_decorators.py) | wrapping functions, `functools.wraps` | FastAPI routes, tracing, and auth checks |
| 04 | ✅ | **Decorators with arguments** | [`04_decorators_with_arguments.py`](04-intermediate/04_decorators_with_arguments.py) | decorator factories | Retries, rate limits, and permissions as `@decorator(...)` |
| 05 | ✅ | **Iterators & iterables** | [`05_iterators_iterables.py`](04-intermediate/05_iterators_iterables.py) | `__iter__`, `__next__` | Streaming responses and paginated APIs |
| 06 | ✅ | **Generators** | [`06_generators.py`](04-intermediate/06_generators.py) | `yield`, lazy evaluation | Streaming tokens and large-file processing |
| 07 | ✅ | **Exception handling** | [`07_exception_handling.py`](04-intermediate/07_exception_handling.py) | try/except/finally, custom exceptions | API error responses and retry logic |
| 08 | ✅ | **Type hints** | [`08_type_hints.py`](04-intermediate/08_type_hints.py) | annotations, `Optional` and unions | Typed API contracts and Pydantic models |
| 09 | 🟡 | **Async I/O** | [`09_async_io.py`](04-intermediate/09_async_io.py) | `async` / `await`, event loop | Concurrent model and tool calls |
| 10 | ⬜ | **Validation** | — | dataclasses, Pydantic | Structured outputs from models |

### 05 · Mental-Bridge Applications

_Ten small scenarios that connect syntax to systems._ · 10/10 topics done

| # | | Topic | Source | What you practise | Why it matters later |
| :-: | :-: | --- | --- | --- | --- |
| 01 | ✅ | **01 Zip & dictionary mapping** | [`01_zip_dictionary_mapping.py`](05-applied-exercises/01_zip_dictionary_mapping.py)<br>[`01_zip_dictionary_mapping_solution.py`](05-applied-exercises/01_zip_dictionary_mapping_solution.py) | zip, filtering | Authorization and tool access |
| 02 | ✅ | **02 Set permissions** | [`02_set_permissions.py`](05-applied-exercises/02_set_permissions.py) | set ops | Permission checks |
| 03 | ✅ | **03 Filter users** | [`03_filter_users.py`](05-applied-exercises/03_filter_users.py) | predicates | Query-like selection / metadata retrieval |
| 04 | ✅ | **04 Transform API data** | [`04_transform_api_data.py`](05-applied-exercises/04_transform_api_data.py) | map | API response shaping |
| 05 | ✅ | **05 Group users by role** | [`05_group_users_by_role.py`](05-applied-exercises/05_group_users_by_role.py) | grouping | Aggregation and reporting |
| 06 | ✅ | **06 JSON data processing** | [`06_json_data_processing.py`](05-applied-exercises/06_json_data_processing.py) | json | External data boundaries |
| 07 | ✅ | **07 Function as data** | [`07_function_as_data.py`](05-applied-exercises/07_function_as_data.py) | callbacks | Pluggable model/tool strategies |
| 08 | ✅ | **08 Decorator logging** | [`08_decorator_logging.py`](05-applied-exercises/08_decorator_logging.py) | decorators | Tracing and observability |
| 09 | ✅ | **09 Generator data** | [`09_generator_large_data.py`](05-applied-exercises/09_generator_large_data.py) | yield | Streaming and memory efficiency |
| 10 | ✅ | **10 Error-handling pipeline** | [`10_error_handling_pipeline.py`](05-applied-exercises/10_error_handling_pipeline.py) | try/except | Resilient processing |

## 🧪 Projects in this folder

| Project | Status | Concepts it uses |
| --- | :-: | --- |
| [**Personal Expense CLI**](projects/personal_expense_cli)<br>_Track expenses from the terminal, stored as JSON._ | ✅ done | Dictionaries _(Data, Logic & Functions)_<br>Functions _(Data, Logic & Functions)_<br>Reading & writing files _(Modules, Libraries & Files)_<br>Exception handling _(Real-world Plumbing)_<br>06 JSON data processing _(Mental-Bridge Applications)_ |
| [**Smart File Organizer**](projects/smart_file_organizer)<br>_Sort a messy folder into tidy categories._ | 💡 planned | Reading & writing files _(Modules, Libraries & Files)_<br>Conditionals & booleans _(Data, Logic & Functions)_<br>Modules & imports _(Modules, Libraries & Files)_ |

✅ done · 🟡 in progress · ⬜ not started
<!--AUTO:END-->

---

⬅️ Back to the [main roadmap](../README.md)
