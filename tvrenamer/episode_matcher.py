# -*- coding: utf-8 -*-
""" episode_matcher: Functions for selecting the best episode match
"""

from fuzzywuzzy import fuzz


def get_best_match(data, name, threshold=80):
    """
    """
    best_ratio = 0
    best_index = None
    for row in data.itertuples(index=True):
        ratio = fuzz.partial_ratio(row.name, name)
        if ratio >= best_ratio:
            best_ratio = ratio
            best_index = row.Index
            
    m = {}
    if best_ratio >= threshold:
        m['season'] = data.iloc[best_index]['season']
        m['episode'] = data.iloc[best_index]['episode']
        m['name'] = data.iloc[best_index]['name']
                                   
    return m, best_ratio
