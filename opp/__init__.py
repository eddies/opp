# -*- coding: future_fstrings -*-

def hello(name = "Treach"):
    """Hello, world

    Args:
        name (str): Who's down with O.P.P.?

    >>> print hello(Kay Gee)
        Kay Gee down with O.P.P. (Yeah, you know me!)
    """
    return f"{name} down with O.P.P. (Yeah, you know me!)"