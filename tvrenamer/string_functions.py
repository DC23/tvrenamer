# -*- coding: utf-8 -*-
""" string_functions: String manipulation functions
"""

import re

def strip_text(text, pattern='.* ?- ?(.*) (Abc Iview)?.*'):
    """
    Strips text matching the pattern from the string.

    Args:
        text (str): the string to clean
        pattern (str): the regex pattern for matching the text to remove. This
            pattern needs to define a single capture that defines the text to
            keep.

    Returns: the matched substring, or the original string if no pattern matches
        were made.  """

    match = re.match(pattern, text)
    if match:
        return match.group(1)
    return text
