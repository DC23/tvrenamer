# -*- coding: utf-8 -*-
""" Heuristic TV File Renamer

    TV show file renamer that pulls data from TVDB, using heuristics to match files to episodes.
"""

from .metadata import __author__, __email__, __version__
from .tvrenamer import start_cli
