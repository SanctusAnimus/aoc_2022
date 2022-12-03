from typing import TypeVar
from collections.abc import Sequence

T = TypeVar("T")


def chunked(src: Sequence[T], size: int) -> list[list[T]]:
    for i in range(0, len(src), size):
        yield src[i:i + size]
