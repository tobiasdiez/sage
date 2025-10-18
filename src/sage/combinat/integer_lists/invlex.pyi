from typing import Any

class IntegerListsLex(IntegerLists, metaclass=ClasscallMetaclass):
    def __classcall_private__(cls: Any, n: Any = ...) -> Any:
        ...

class IntegerListsBackend_invlex(IntegerListsBackend):
    def __init__(self: Any, check: Any = ...) -> Any:
        ...

class IntegerListsLexIter(builtins.object):
    def __init__(self: Any, backend: Any) -> Any:
        ...
    def __iter__(self: Any) -> Any:
        ...
    def __next__(self: Any) -> Any:
        ...
