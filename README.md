<p align="center"><img src="assets/header.svg" alt="Python: From First Principles to AI Engineering" width="100%"/></p>


<p align="center">

  <img alt="Python" src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

  <img alt="Focus" src="https://img.shields.io/badge/Goal-AI%20Engineering-8b5cf6?style=for-the-badge"/>

  <img alt="Status" src="https://img.shields.io/badge/Learning-In%20Public-22c55e?style=for-the-badge"/>

  <img alt="Last commit" src="https://img.shields.io/github/last-commit/devanshu-puri/Python?style=for-the-badge"/>

</p>


<p align="center"><i>A living learning lab for building Python intuition, one small system at a time.</i></p>


---


## 📊 Journey Dashboard


<!--DASH:START-->
<p align="center"><img src="assets/dashboard.svg?v=5b86e7f3" alt="Journey dashboard" width="100%"/></p>

**Current checkpoint:** `Python foundations + mental-bridge applications`  
**Overall:** `██████████░░░░░░░░░░` **51%**

<details><summary>Plain-text view</summary>

```text
Python foundations    [██████████] 100%
Modules & files       [████████░░]  75%
Object-oriented code  [█████████░]  93%
Intermediate Python   [████████░░]  85%
Small applications    [██████████] 100%
Backend engineering   [░░░░░░░░░░]   3%
ML fundamentals       [░░░░░░░░░░]   0%
LLM / RAG / agents    [░░░░░░░░░░]   0%
Production AI         [░░░░░░░░░░]   0%
```
</details>
<!--DASH:END-->


> Edit `journey.json`, push, and the dashboard, map, and book below rebuild automatically. See [How to update](#-how-to-update).


## 🗺️ Learning Map


<!--MAP:START-->
A quick view of what is complete, in progress, and still ahead:

- 🟢 **🧱 Python foundations** — 100% (8/8 topics)
- 🟡 **📚 Modules & files** — 75% (3/4 topics)
- 🟡 **🧩 Object-oriented code** — 93% (6/7 topics)
- 🟡 **🛠️ Intermediate Python** — 85% (8/10 topics)
- 🟢 **🚀 Small applications** — 100% (10/10 topics)
- 🟡 **🏗️ Backend engineering** — 3% (0/16 topics)
- 🔵 **📈 ML fundamentals** — 0% (0/4 topics)
- 🔵 **🤖 LLM / RAG / agents** — 0% (0/9 topics)
- 🔵 **🛡️ Production AI** — 0% (0/3 topics)

🟢 Complete · 🟡 In progress · 🔵 Upcoming
<!--MAP:END-->


## 📂 Explore the Tracks


The journey is split into three areas. Open a folder README for its chapters, exercises, and projects. Start with Python, then move into backend and AI engineering.


<!--AREAS:START-->
<details>
<summary><b>🐍 Python</b> · 92% · 35/39 topics</summary>

The core language, from strings and dictionaries to decorators, generators and async, plus small projects.

📁 [`01-python/`](01-python/)

</details>

<details>
<summary><b>🏗️ Backend engineering</b> · 3% · 0/16 topics</summary>

Turning Python scripts into real services: HTTP, FastAPI, databases, auth, testing and deployment.

📁 [`02-backend/`](02-backend/)

</details>

<details>
<summary><b>🤖 AI engineering</b> · 0% · 0/16 topics</summary>

ML foundations, LLM APIs, embeddings, retrieval, agents, evaluation and production AI.

📁 [`03-llm-rag-agents/`](03-llm-rag-agents/)

</details>
<!--AREAS:END-->


## 📖 The Book: Chapters, Topics, Subtopics


Every chapter lists what was covered, and where that idea shows up later in **AI or backend engineering**.


<!--BOOK:START-->
### Part 1 · 🧱 Python foundations — 100%

<details>
<summary><b>1.1 · Data, Logic &amp; Functions</b> — 8/8 topics</summary>

_The raw material every program is made of: data types, control flow and functions._ · 📂 [`01-python/01-basics/`](01-python/01-basics)

- [x] **Strings**  —  slicing, f-strings, methods · Source: [`01_strings.py`](01-python/01-basics/01_strings.py)
  - *Why it matters later:* Prompt templates and text cleaning for LLM inputs
- [x] **Numeric data**  —  int/float, operators, conversion · Source: [`02_numeric_data.py`](01-python/01-basics/02_numeric_data.py)
  - *Why it matters later:* Token counts, scores, and metrics
- [x] **Lists, sets, tuples**  —  mutability, membership, ordering · Source: [`03_list_set_tuple.py`](01-python/01-basics/03_list_set_tuple.py)
  - *Why it matters later:* Batches of documents, permission sets, immutable configs
- [x] **Dictionaries**  —  lookup, nesting, iteration · Source: [`04_dictionaries.py`](01-python/01-basics/04_dictionaries.py)
  - *Why it matters later:* JSON payloads and API records
- [x] **Conditionals & booleans**  —  if/elif/else, truthiness · Source: [`05_conditionals_booleans.py`](01-python/01-basics/05_conditionals_booleans.py)
  - *Why it matters later:* Request routing and guardrail checks
- [x] **Loops & iterators**  —  for/while, iter/next · Source: [`06_loops_iterators.py`](01-python/01-basics/06_loops_iterators.py)
  - *Why it matters later:* Streaming tokens and retry loops
- [x] **Comprehensions**  —  list, dict, set · Source: [`07_comprehensions.py`](01-python/01-basics/07_comprehensions.py)
  - *Why it matters later:* Fast data shaping in ETL and feature prep
- [x] **Functions**  —  args/kwargs, return values, scope · Source: [`08_functions.py`](01-python/01-basics/08_functions.py)
  - *Why it matters later:* Service handlers and agent tool functions

</details>

### Part 2 · 📚 Modules & files — 75%

<details>
<summary><b>1.2 · Modules, Libraries &amp; Files</b> — 3/4 topics</summary>

_Splitting code into modules, using the standard library, and reading and writing files._ · 📂 [`01-python/02-modules-and-files/`](01-python/02-modules-and-files)

- [x] **Modules & imports**  —  `import`, `from ... import`, your own module · Source: [`01_modules_library.py`](01-python/02-modules-and-files/01_modules_library.py), [`my_module.py`](01-python/02-modules-and-files/my_module.py)
  - *Why it matters later:* Package layout of real services
- [x] **Standard library tour**  —  stdlib modules, third-party packages · Source: [`02_modules_library_2.py`](01-python/02-modules-and-files/02_modules_library_2.py)
  - *Why it matters later:* Stdlib in real services
- [x] **Reading & writing files**  —  `open()`, file modes, `with` blocks, copying files · Source: [`03_read_write.py`](01-python/02-modules-and-files/03_read_write.py)
  - *Why it matters later:* Config files, logs, and dataset loading
- [ ] **Logging**
  - *Why it matters later:* Observability in services and agents

</details>

### Part 3 · 🧩 Object-oriented code — 93%

<details>
<summary><b>1.3 · Classes &amp; Abstraction</b> — 6/7 topics</summary>

_Bundling data and behaviour into objects._ · 📂 [`01-python/03-oop/`](01-python/03-oop)

- [x] **Classes & instances**  —  `__init__`, instance attributes · Source: [`01_classes_instances.py`](01-python/03-oop/01_classes_instances.py)
  - *Why it matters later:* Models, clients, and service objects
- [x] **Class variables**  —  shared state, class vs instance attributes · Source: [`02_class_variables.py`](01-python/03-oop/02_class_variables.py)
  - *Why it matters later:* Shared config and registries
- [x] **Class & static methods**  —  `@classmethod`, `@staticmethod` · Source: [`03_classmethods_staticmethods.py`](01-python/03-oop/03_classmethods_staticmethods.py)
  - *Why it matters later:* Alternate constructors, e.g. Model.from_config()
- [x] **Inheritance**  —  `super()`, overriding · Source: [`04_inheritance.py`](01-python/03-oop/04_inheritance.py)
  - *Why it matters later:* Base provider classes for LLM vendors
- [x] **Special methods**  —  `__repr__`, dunder methods · Source: [`05_special_methods.py`](01-python/03-oop/05_special_methods.py)
  - *Why it matters later:* Readable logs and debuggable objects
- [x] **Property decorator**  —  `@property`, getters and setters · Source: [`06_property_decorator.py`](01-python/03-oop/06_property_decorator.py)
  - *Why it matters later:* Validated fields, as in Pydantic
- [/] **Composition**  —  has-a vs is-a
  - *Why it matters later:* Agents composed of tools, memory, and a model

</details>

### Part 4 · 🛠️ Intermediate Python — 85%

<details>
<summary><b>1.4 · Real-world Plumbing</b> — 8/10 topics</summary>

_The language features that frameworks are built on._ · 📂 [`01-python/04-intermediate/`](01-python/04-intermediate)

- [x] **First-class functions**  —  functions as values, passing functions around · Source: [`01_first_class_functions.py`](01-python/04-intermediate/01_first_class_functions.py)
  - *Why it matters later:* Pluggable model and tool strategies
- [x] **Closures**  —  enclosing scope, factory functions · Source: [`02_closures.py`](01-python/04-intermediate/02_closures.py)
  - *Why it matters later:* Configured clients and per-request handlers
- [x] **Decorators**  —  wrapping functions, `functools.wraps` · Source: [`03_decorators.py`](01-python/04-intermediate/03_decorators.py)
  - *Why it matters later:* FastAPI routes, tracing, and auth checks
- [x] **Decorators with arguments**  —  decorator factories · Source: [`04_decorators_with_arguments.py`](01-python/04-intermediate/04_decorators_with_arguments.py)
  - *Why it matters later:* Retries, rate limits, and permissions as `@decorator(...)`
- [x] **Iterators & iterables**  —  `__iter__`, `__next__` · Source: [`05_iterators_iterables.py`](01-python/04-intermediate/05_iterators_iterables.py)
  - *Why it matters later:* Streaming responses and paginated APIs
- [x] **Generators**  —  `yield`, lazy evaluation · Source: [`06_generators.py`](01-python/04-intermediate/06_generators.py)
  - *Why it matters later:* Streaming tokens and large-file processing
- [x] **Exception handling**  —  try/except/finally, custom exceptions · Source: [`07_exception_handling.py`](01-python/04-intermediate/07_exception_handling.py)
  - *Why it matters later:* API error responses and retry logic
- [x] **Type hints**  —  annotations, `Optional` and unions · Source: [`08_type_hints.py`](01-python/04-intermediate/08_type_hints.py)
  - *Why it matters later:* Typed API contracts and Pydantic models
- [/] **Async I/O**  —  `async` / `await`, event loop · Source: [`09_async_io.py`](01-python/04-intermediate/09_async_io.py)
  - *Why it matters later:* Concurrent model and tool calls
- [ ] **Validation**  —  dataclasses, Pydantic
  - *Why it matters later:* Structured outputs from models

</details>

### Part 5 · 🚀 Small applications — 100%

<details>
<summary><b>1.5 · Mental-Bridge Applications</b> — 10/10 topics</summary>

_Ten small scenarios that connect syntax to systems._ · 📂 [`01-python/05-applied-exercises/`](01-python/05-applied-exercises)

- [x] **01 Zip & dictionary mapping**  —  zip, filtering · Source: [`01_zip_dictionary_mapping.py`](01-python/05-applied-exercises/01_zip_dictionary_mapping.py), [`01_zip_dictionary_mapping_solution.py`](01-python/05-applied-exercises/01_zip_dictionary_mapping_solution.py)
  - *Why it matters later:* Authorization and tool access
- [x] **02 Set permissions**  —  set ops · Source: [`02_set_permissions.py`](01-python/05-applied-exercises/02_set_permissions.py)
  - *Why it matters later:* Permission checks
- [x] **03 Filter users**  —  predicates · Source: [`03_filter_users.py`](01-python/05-applied-exercises/03_filter_users.py)
  - *Why it matters later:* Query-like selection / metadata retrieval
- [x] **04 Transform API data**  —  map · Source: [`04_transform_api_data.py`](01-python/05-applied-exercises/04_transform_api_data.py)
  - *Why it matters later:* API response shaping
- [x] **05 Group users by role**  —  grouping · Source: [`05_group_users_by_role.py`](01-python/05-applied-exercises/05_group_users_by_role.py)
  - *Why it matters later:* Aggregation and reporting
- [x] **06 JSON data processing**  —  json · Source: [`06_json_data_processing.py`](01-python/05-applied-exercises/06_json_data_processing.py)
  - *Why it matters later:* External data boundaries
- [x] **07 Function as data**  —  callbacks · Source: [`07_function_as_data.py`](01-python/05-applied-exercises/07_function_as_data.py)
  - *Why it matters later:* Pluggable model/tool strategies
- [x] **08 Decorator logging**  —  decorators · Source: [`08_decorator_logging.py`](01-python/05-applied-exercises/08_decorator_logging.py)
  - *Why it matters later:* Tracing and observability
- [x] **09 Generator data**  —  yield · Source: [`09_generator_large_data.py`](01-python/05-applied-exercises/09_generator_large_data.py)
  - *Why it matters later:* Streaming and memory efficiency
- [x] **10 Error-handling pipeline**  —  try/except · Source: [`10_error_handling_pipeline.py`](01-python/05-applied-exercises/10_error_handling_pipeline.py)
  - *Why it matters later:* Resilient processing

</details>

### Part 6 · 🏗️ Backend engineering — 3%

<details>
<summary><b>2.1 · HTTP &amp; APIs</b> — 0/3 topics</summary>

_How clients and servers talk: requests, responses and status codes._ · 📂 [`02-backend/01-http-and-apis/`](02-backend/01-http-and-apis)

- [ ] **HTTP basics**  —  requests and responses, status codes, headers
  - *Why it matters later:* Calling LLM provider APIs
- [ ] **REST design**  —  resources, verbs, pagination
  - *Why it matters later:* Tool and webhook APIs
- [/] **Handlers & pipelines**  —  handlers, pipelines
  - *Why it matters later:* FastAPI services

</details>

<details>
<summary><b>2.2 · FastAPI</b> — 0/3 topics</summary>

_Serving Python functions over HTTP._ · 📂 [`02-backend/02-fastapi/`](02-backend/02-fastapi)

- [ ] **First FastAPI service**  —  routes, path and query parameters
  - *Why it matters later:* Serving models and RAG endpoints
- [ ] **Request & response models**  —  Pydantic models, validation errors
  - *Why it matters later:* Structured LLM outputs
- [ ] **Dependencies & middleware**  —  dependency injection, middleware
  - *Why it matters later:* Auth, logging, and rate-limiting layers

</details>

<details>
<summary><b>2.3 · Databases</b> — 0/3 topics</summary>

_Storing and querying data reliably._ · 📂 [`02-backend/03-databases/`](02-backend/03-databases)

- [ ] **SQL basics**  —  tables, joins, indexes
  - *Why it matters later:* Metadata and application data
- [ ] **SQLAlchemy**  —  models, sessions
  - *Why it matters later:* Repository-style data access
- [ ] **Redis & caching**  —  key-value, TTL
  - *Why it matters later:* Caching LLM responses and rate limits

</details>

<details>
<summary><b>2.4 · Auth &amp; Security</b> — 0/2 topics</summary>

_Knowing who is calling and what they may do._ · 📂 [`02-backend/04-auth-and-security/`](02-backend/04-auth-and-security)

- [ ] **Authentication**  —  password hashing, JWT
  - *Why it matters later:* API keys and user sessions
- [ ] **Authorization**  —  roles, permissions, multi-tenancy
  - *Why it matters later:* Access control for RAG and agent tools

</details>

<details>
<summary><b>2.5 · Testing</b> — 0/2 topics</summary>

_Proving the code works before users find out it doesn't._ · 📂 [`02-backend/05-testing/`](02-backend/05-testing)

- [ ] **pytest basics**  —  asserts, fixtures
  - *Why it matters later:* Regression tests for prompts and pipelines
- [ ] **Mocking & API tests**  —  mocks, test client
  - *Why it matters later:* Testing LLM calls without paying for them

</details>

<details>
<summary><b>2.6 · Docker &amp; Deployment</b> — 0/3 topics</summary>

_Packaging and shipping a service._ · 📂 [`02-backend/06-docker-and-deployment/`](02-backend/06-docker-and-deployment)

- [ ] **Docker basics**  —  images, containers
  - *Why it matters later:* Reproducible AI services
- [ ] **Config & secrets**  —  environment variables, `.env` files
  - *Why it matters later:* Keeping API keys out of code
- [ ] **CI/CD**  —  GitHub Actions
  - *Why it matters later:* Automated tests and deploys

</details>

### Part 7 · 📈 ML fundamentals — 0%

<details>
<summary><b>3.1 · NumPy &amp; pandas</b> — 0/2 topics</summary>

_Working with arrays and tables of data._ · 📂 [`03-llm-rag-agents/01-ml-foundations/01-numpy-and-pandas/`](03-llm-rag-agents/01-ml-foundations/01-numpy-and-pandas)

- [ ] **NumPy arrays**  —  arrays, vectorised maths
  - *Why it matters later:* Embeddings are just vectors
- [ ] **pandas DataFrames**  —  load, clean, group
  - *Why it matters later:* Dataset prep and evaluation tables

</details>

<details>
<summary><b>3.1 · Model basics</b> — 0/2 topics</summary>

_What it means for a model to learn, and how to tell if it did._ · 📂 [`03-llm-rag-agents/01-ml-foundations/02-model-basics/`](03-llm-rag-agents/01-ml-foundations/02-model-basics)

- [ ] **Train, test & evaluate**  —  data splits, metrics
  - *Why it matters later:* Evaluation mindset for LLM systems
- [ ] **Simple models**  —  scikit-learn, overfitting
  - *Why it matters later:* Understanding what a model actually learns

</details>

### Part 8 · 🤖 LLM / RAG / agents — 0%

<details>
<summary><b>3.2 · LLM Basics</b> — 0/2 topics</summary>

_Talking to a model from code._ · 📂 [`03-llm-rag-agents/02-llm-basics/`](03-llm-rag-agents/02-llm-basics)

- [ ] **LLM APIs & prompting**  —  chat messages, system prompts, parameters
  - *Why it matters later:* Every AI feature starts here
- [ ] **Structured output**  —  JSON output, schema validation
  - *Why it matters later:* Reliable parsing of model responses

</details>

<details>
<summary><b>3.3 · Embeddings &amp; Vector Search</b> — 0/2 topics</summary>

_Turning text into vectors and finding what is similar._ · 📂 [`03-llm-rag-agents/03-embeddings-and-vector-search/`](03-llm-rag-agents/03-embeddings-and-vector-search)

- [ ] **Embeddings**  —  text to vectors, similarity
  - *Why it matters later:* Semantic search and clustering
- [ ] **Vector search**  —  nearest neighbours, metadata filters
  - *Why it matters later:* Retrieval for RAG

</details>

<details>
<summary><b>3.4 · RAG</b> — 0/2 topics</summary>

_Giving a model the right knowledge at the right time._ · 📂 [`03-llm-rag-agents/04-rag/`](03-llm-rag-agents/04-rag)

- [ ] **Chunking & retrieval**  —  splitting documents, top-k, metadata filtering
  - *Why it matters later:* Document Q&A over private data
- [ ] **RAG pipeline**  —  retrieve, augment, generate
  - *Why it matters later:* End-to-end grounded answers

</details>

<details>
<summary><b>3.5 · Agents &amp; Tool Use</b> — 0/3 topics</summary>

_Letting a model call functions and make decisions in a loop._ · 📂 [`03-llm-rag-agents/05-agents-and-tool-use/`](03-llm-rag-agents/05-agents-and-tool-use)

- [ ] **Function calling**  —  tool schemas, tool permissions
  - *Why it matters later:* Models that act, not just talk
- [ ] **Agent loop**  —  plan, act, observe, memory
  - *Why it matters later:* Multi-step task automation
- [ ] **MCP tools**  —  servers, tools and resources
  - *Why it matters later:* Standard way to plug tools into models

</details>

### Part 9 · 🛡️ Production AI — 0%

<details>
<summary><b>3.6 · Evaluation &amp; Observability</b> — 0/3 topics</summary>

_Knowing whether an AI system is good, and seeing what it does in production._ · 📂 [`03-llm-rag-agents/06-evaluation-and-observability/`](03-llm-rag-agents/06-evaluation-and-observability)

- [ ] **Evaluation**  —  test sets, LLM-as-judge
  - *Why it matters later:* Catching regressions before users do
- [ ] **Tracing & observability**  —  logs, traces, cost tracking
  - *Why it matters later:* Debugging agents and RAG in production
- [ ] **Guardrails & safety**  —  input checks, output validation
  - *Why it matters later:* Safe tool use and data access

</details>
<!--BOOK:END-->


## 🧪 Projects and the Concepts They Use


<!--PROJECTS:START-->
- ✅ [**Personal Expense CLI**](01-python/projects/personal_expense_cli) — *done*
  - Track expenses from the terminal, stored as JSON.
  - **Concepts:** Dictionaries _(Data, Logic & Functions)_, Functions _(Data, Logic & Functions)_, Reading & writing files _(Modules, Libraries & Files)_, Exception handling _(Real-world Plumbing)_, 06 JSON data processing _(Mental-Bridge Applications)_
- 💡 [**Smart File Organizer**](01-python/projects/smart_file_organizer) — *planned*
  - Sort a messy folder into tidy categories.
  - **Concepts:** Reading & writing files _(Modules, Libraries & Files)_, Conditionals & booleans _(Data, Logic & Functions)_, Modules & imports _(Modules, Libraries & Files)_
<!--PROJECTS:END-->


## 🧠 The Core Mental Model


**How Python concepts evolve into real-world engineering systems:**

Data structures → Records → Filtering → Functions → Modules → Backend services → AI systems → Production AI

| Python idea | Becomes |
| --- | --- |
| Dictionary mapping | Authorization |
| Filter | Metadata retrieval |
| Generator | Streaming |
| Decorator | Logging / tracing |
| Exception handler | Resilient processing |
| Function passed as data | Model or tool strategy |


## 🧭 Repository Guide


```text
.
├── 01-python/             Python foundations, OOP, intermediate topics, projects
├── 02-backend/            HTTP, APIs, databases, auth, testing, deployment
├── 03-llm-rag-agents/     ML foundations, LLMs, embeddings, RAG, agents, evaluation
├── docs/                  mental models and mental bridges
├── scripts/               README and dashboard generator
├── assets/                header and dashboard graphics
└── journey.json           single source of truth for learning progress
```


- [Python mental models](docs/mental-models/python_mental_models.md): the ideas behind the progression

- [Mental model map](docs/mental-models/python_mental_model_map.md): syntax to systems

- [Mental bridges](docs/mental-bridges/README.md): realistic scenarios that connect small patterns to real systems


Run any file from the repo root, for example:


```bash

python 01-python/05-applied-exercises/01_zip_dictionary_mapping.py

```


## 🔄 How to update


1\. Change a topic's `status` in `journey.json` to `done`, `wip`, or `todo` (`wip` counts as half).

2\. Add a topic to a chapter's `topics` list. File paths are written from the repo root; use `also` for extra files:

   ```json

   {"name": "Generators", "status": "done", "subtopics": ["`yield`"],

    "future": "Streaming tokens", "file": "01-python/04-intermediate/06_generators.py"}

   ```

3\. Add a chapter under a track's `chapters` with its `folder`, e.g. `"folder": "02-backend/02-fastapi"`. It appears automatically in that folder's README.

4\. Add a project under `projects`. Each `concepts` entry must match a topic name exactly:

   ```json

   {"name": "Tool router", "path": "03-llm-rag-agents/projects/tool_router", "status": "building",

    "concepts": ["Inheritance", "10 Error-handling pipeline"]}

   ```

5\. Run `python scripts/build_readme.py` locally, or just push: the GitHub Action does it for you. The script prints warnings for files that are missing or not listed in `journey.json`.


## ⭐ North Star


```text

Learn a concept. Use it in a realistic problem.

Recognize the larger system it belongs to. Build the next layer.

```
