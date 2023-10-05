#!/usr/bin/env python3
"""
Duck type annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[None, Any]:
    if lst:
        return lst[0]
    else:
        return None
