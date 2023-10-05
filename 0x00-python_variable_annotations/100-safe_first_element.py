#!/usr/bin/env python3
"""
Duck type annotations ddddddddddddddddddddddddddddddddddddddddddddd
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[None, Any]:
    """return first item of list dddddddd"""
    if lst:
        return lst[0]
    else:
        return None
