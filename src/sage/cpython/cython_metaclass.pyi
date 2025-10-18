from typing import Any

class MyCustomType:
    def __getmetaclass__(_: Any) -> Any:
        ...
