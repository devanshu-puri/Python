<p align="center"><img src="assets/header.svg" alt="Python: From First Principles to AI Engineering" width="100%"/></p><p align="center">  <img alt="Python" src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

  <img alt="Focus" src="https://img.shields.io/badge/Goal-AI%20Engineering-8b5cf6?style=for-the-badge"/>

  <img alt="Status" src="https://img.shields.io/badge/Learning-In%20Public-22c55e?style=for-the-badge"/>

  <img alt="Last commit" src="https://img.shields.io/github/last-commit/devanshu-puri/Python?style=for-the-badge"/>
</p><p align="center"><i>A living learning lab for building Python intuition, one small system at a time.</i></p>📊 Journey Dashboard
<!--DASH:START--><p align="center"><img src="assets/dashboard.svg?v=5b86e7f3" alt="Journey dashboard" width="100%"/></p>Current checkpoint: Python foundations + mental-bridge applications  

Overall: ██████████░░░░░░░░░░ 51%
<details><summary>Plain-text view</summary>
Python foundations    [██████████] 100%

Modules & files       [████████░░]  75%

Object-oriented code  [█████████░]  93%

Intermediate Python   [████████░░]  85%

Small applications    [██████████] 100%

Backend engineering   [░░░░░░░░░░]   3%

ML fundamentals       [░░░░░░░░░░]   0%

LLM / RAG / agents    [░░░░░░░░░░]   0%

Production AI         [░░░░░░░░░░]   0%

</details><!--DASH:END-->Edit journey.json, push, and the dashboard, map, and book below rebuild automatically. See How to update.

🗺️ Learning Map
<!--MAP:START-->
Your learning journey, from Python fundamentals to production AI engineering.
Track	Progress
🧱 Python foundations	100%
📚 Modules & files	75%
🧩 Object-oriented code	93%
🛠️ Intermediate Python	85%
🚀 Small applications	100%
🏗️ Backend engineering	3%
📈 ML fundamentals	0%
🤖 LLM / RAG / agents	0%
🛡️ Production AI	0%


🟢 Complete · 🟡 In progress · 🔵 Upcoming
<!--MAP:END-->📂 Explore the Tracks
Every folder has its own README with the chapters, the topics inside each chapter, and what each one is for. Start with 01-python, then follow the numbers.
<!--AREAS:START-->
| Folder | What's inside | Progress |

| --- | --- | --- |

| [🐍 **`01-python/`**](01-python/)
Python | The core language, from strings and dictionaries to decorators, generators and async, plus small projects. | █████████░ 92%
35/39 topics |

| [🏗️ **`02-backend/`**](02-backend/)
Backend engineering | Turning Python scripts into real services: HTTP, FastAPI, databases, auth, testing and deployment. | ░░░░░░░░░░ 3%
0/16 topics |

| [📈 **`03-ml-foundations/`**](03-ml-foundations/)
ML foundations | Just enough NumPy, pandas and model basics to understand embeddings, evaluation and what LLMs are built on. | ░░░░░░░░░░ 0%
0/4 topics |

| [🤖 **`04-llm-rag-agents/`**](04-llm-rag-agents/)
LLMs, RAG & agents | Calling models, retrieving knowledge, using tools, and running all of it safely in production. | ░░░░░░░░░░ 0%
0/12 topics |
<!--AREAS:END-->📖 The Book: Chapters, Topics, Subtopics
Every chapter lists what was covered, and where that idea shows up later in AI or backend engineering.
<!--BOOK:START-->Part 1 · 🧱 Python foundations — 100%
<details><summary><b>Chapter 1.1: Data, Logic &amp; Functions</b> &nbsp;·&nbsp; 8/8 topics</summary>_The raw material every program is made of: data types, control flow and functions._  📂 01-python/01-basics/

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ✅ | Strings | [`01_strings.py`](01-python/01-basics/01_strings.py) | slicing, f-strings, methods | Prompt templates and text cleaning for LLM inputs |

| ✅ | Numeric data | [`02_numeric_data.py`](01-python/01-basics/02_numeric_data.py) | int/float, operators, conversion | Token counts, scores, and metrics |

| ✅ | Lists, sets, tuples | [`03_list_set_tuple.py`](01-python/01-basics/03_list_set_tuple.py) | mutability, membership, ordering | Batches of documents, permission sets, immutable configs |

| ✅ | Dictionaries | [`04_dictionaries.py`](01-python/01-basics/04_dictionaries.py) | lookup, nesting, iteration | JSON payloads and API records |

| ✅ | Conditionals & booleans | [`05_conditionals_booleans.py`](01-python/01-basics/05_conditionals_booleans.py) | if/elif/else, truthiness | Request routing and guardrail checks |

| ✅ | Loops & iterators | [`06_loops_iterators.py`](01-python/01-basics/06_loops_iterators.py) | for/while, iter/next | Streaming tokens and retry loops |

| ✅ | Comprehensions | [`07_comprehensions.py`](01-python/01-basics/07_comprehensions.py) | list, dict, set | Fast data shaping in ETL and feature prep |

| ✅ | Functions | [`08_functions.py`](01-python/01-basics/08_functions.py) | args/kwargs, return values, scope | Service handlers and agent tool functions |
</details>Part 2 · 📚 Modules & files — 75%
<details open><summary><b>Chapter 1.2: Modules, Libraries &amp; Files</b> &nbsp;·&nbsp; 3/4 topics</summary>_Splitting code into modules, using the standard library, and reading and writing files._  📂 01-python/02-modules-and-files/

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ✅ | Modules & imports | [`01_modules_library.py`](01-python/02-modules-and-files/01_modules_library.py)
[`my_module.py`](01-python/02-modules-and-files/my_module.py) | import, from ... import, your own module | Package layout of real services |

| ✅ | Standard library tour | [`02_modules_library_2.py`](01-python/02-modules-and-files/02_modules_library_2.py) | stdlib modules, third-party packages | Stdlib in real services |

| ✅ | Reading & writing files | [`03_read_write.py`](01-python/02-modules-and-files/03_read_write.py) | open(), file modes, with blocks, copying files | Config files, logs, and dataset loading |

| ⬜ | Logging | — | — | Observability in services and agents |
</details>Part 3 · 🧩 Object-oriented code — 93%
<details open><summary><b>Chapter 1.3: Classes &amp; Abstraction</b> &nbsp;·&nbsp; 6/7 topics</summary>_Bundling data and behaviour into objects._  📂 01-python/03-oop/

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ✅ | Classes & instances | [`01_classes_instances.py`](01-python/03-oop/01_classes_instances.py) | \_\_init\_\_, instance attributes | Models, clients, and service objects |

| ✅ | Class variables | [`02_class_variables.py`](01-python/03-oop/02_class_variables.py) | shared state, class vs instance attributes | Shared config and registries |

| ✅ | Class & static methods | [`03_classmethods_staticmethods.py`](01-python/03-oop/03_classmethods_staticmethods.py) | @classmethod, @staticmethod | Alternate constructors, e.g. Model.from_config() |

| ✅ | Inheritance | [`04_inheritance.py`](01-python/03-oop/04_inheritance.py) | super(), overriding | Base provider classes for LLM vendors |

| ✅ | Special methods | [`05_special_methods.py`](01-python/03-oop/05_special_methods.py) | \_\_repr\_\_, dunder methods | Readable logs and debuggable objects |

| ✅ | Property decorator | [`06_property_decorator.py`](01-python/03-oop/06_property_decorator.py) | @property, getters and setters | Validated fields, as in Pydantic |

| 🟡 | Composition | — | has-a vs is-a | Agents composed of tools, memory, and a model |
</details>Part 4 · 🛠️ Intermediate Python — 85%
<details open><summary><b>Chapter 1.4: Real-world Plumbing</b> &nbsp;·&nbsp; 8/10 topics</summary>_The language features that frameworks are built on._  📂 01-python/04-intermediate/

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ✅ | First-class functions | [`01_first_class_functions.py`](01-python/04-intermediate/01_first_class_functions.py) | functions as values, passing functions around | Pluggable model and tool strategies |

| ✅ | Closures | [`02_closures.py`](01-python/04-intermediate/02_closures.py) | enclosing scope, factory functions | Configured clients and per-request handlers |

| ✅ | Decorators | [`03_decorators.py`](01-python/04-intermediate/03_decorators.py) | wrapping functions, functools.wraps | FastAPI routes, tracing, and auth checks |

| ✅ | Decorators with arguments | [`04_decorators_with_arguments.py`](01-python/04-intermediate/04_decorators_with_arguments.py) | decorator factories | Retries, rate limits, and permissions as decorator(...) |

| ✅ | Iterators & iterables | [`05_iterators_iterables.py`](01-python/04-intermediate/05_iterators_iterables.py) | \_\_iter\_\_, \_\_next\_\_ | Streaming responses and paginated APIs |

| ✅ | Generators | [`06_generators.py`](01-python/04-intermediate/06_generators.py) | yield, lazy evaluation | Streaming tokens and large-file processing |

| ✅ | Exception handling | [`07_exception_handling.py`](01-python/04-intermediate/07_exception_handling.py) | try/except/finally, custom exceptions | API error responses and retry logic |

| ✅ | Type hints | [`08_type_hints.py`](01-python/04-intermediate/08_type_hints.py) | annotations, Optional and unions | Typed API contracts and Pydantic models |

| 🟡 | Async I/O | [`09_async_io.py`](01-python/04-intermediate/09_async_io.py) | async / await, event loop | Concurrent model and tool calls |

| ⬜ | Validation | — | dataclasses, Pydantic | Structured outputs from models |
</details>Part 5 · 🚀 Small applications — 100%
<details><summary><b>Chapter 1.5: Mental-Bridge Applications</b> &nbsp;·&nbsp; 10/10 topics</summary>_Ten small scenarios that connect syntax to systems._  📂 01-python/05-applied-exercises/

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ✅ | 01 Zip & dictionary mapping | [`01_zip_dictionary_mapping.py`](01-python/05-applied-exercises/01_zip_dictionary_mapping.py)
[`01_zip_dictionary_mapping_solution.py`](01-python/05-applied-exercises/01_zip_dictionary_mapping_solution.py) | zip, filtering | Authorization and tool access |

| ✅ | 02 Set permissions | [`02_set_permissions.py`](01-python/05-applied-exercises/02_set_permissions.py) | set ops | Permission checks |

| ✅ | 03 Filter users | [`03_filter_users.py`](01-python/05-applied-exercises/03_filter_users.py) | predicates | Query-like selection / metadata retrieval |

| ✅ | 04 Transform API data | [`04_transform_api_data.py`](01-python/05-applied-exercises/04_transform_api_data.py) | map | API response shaping |

| ✅ | 05 Group users by role | [`05_group_users_by_role.py`](01-python/05-applied-exercises/05_group_users_by_role.py) | grouping | Aggregation and reporting |

| ✅ | 06 JSON data processing | [`06_json_data_processing.py`](01-python/05-applied-exercises/06_json_data_processing.py) | json | External data boundaries |

| ✅ | 07 Function as data | [`07_function_as_data.py`](01-python/05-applied-exercises/07_function_as_data.py) | callbacks | Pluggable model/tool strategies |

| ✅ | 08 Decorator logging | [`08_decorator_logging.py`](01-python/05-applied-exercises/08_decorator_logging.py) | decorators | Tracing and observability |

| ✅ | 09 Generator data | [`09_generator_large_data.py`](01-python/05-applied-exercises/09_generator_large_data.py) | yield | Streaming and memory efficiency |

| ✅ | 10 Error-handling pipeline | [`10_error_handling_pipeline.py`](01-python/05-applied-exercises/10_error_handling_pipeline.py) | try/except | Resilient processing |
</details>Part 6 · 🏗️ Backend engineering — 3%
<details open><summary><b>Chapter 2.1: HTTP &amp; APIs</b> &nbsp;·&nbsp; 0/3 topics</summary>_How clients and servers talk: requests, responses and status codes._  📂 02-backend/01-http-and-apis/

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | HTTP basics | — | requests and responses, status codes, headers | Calling LLM provider APIs |

| ⬜ | REST design | — | resources, verbs, pagination | Tool and webhook APIs |

| 🟡 | Handlers & pipelines | — | handlers, pipelines | FastAPI services |
</details><details><summary><b>Chapter 2.2: FastAPI</b> &nbsp;·&nbsp; 0/3 topics</summary>
_Serving Python functions over HTTP._  📂 02-backend/02-fastapi/

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | First FastAPI service | — | routes, path and query parameters | Serving models and RAG endpoints |

| ⬜ | Request & response models | — | Pydantic models, validation errors | Structured LLM outputs |

| ⬜ | Dependencies & middleware | — | dependency injection, middleware | Auth, logging, and rate-limiting layers |
</details><details><summary><b>Chapter 2.3: Databases</b> &nbsp;·&nbsp; 0/3 topics</summary>
_Storing and querying data reliably._  📂 02-backend/03-databases/

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | SQL basics | — | tables, joins, indexes | Metadata and application data |

| ⬜ | SQLAlchemy | — | models, sessions | Repository-style data access |

| ⬜ | Redis & caching | — | key-value, TTL | Caching LLM responses and rate limits |
</details><details><summary><b>Chapter 2.4: Auth &amp; Security</b> &nbsp;·&nbsp; 0/2 topics</summary>
_Knowing who is calling and what they may do._  📂 02-backend/04-auth-and-security/

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | Authentication | — | password hashing, JWT | API keys and user sessions |

| ⬜ | Authorization | — | roles, permissions, multi-tenancy | Access control for RAG and agent tools |
</details><details><summary><b>Chapter 2.5: Testing</b> &nbsp;·&nbsp; 0/2 topics</summary>
_Proving the code works before users find out it doesn't._  📂 02-backend/05-testing/

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | pytest basics | — | asserts, fixtures | Regression tests for prompts and pipelines |

| ⬜ | Mocking & API tests | — | mocks, test client | Testing LLM calls without paying for them |
</details><details><summary><b>Chapter 2.6: Docker &amp; Deployment</b> &nbsp;·&nbsp; 0/3 topics</summary>
_Packaging and shipping a service._  📂 02-backend/06-docker-and-deployment/

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | Docker basics | — | images, containers | Reproducible AI services |

| ⬜ | Config & secrets | — | environment variables, .env files | Keeping API keys out of code |

| ⬜ | CI/CD | — | GitHub Actions | Automated tests and deploys |
</details>Part 7 · 📈 ML fundamentals — 0%
<details><summary><b>Chapter 3.1: NumPy &amp; pandas</b> &nbsp;·&nbsp; 0/2 topics</summary>_Working with arrays and tables of data._

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | NumPy arrays | — | arrays, vectorised maths | Embeddings are just vectors |

| ⬜ | pandas DataFrames | — | load, clean, group | Dataset prep and evaluation tables |
</details><details><summary><b>Chapter 3.2: Model basics</b> &nbsp;·&nbsp; 0/2 topics</summary>
_What it means for a model to learn, and how to tell if it did._

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | Train, test & evaluate | — | data splits, metrics | Evaluation mindset for LLM systems |

| ⬜ | Simple models | — | scikit-learn, overfitting | Understanding what a model actually learns |
</details>Part 8 · 🤖 LLM / RAG / agents — 0%
<details><summary><b>Chapter 4.1: LLM Basics</b> &nbsp;·&nbsp; 0/2 topics</summary>_Talking to a model from code._

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | LLM APIs & prompting | — | chat messages, system prompts, parameters | Every AI feature starts here |

| ⬜ | Structured output | — | JSON output, schema validation | Reliable parsing of model responses |
</details><details><summary><b>Chapter 4.2: Embeddings &amp; Vector Search</b> &nbsp;·&nbsp; 0/2 topics</summary>
_Turning text into vectors and finding what is similar._

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | Embeddings | — | text to vectors, similarity | Semantic search and clustering |

| ⬜ | Vector search | — | nearest neighbours, metadata filters | Retrieval for RAG |
</details><details><summary><b>Chapter 4.3: RAG</b> &nbsp;·&nbsp; 0/2 topics</summary>
_Giving a model the right knowledge at the right time._

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | Chunking & retrieval | — | splitting documents, top-k, metadata filtering | Document Q&A over private data |

| ⬜ | RAG pipeline | — | retrieve, augment, generate | End-to-end grounded answers |
</details><details><summary><b>Chapter 4.4: Agents &amp; Tool Use</b> &nbsp;·&nbsp; 0/3 topics</summary>
_Letting a model call functions and make decisions in a loop._

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | Function calling | — | tool schemas, tool permissions | Models that act, not just talk |

| ⬜ | Agent loop | — | plan, act, observe, memory | Multi-step task automation |

| ⬜ | MCP tools | — | servers, tools and resources | Standard way to plug tools into models |
</details>Part 9 · 🛡️ Production AI — 0%
<details><summary><b>Chapter 4.5: Evaluation &amp; Observability</b> &nbsp;·&nbsp; 0/3 topics</summary>_Knowing whether an AI system is good, and seeing what it does in production._

| | Topic | Source | Subtopics covered | Future reference (AI / backend) |

| :-: | --- | --- | --- | --- |

| ⬜ | Evaluation | — | test sets, LLM-as-judge | Catching regressions before users do |

| ⬜ | Tracing & observability | — | logs, traces, cost tracking | Debugging agents and RAG in production |

| ⬜ | Guardrails & safety | — | input checks, output validation | Safe tool use and data access |
</details><!--BOOK:END-->🧪 Projects and the Concepts They Use
<!--PROJECTS:START-->| Project | Status | Concepts it uses |

| --- | :-: | --- |

| Personal Expense CLI
_Track expenses from the terminal, stored as JSON._ | ✅ done | Dictionaries _(Data, Logic & Functions)_
Functions _(Data, Logic & Functions)_
Reading & writing files _(Modules, Libraries & Files)_
Exception handling _(Real-world Plumbing)_
06 JSON data processing _(Mental-Bridge Applications)_ |

| Smart File Organizer
_Sort a messy folder into tidy categories._ | 💡 planned | Reading & writing files _(Modules, Libraries & Files)_
Conditionals & booleans _(Data, Logic & Functions)_
Modules & imports _(Modules, Libraries & Files)_ |
<!--PROJECTS:END-->🧠 The Core Mental Model
How Python concepts evolve into real-world engineering systems:

Data structures → Records → Filtering → Functions → Modules → Backend services → AI systems → Production AI

| Python idea | Becomes |

| --- | --- |

| Dictionary mapping | Authorization |

| Filter | Metadata retrieval |

| Generator | Streaming |

| Decorator | Logging / tracing |

| Exception handler | Resilient processing |

| Function passed as data | Model or tool strategy |
🧭 Repository Guide

.

├── 01-python/              core language: basics → OOP → intermediate → exercises → projects

├── 02-backend/             HTTP, FastAPI, databases, auth, testing, deployment

├── 03-ml-foundations/      NumPy, pandas, model basics

├── 04-llm-rag-agents/      LLM APIs, embeddings, RAG, agents, evaluation

├── docs/                   mental models, mental bridges, prompts

├── scripts/                build_readme.py (regenerates the READMEs)

├── assets/                 header and dashboard images

└── journey.json            the single source of truth for progress

- [Python mental models](docs/mental-models/python_mental_models.md): the ideas behind the progression
- [Mental model map](docs/mental-models/python_mental_model_map.md): syntax to systems
- [Mental bridges](docs/mental-bridges/README.md): realistic scenarios that connect small patterns to real systems
Run any file from the repo root, for example:

python 01-python/05-applied-exercises/01_zip_dictionary_mapping.py

🔄 How to update
1. Change a topic's status in journey.json to done, wip, or todo (wip counts as half).

2. Add a topic to a chapter's topics list. File paths are written from the repo root; use also for extra files:

   ```json

   {"name": "Generators", "status": "done", "subtopics": ["yield"],

    "future": "Streaming tokens", "file": "01-python/04-intermediate/06_generators.py"}

   ```

3. Add a chapter under a track's chapters with its folder, e.g. "folder": "02-backend/02-fastapi". It appears automatically in that folder's README.

4. Add a project under projects. Each concepts entry must match a topic name exactly:

   ```json

   {"name": "Tool router", "path": "04-llm-rag-agents/projects/tool_router", "status": "building",

    "concepts": ["Inheritance", "10 Error-handling pipeline"]}

   ```

5. Run python scripts/build_readme.py locally, or just push: the GitHub Action does it for you. The script prints warnings for files that are missing or not listed in journey.json.
⭐ North Star

Learn a concept. Use it in a realistic problem.

Recognize the larger system it belongs to. Build the next layer.