# -*- coding: utf-8 -*-
""" tvdb_scraper: scrapes show data from TVDB.
"""

import lxml
import requests
import pandas as pd
from lxml import html

def read_show_html(show_id):
    """
    Scrapes show data from TVDB.

    Args:
        show_id (str): The TVDB show id

    Returns:
        str: The Show title.
        str: The complete HTML table of episode data for the given show.
    """
    url = 'https://www.thetvdb.com/?tab=seasonall&id={id}&lid=7'.format(
        id=show_id)
    page = requests.get(url)
    tree = lxml.html.fromstring(page.content)
    episodes = tree.xpath('//*[@id="listtable"]')[0]
    title = tree.xpath('//*[@id="maincontent"]/div[2]/h1/a')[0].text
    return title, lxml.etree.tostring(episodes)

def parse_show_data(html):
    """
    Parses TVDB show data from a HTML string.

    Args:
        html (str): The complete HTML table of episode data for the given show.

    Returns:
        pandas.DataFrame: Dataframe containing the following columns:
            - name (str): the episode name
            - season (int): the episode season. 0 indicates specials
            - episode (int): the episode number
            - aired (date): The original air date
    """

    data = pd.read_html(
        html,
        header=0,
        parse_dates=[2])[0]

    # remove and rename columns
    del data['Image']
    data.rename(
        inplace=True,
        columns=
        {
            'Episode Number': 'ep_num', 
            'Episode Name': 'name',
            'Originally Aired': 'aired',
        })

    # parse season and episode numbers
    def season(row):
        season = row['ep_num'].split('x')[0].strip().lower()
        if season == 'special':
            return 0
        else:
            return int(season)

    def episode(row):
        split = row['ep_num'].split('x')
        if len(split) > 1:
            return int(split[1].strip().lower())
        else:
            return 0

    data['season'] = data.apply(season, axis=1)
    data['episode'] = data.apply(episode, axis=1)

    # Don't need this any more
    del data['ep_num']

    # take a copy so we can modify the data frame while iterating
    df = data.copy()
    special_episode = 0
    for i, row in df.iterrows():
        if row.season == 0:
            special_episode += 1
            data.loc[i, 'episode'] = special_episode

    return data
