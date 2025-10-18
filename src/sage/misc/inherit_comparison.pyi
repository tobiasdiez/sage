from typing import Any

class InheritComparisonMetaclass(type):
    def __init__(self: Any) -> Any:
        ...

class InheritComparisonClasscallMetaclass(ClasscallMetaclass, InheritComparisonMetaclass):
    ...
