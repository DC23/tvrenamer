# -*- coding: utf-8 -*-
""" Configuration and command-line arguments
"""

import argparse

def get_configuration():
    """Parses and returns the program configuration options.
    """
    parser = argparse.ArgumentParser(
        add_help=True)

    parser.add_argument(
        '-t',
        '--threshold',
        required=False,
        default=90,
        type=int,
        help='Similarity threshold for show name fuzzy matching',
        )

    parser.add_argument(
        '-v',
        '--version',
        action='version',                    
        version='%(prog)s (version 0.4.0)')

    parser.add_argument(
        '-vb',
        '--verbose',
        required=False,
        action='store_true',
        help='''Verbose reporting mode''')

    parser.add_argument(
        '-dr',
        '--dry-run',
        required=False,
        action='store_true',
        help='''Conduct a dry run. No changes are written to file''')

    parser.add_argument(
        '-p',
        '--path',
        required=True,
        metavar='DIRECTORY',
        help='''The directory to scan for files''')

    parser.add_argument(
        '-id',
        '--showid',
        required=True,
        type=str,
        help='''TVDB show id for matching episodes''')

    return parser.parse_known_args()[0]
