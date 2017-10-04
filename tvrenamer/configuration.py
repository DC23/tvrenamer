# -*- coding: utf-8 -*-
""" Configuration and command-line arguments
"""

import os
import shutil

import configargparse
from pkg_resources import Requirement, resource_filename


def get_config_file(basename):
    """ Looks for a configuration file in 3 locations:

        - the current directory
        - the user config directory (~/.config/tvrenamer)
        - the version installed with the package (using setuptools resource API)

    Args:
        basename (str): The base filename.

    Returns:
        str: The full path to the configuration file.
    """
    locations = [
        os.path.join(os.curdir, basename),
        os.path.join(
            os.path.expanduser("~"),
            ".config",
            "tvrenamer",
            basename),
        resource_filename(
            Requirement.parse("tvrenamer"),
            os.path.join('tvrenamer', basename))
    ]

    for location in locations:
        if os.path.isfile(location):
            return location

def copy_default_config_to_user_directory(
        basename,
        clobber=False,
        dst_dir='~/.config/tvrenamer'):
    """ Copies the default configuration file into the user config directory.

    Args:
        basename (str): The base filename.
        clobber (bool): If True, the default will be written even if a user
            config already exists.
        dst_dir (str): The destination directory.
    """
    dst_dir = os.path.expanduser(dst_dir)
    dst = os.path.join(dst_dir, basename)
    src = resource_filename(
        Requirement.parse("tvrenamer"),
        os.path.join('tvrenamer', basename))

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    if clobber or not os.path.isfile(dst):
        shutil.copy(src, dst)

def get_configuration(basename='tvrenamer.cfg', parents=None):
    """Parses and returns the program configuration options,
    taken from a combination of ini-style config file, and
    command line arguments.

    Args:
        basename (str): The base filename.
        parents (list): A list of ArgumentParser objects whose arguments
            should also be included in the configuration parsing. These
            ArgumentParser instances **must** be instantiated with the
            `add_help` argument set to `False`, otherwise the main
            ArgumentParser instance will raise an exception due to duplicate
            help arguments.

    Returns:
        The options object, and a function that can be called to print the help
        text.
    """
    copy_default_config_to_user_directory(basename)

    parser = configargparse.ArgParser(
        formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter,
        add_help=True,
        parents=parents or [],
        default_config_files=[
            resource_filename(
                Requirement.parse("tvrenamer"),
                os.path.join('tvrenamer', basename)),
            os.path.join(
                os.path.expanduser("~/.config/tvrenamer"),
                basename),
            os.path.join(os.curdir, basename)])

    # logging config file
    parser.add(
        '-lc',
        '--logging-config',
        required=False,
        default='tvrenamer_logging.cfg',
        metavar='FILE',
        env_var='TVRENAMER_LOGGING_CONFIG',
        help='Logging configuration file')

    parser.add(
        '-v',
        '--version',
        required=False,
        action='store_true',
        help='''Display tvrenamer version''')

    parser.add(
        '-vb',
        '--verbose',
        required=False,
        action='store_true',
        help='''Verbose reporting mode''')

    parser.add(
        '-dr',
        '--dry-run',
        required=False,
        action='store_true',
        help='''Conduct a dry run. No changes are written to file''')

    parser.add(
        '-p',
        '--path',
        required=True,
        metavar='DIRECTORY',
        help='''The directory to scan for files''')

    parser.add(
        '-id',
        '--showid',
        required=True,
        type=str,
        help='''TVDB show id for matching episodes''')


    return parser.parse_known_args()[0], parser.print_help
