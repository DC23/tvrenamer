# -*- coding: utf-8 -*-
import pytest

from tvrenamer.episode_matcher import get_best_match
from tvrenamer.tvdb_scraper import parse_show_data

html = b'<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center" id="listtable">&#13;\n\t\t<tr>&#13;\n\t\t<td class="head">Episode Number</td>&#13;\n\t\t\t<td class="head">Episode Name</td>&#13;\n\t\t\t<td class="head">Originally Aired</td>&#13;\n\t\t\t<td class="head">Image</td>&#13;\n\t\t</tr>&#13;\n<tr><td class="special"><a href="/index.php?tab=episode&amp;seriesid=213081&amp;seasonid=374121&amp;id=4061921">Special</a></td><td class="special"><a href="/index.php?tab=episode&amp;seriesid=213081&amp;seasonid=374121&amp;id=4061921">Pilot</a></td><td class="special">2010-12-16</td><td class="special"><img src="/images/checkmark.png" width="10" height="10" /></td></tr>\n<tr><td class="even"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=3298371&amp;lid=7">1 x 1</a></td><td class="even"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=3298371&amp;lid=7">Episode 1</a></td><td class="even">2012-03-05</td><td class="even"><img src="/images/checkmark.png" width="10" height="10" /> &#160;</td></tr>\n<tr><td class="odd"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=4272600&amp;lid=7">1 x 2</a></td><td class="odd"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=4272600&amp;lid=7">Episode 2</a></td><td class="odd">2012-03-12</td><td class="odd"><img src="/images/checkmark.png" width="10" height="10" /> &#160;</td></tr>\n<tr><td class="even"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=4272601&amp;lid=7">1 x 3</a></td><td class="even"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=4272601&amp;lid=7">Episode 3</a></td><td class="even">2012-03-19</td><td class="even"><img src="/images/checkmark.png" width="10" height="10" /> &#160;</td></tr>\n\t</table>&#13;\n'

data = parse_show_data(html)

def test_match_episode_one():
    target = 'sode 1'
    match, _ = get_best_match(data, target)
    assert match
    assert match['name'] == 'Episode 1'
    assert match['season'] == 1
    assert match['episode'] == 1

def test_match_episode_two():
    target = 'epsode 2'
    match, _ = get_best_match(data, target)
    assert match['episode'] == 2

def test_match_pilot():
    target = 's00e01 pilot bbc-27'
    match, _ = get_best_match(data, target)
    assert match['name'] == 'Pilot'
