# -*- coding: utf-8 -*-
import pytest

from tvrenamer.tvdb_scraper import parse_show_data

html = b'<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center" id="listtable">&#13;\n\t\t<tr>&#13;\n\t\t<td class="head">Episode Number</td>&#13;\n\t\t\t<td class="head">Episode Name</td>&#13;\n\t\t\t<td class="head">Originally Aired</td>&#13;\n\t\t\t<td class="head">Image</td>&#13;\n\t\t</tr>&#13;\n<tr><td class="special"><a href="/index.php?tab=episode&amp;seriesid=213081&amp;seasonid=374121&amp;id=4061921">Special</a></td><td class="special"><a href="/index.php?tab=episode&amp;seriesid=213081&amp;seasonid=374121&amp;id=4061921">Pilot</a></td><td class="special">2010-12-16</td><td class="special"><img src="/images/checkmark.png" width="10" height="10" /></td></tr>\n<tr><td class="even"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=3298371&amp;lid=7">1 x 1</a></td><td class="even"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=3298371&amp;lid=7">Episode 1</a></td><td class="even">2012-03-05</td><td class="even"><img src="/images/checkmark.png" width="10" height="10" /> &#160;</td></tr>\n<tr><td class="odd"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=4272600&amp;lid=7">1 x 2</a></td><td class="odd"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=4272600&amp;lid=7">Episode 2</a></td><td class="odd">2012-03-12</td><td class="odd"><img src="/images/checkmark.png" width="10" height="10" /> &#160;</td></tr>\n<tr><td class="even"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=4272601&amp;lid=7">1 x 3</a></td><td class="even"><a href="/?tab=episode&amp;seriesid=213081&amp;seasonid=374131&amp;id=4272601&amp;lid=7">Episode 3</a></td><td class="even">2012-03-19</td><td class="even"><img src="/images/checkmark.png" width="10" height="10" /> &#160;</td></tr>\n\t</table>&#13;\n'

data = parse_show_data(html)

def test_episode_count():
    assert len(data) == 4

def test_column_names():
    assert len(data.columns) == 4
    assert 'name' in data.columns
    assert 'season' in data.columns
    assert 'episode' in data.columns
    assert 'aired' in data.columns

def test_column_dtypes():
    assert data['name'].dtype == object
    assert data['season'].dtype == int
    assert data['episode'].dtype == int

def test_special_numbering():
    assert data[data.name == 'Pilot'].episode[0] == 1

