from typing import Any

class IdempotentSemigroups(Category):
    def super_categories(self: Any) -> Any:
        ...

class ElementMethods:
    def is_idempotent(self: Any) -> Any:
        ...

class LeftZeroSemigroupElement(Element):
    def __init__(self: Any, parent: Any, value: Any) -> Any:
        ...
    def __reduce__(self: Any) -> Any:
        ...
    def __pow__(self: Any, i: Any, dummy: Any) -> Any:
        ...

class LeftZeroSemigroup(LeftZeroSemigroupPython):
    def __init__(self: Any) -> Any:
        ...
