# Materials Science Search Indexer

This is a search indexer designed to efficiently retrieve information about crystal lattices and alloys from large datasets, utilizing a ranking system to prioritize relevant results. Built entirely in Python, this tool includes comprehensive testing and documentation for ease of use and modification. It is an inverted-index search engine capable of handling complex queries with high performance.

## What makes it unique

Combines crystal lattice and alloy properties with an inverted-index search engine with ranking — a niche where few ready-made tools exist.

## Features

- **`materials_science_indexer/search_indexer.py`** — Main class for search index creation and query processing
- **`materials_science_indexer/inverted_index.py`** — Implementation of inverted index data structure
- **`materials_science_indexer/ranker.py`** — Module for ranking search results based on relevance
- **`materials_science_indexer/materials_database.py`** — Database interface for materials science data
- **`materials_science_indexer/test_search_indexer.py`** — Unit tests for search indexer functionality
- **`materials_science_indexer/docs.py`** — Module containing documentation and metadata for the project

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/materials-science-indexer.git
cd materials-science-indexer

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
materials-science-indexer/
├── materials_science_indexer/
│   ├── search_indexer.py
│   ├── inverted_index.py
│   ├── ranker.py
│   ├── materials_database.py
│   ├── test_search_indexer.py
│   ├── docs.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **materials-science** · Archetype: **indexer** ·
Built autonomously by JARVIS on 2026-09-30. MIT licensed.
