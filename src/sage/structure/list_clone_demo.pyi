from typing import Any

class IncreasingArray(ClonableArray):
    def check(self: Any) -> Any:
        ...

class IncreasingArrays(UniqueRepresentation, Parent):
    def __init__(self: Any) -> Any:
        ...

class IncreasingLists(IncreasingArrays):
    ...

class IncreasingList(ClonableList):
    def check(self: Any) -> Any:
        ...

class IncreasingIntArray(ClonableIntArray):
    def check(self: Any) -> Any:
        ...

class IncreasingIntArrays(IncreasingArrays):
    ...

class SortedList(NormalizedClonableList):
    def normalize(self: Any) -> Any:
        ...
    def check(self: Any) -> Any:
        ...

class SortedLists(IncreasingLists):
    ...
