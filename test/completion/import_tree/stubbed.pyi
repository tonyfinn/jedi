from typing import List

x: List[str]
mismatched: List[int]

class Foo:
    x: str

    def __init__(self, k: str) -> None: ...
    def bar(self) -> str: ...

    def stubonly(self, x: float) -> int: ...