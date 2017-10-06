# -*- coding: utf-8 -*-
""" tvdb-renamer: TV show file renamer
"""

import os
from glob import glob

from .configuration import get_configuration
from.episode_matcher import get_best_match
from .metadata import __author__, __email__, __version__
from .tvdb_scraper import read_show_html, parse_show_data

def start_cli():
    """ Runs the renamer."""

    config = get_configuration()
    print('version {0}'.format(__version__))

    if config.dry_run:
        print('**** Dry run, no files changed ****')

    # get show data
    title, html = read_show_html(config.showid)
    data = parse_show_data(html)
    print('**** {0} ****'.format(title))
    if config.verbose:
        print(data)

    # Parse the files
    print('Scanning for files at {0}'.format(config.path))
    search_path = os.path.join(config.path, '*')
    for f in glob(search_path):
        base, ext = os.path.splitext(f)
        basename = os.path.basename(base)
        directory = os.path.dirname(f)

        best_match, best_ratio = get_best_match(data, basename)
        if best_match:
            new_name = 's{season:02d}-e{episode:03d}-{title}-{name}'.format(
                season=best_match['season'],
                episode=best_match['episode'],
                title=title,
                name=best_match['name'])

            if basename == new_name:
                if config.verbose:
                    print('    Already named correctly')
                continue

            print('\nChecking {0}'.format(basename))

            if best_ratio >= config.threshold:
                print('    Similarity score: {0}'.format(best_ratio))
                print('    --> {0}'.format(new_name))
                if not config.dry_run:
                    new_name = os.path.join(directory, new_name) + ext
                    os.rename(f, new_name)
            else:
                print('    Below threshold')
                print('    Similarity score: {0}'.format(best_ratio))
                print('    Best Match: {0}'.format(new_name))
        else:
            print('    no match')

if __name__ == 'main':
    start_cli()
