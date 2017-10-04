# -*- coding: utf-8 -*-
""" tvdb-renamer: TV show file renamer
"""

# Ensure backwards compatibility with Python 2
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals)
from builtins import *

import logging
import logging.config
import os
from datetime import datetime
from time import sleep

from pkg_resources import Requirement, resource_filename

from .configuration import (
    get_configuration,
    get_config_file,
    copy_default_config_to_user_directory)

from .metadata import __author__, __email__, __version__

def __init_logging(logging_config_file):
    """
    Initialises logging.

    Args:
        logging_config_file (str): The logging configuration file.
        """

    # Make sure the user copy of the logging config file exists
    copy_default_config_to_user_directory(logging_config_file, clobber=False)

    # Load the config
    logging.config.fileConfig(get_config_file(logging_config_file))

def start_cli():
    """ Runs the renamer."""

    config = get_configuration()
    __init_logging(config.logging_config)
    logging.getLogger(__name__).info('renamer version %s', __version__)
    logging.getLogger(__name__).info('verbose mode: %s', config.verbose)

    if config.version:
        return

    try:
        logging.getLogger(__name__).info('todo')

    except Exception as exception:
        logging.getLogger(__name__).error(exception, exc_info=True)

    logging.getLogger(__name__).info("Exiting")


if __name__ == 'main':
    start_cli()
