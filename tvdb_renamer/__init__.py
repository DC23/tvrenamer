# -*- coding: utf-8 -*-
""" TVDB Heuristic File Renamer

    TV show file renamer that pulls data from TVDB, using heuristics to match files to episodes.
"""

from .metadata import __author__, __email__, __version__
from .tvdb_renamer import start_cli
