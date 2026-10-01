"""
Materials Science Search Indexer — A search indexer for crystal lattice and alloy properties.

This module contains documentation and metadata for the project.
"""

__title__ = "materials_science_indexer"
__version__ = "1.0.0"
__author__ = "Your Name <your@email.com>"
__license__ = "MIT License"
__copyright__ = f"Copyright {datetime.now().year} {__author__}"

"""
Project Description
-------------------

The Materials Science Search Indexer is an inverted-index search engine with ranking.
It's designed to efficiently search and retrieve crystal lattice and alloy properties.

"""

__doc__ = __title__

def get_project_info():
    """Returns project metadata as a dictionary."""
    return {
        "title": __title__,
        "version": __version__,
        "author": __author__,
        "license": __license__,
        "copyright": __copyright__
    }

if __name__ == "__main__":
    print(get_project_info())
