#!/usr/bin/env python3
"""Duck type annotations ddddddddddddddddddddddddddddddddddddddddddddd"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return first item of list dddddddd"""
    if lst:
        return lst[0]
    else:
        return None
