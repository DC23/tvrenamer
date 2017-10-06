# -*- coding: utf-8 -*-
""" episode_matcher: Functions for selecting the best episode match
"""

from fuzzywuzzy import fuzz


def get_best_match(data, name):
    """ Finds the best match for an episode name in the data table.

    Args:
        data (pandas.DataFrame): The TV show data table
        name (str): the episode name to match

    Returns:
        dict: contains the season, episode, and name of the best match
        int: the similarity ratio for the best match
    """
    best_ratio = 0
    best_index = None
    for row in data.itertuples(index=True):
        ratio = fuzz.partial_ratio(row.name, name)
        if ratio >= best_ratio:
            best_ratio = ratio
            best_index = row.Index
            
    m = {
        'season': data.iloc[best_index]['season'],
        'episode': data.iloc[best_index]['episode'],
        'name': data.iloc[best_index]['name'],
        }
                                   
    return m, best_ratio
