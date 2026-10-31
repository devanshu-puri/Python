# 🐍 01 · Python

<!--AUTO:START-->
> The core language, from strings and dictionaries to decorators, generators and async, plus small projects.

**Progress:** `██████████████████░░` **92%** · 35 of 39 topics done

## 🧭 How to use this folder

Go through the chapters in numeric order. Every file is a small, runnable script: read it, run it, change the inputs, break it on purpose. When a chapter feels comfortable, try the applied exercises, which combine several concepts into realistic problems. Mental models and write-ups live in [`docs/`](../docs).

## 📚 Chapters

### 01 · Data, Logic & Functions

_The raw material every program is made of: data types, control flow and functions._ · 8/8 topics done

- [x] **01. Strings**  —  slicing, f-strings, methods · Source: [`01_strings.py`](01-basics/01_strings.py)
  - *Why it matters later:* Prompt templates and text cleaning for LLM inputs
- [x] **02. Numeric data**  —  int/float, operators, conversion · Source: [`02_numeric_data.py`](01-basics/02_numeric_data.py)
  - *Why it matters later:* Token counts, scores, and metrics
- [x] **03. Lists, sets, tuples**  —  mutability, membership, ordering · Source: [`03_list_set_tuple.py`](01-basics/03_list_set_tuple.py)
  - *Why it matters later:* Batches of documents, permission sets, immutable configs
- [x] **04. Dictionaries**  —  lookup, nesting, iteration · Source: [`04_dictionaries.py`](01-basics/04_dictionaries.py)
  - *Why it matters later:* JSON payloads and API records
- [x] **05. Conditionals & booleans**  —  if/elif/else, truthiness · Source: [`05_conditionals_booleans.py`](01-basics/05_conditionals_booleans.py)
  - *Why it matters later:* Request routing and guardrail checks
- [x] **06. Loops & iterators**  —  for/while, iter/next · Source: [`06_loops_iterators.py`](01-basics/06_loops_iterators.py)
  - *Why it matters later:* Streaming tokens and retry loops
- [x] **07. Comprehensions**  —  list, dict, set · Source: [`07_comprehensions.py`](01-basics/07_comprehensions.py)
  - *Why it matters later:* Fast data shaping in ETL and feature prep
- [x] **08. Functions**  —  args/kwargs, return values, scope · Source: [`08_functions.py`](01-basics/08_functions.py)
  - *Why it matters later:* Service handlers and agent tool functions

### 02 · Modules, Libraries & Files

_Splitting code into modules, using the standard library, and reading and writing files._ · 3/4 topics done

- [x] **01. Modules & imports**  —  `import`, `from ... import`, your own module · Source: [`01_modules_library.py`](02-modules-and-files/01_modules_library.py), [`my_module.py`](02-modules-and-files/my_module.py)
  - *Why it matters later:* Package layout of real services
- [x] **02. Standard library tour**  —  stdlib modules, third-party packages · Source: [`02_modules_library_2.py`](02-modules-and-files/02_modules_library_2.py)
  - *Why it matters later:* Stdlib in real services
- [x] **03. Reading & writing files**  —  `open()`, file modes, `with` blocks, copying files · Source: [`03_read_write.py`](02-modules-and-files/03_read_write.py)
  - *Why it matters later:* Config files, logs, and dataset loading
- [ ] **04. Logging**
  - *Why it matters later:* Observability in services and agents

### 03 · Classes & Abstraction

_Bundling data and behaviour into objects._ · 6/7 topics done

- [x] **01. Classes & instances**  —  `__init__`, instance attributes · Source: [`01_classes_instances.py`](03-oop/01_classes_instances.py)
  - *Why it matters later:* Models, clients, and service objects
- [x] **02. Class variables**  —  shared state, class vs instance attributes · Source: [`02_class_variables.py`](03-oop/02_class_variables.py)
  - *Why it matters later:* Shared config and registries
- [x] **03. Class & static methods**  —  `@classmethod`, `@staticmethod` · Source: [`03_classmethods_staticmethods.py`](03-oop/03_classmethods_staticmethods.py)
  - *Why it matters later:* Alternate constructors, e.g. Model.from_config()
- [x] **04. Inheritance**  —  `super()`, overriding · Source: [`04_inheritance.py`](03-oop/04_inheritance.py)
  - *Why it matters later:* Base provider classes for LLM vendors
- [x] **05. Special methods**  —  `__repr__`, dunder methods · Source: [`05_special_methods.py`](03-oop/05_special_methods.py)
  - *Why it matters later:* Readable logs and debuggable objects
- [x] **06. Property decorator**  —  `@property`, getters and setters · Source: [`06_property_decorator.py`](03-oop/06_property_decorator.py)
  - *Why it matters later:* Validated fields, as in Pydantic
- [/] **07. Composition**  —  has-a vs is-a
  - *Why it matters later:* Agents composed of tools, memory, and a model

### 04 · Real-world Plumbing

_The language features that frameworks are built on._ · 8/10 topics done

- [x] **01. First-class functions**  —  functions as values, passing functions around · Source: [`01_first_class_functions.py`](04-intermediate/01_first_class_functions.py)
  - *Why it matters later:* Pluggable model and tool strategies
- [x] **02. Closures**  —  enclosing scope, factory functions · Source: [`02_closures.py`](04-intermediate/02_closures.py)
  - *Why it matters later:* Configured clients and per-request handlers
- [x] **03. Decorators**  —  wrapping functions, `functools.wraps` · Source: [`03_decorators.py`](04-intermediate/03_decorators.py)
  - *Why it matters later:* FastAPI routes, tracing, and auth checks
- [x] **04. Decorators with arguments**  —  decorator factories · Source: [`04_decorators_with_arguments.py`](04-intermediate/04_decorators_with_arguments.py)
  - *Why it matters later:* Retries, rate limits, and permissions as `@decorator(...)`
- [x] **05. Iterators & iterables**  —  `__iter__`, `__next__` · Source: [`05_iterators_iterables.py`](04-intermediate/05_iterators_iterables.py)
  - *Why it matters later:* Streaming responses and paginated APIs
- [x] **06. Generators**  —  `yield`, lazy evaluation · Source: [`06_generators.py`](04-intermediate/06_generators.py)
  - *Why it matters later:* Streaming tokens and large-file processing
- [x] **07. Exception handling**  —  try/except/finally, custom exceptions · Source: [`07_exception_handling.py`](04-intermediate/07_exception_handling.py)
  - *Why it matters later:* API error responses and retry logic
- [x] **08. Type hints**  —  annotations, `Optional` and unions · Source: [`08_type_hints.py`](04-intermediate/08_type_hints.py)
  - *Why it matters later:* Typed API contracts and Pydantic models
- [/] **09. Async I/O**  —  `async` / `await`, event loop · Source: [`09_async_io.py`](04-intermediate/09_async_io.py)
  - *Why it matters later:* Concurrent model and tool calls
- [ ] **10. Validation**  —  dataclasses, Pydantic
  - *Why it matters later:* Structured outputs from models

### 05 · Mental-Bridge Applications

_Ten small scenarios that connect syntax to systems._ · 10/10 topics done

- [x] **01. 01 Zip & dictionary mapping**  —  zip, filtering · Source: [`01_zip_dictionary_mapping.py`](05-applied-exercises/01_zip_dictionary_mapping.py), [`01_zip_dictionary_mapping_solution.py`](05-applied-exercises/01_zip_dictionary_mapping_solution.py)
  - *Why it matters later:* Authorization and tool access
- [x] **02. 02 Set permissions**  —  set ops · Source: [`02_set_permissions.py`](05-applied-exercises/02_set_permissions.py)
  - *Why it matters later:* Permission checks
- [x] **03. 03 Filter users**  —  predicates · Source: [`03_filter_users.py`](05-applied-exercises/03_filter_users.py)
  - *Why it matters later:* Query-like selection / metadata retrieval
- [x] **04. 04 Transform API data**  —  map · Source: [`04_transform_api_data.py`](05-applied-exercises/04_transform_api_data.py)
  - *Why it matters later:* API response shaping
- [x] **05. 05 Group users by role**  —  grouping · Source: [`05_group_users_by_role.py`](05-applied-exercises/05_group_users_by_role.py)
  - *Why it matters later:* Aggregation and reporting
- [x] **06. 06 JSON data processing**  —  json · Source: [`06_json_data_processing.py`](05-applied-exercises/06_json_data_processing.py)
  - *Why it matters later:* External data boundaries
- [x] **07. 07 Function as data**  —  callbacks · Source: [`07_function_as_data.py`](05-applied-exercises/07_function_as_data.py)
  - *Why it matters later:* Pluggable model/tool strategies
- [x] **08. 08 Decorator logging**  —  decorators · Source: [`08_decorator_logging.py`](05-applied-exercises/08_decorator_logging.py)
  - *Why it matters later:* Tracing and observability
- [x] **09. 09 Generator data**  —  yield · Source: [`09_generator_large_data.py`](05-applied-exercises/09_generator_large_data.py)
  - *Why it matters later:* Streaming and memory efficiency
- [x] **10. 10 Error-handling pipeline**  —  try/except · Source: [`10_error_handling_pipeline.py`](05-applied-exercises/10_error_handling_pipeline.py)
  - *Why it matters later:* Resilient processing

## 🧪 Projects in this folder

- ✅ [**Personal Expense CLI**](projects/personal_expense_cli) — *done*
  - Track expenses from the terminal, stored as JSON.
  - **Concepts:** Dictionaries _(Data, Logic & Functions)_, Functions _(Data, Logic & Functions)_, Reading & writing files _(Modules, Libraries & Files)_, Exception handling _(Real-world Plumbing)_, 06 JSON data processing _(Mental-Bridge Applications)_
- 💡 [**Smart File Organizer**](projects/smart_file_organizer) — *planned*
  - Sort a messy folder into tidy categories.
  - **Concepts:** Reading & writing files _(Modules, Libraries & Files)_, Conditionals & booleans _(Data, Logic & Functions)_, Modules & imports _(Modules, Libraries & Files)_

✅ done · 🟡 in progress · ⬜ not started
<!--AUTO:END-->

---

⬅️ Back to the [main roadmap](../README.md)
