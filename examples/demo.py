"""Demo for Materials Science Search Indexer."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import materials_science_indexer

print("Materials Science Search Indexer", "v" + materials_science_indexer.__version__)
print("modules:", [m for m in dir(materials_science_indexer) if not m.startswith('_')])
