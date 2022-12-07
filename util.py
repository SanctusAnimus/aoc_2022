from typing import TypeVar
from collections.abc import Sequence
from functools import reduce
from operator import getitem

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def chunked(src: Sequence[T], size: int) -> list[list[T]]:
    for i in range(0, len(src), size):
        yield src[i:i + size]


def get_nested(src: dict[K, V], keys: Sequence[K]) -> V:
    return reduce(getitem, keys, src)


def set_nested(src: dict[K, V], keys: Sequence[K], value: V):
    for key in keys[:-1]:
        src = src.setdefault(key, {})
    src[keys[-1]] = value
