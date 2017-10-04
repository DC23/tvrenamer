# -*- coding: utf-8 -*-
""" tvdb-renamer: TV show file renamer
"""

import logging
import logging.config
import os
from glob import glob

from .configuration import (
    get_configuration,
    get_config_file,
    copy_default_config_to_user_directory)
from .metadata import __author__, __email__, __version__
from .tvdb_scraper import read_show_html, parse_show_data

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

    if config.dry_run:
        print('**** Dry run, no files changed')

    try:
        # get show data
        title, html = read_show_html(config.showid)
        data = parse_show_data(html)
        print('**** {0} ****'.format(title))
        if config.verbose:
            print(data)

        # Parse the files
        print('Scanning for files at {0}'.format(config.path))
        search_path = os.path.join(config.path, '*')
        for file in glob(search_path):
            base, ext = os.path.splitext(file)
            basename = os.path.basename(base)
            directory = os.path.dirname(file)
            if config.verbose:
                print('Checking {0}'.format(basename))

            # match = p.match(os.path.basename(basename))
            # if match:
                # name = match.group(1)
                # #print(name)
                # matching_data = get_match(name)
                # if not matching_data:
                    # print('no match for {0}'.format(name))
                # else:
                    # new_name = 's{season:02d}-e{episode:03d}-{name}'.format(
                        # season=matching_data['season'],
                        # episode=matching_data['episode'],
                        # name=matching_data['name'])

                    # new_name = os.path.join(directory, new_name) + ext
                    # print('{0} --> {1}'.format(file, new_name))
                    # if not dry_run:
                        # os.rename(file, new_name)

    except Exception as exception:
        logging.getLogger(__name__).error(exception, exc_info=True)

    logging.getLogger(__name__).info("Exiting")


if __name__ == 'main':
    start_cli()
