from typing import Any

class MatrixMulAction(Action):
    def __init__(self: Any, G: Any, S: Any, is_left: Any) -> Any:
        ...
    def codomain(self: Any) -> Any:
        ...

class MatrixMatrixAction(MatrixMulAction):
    def __init__(self: Any, G: Any, S: Any) -> Any:
        ...

class MatrixVectorAction(MatrixMulAction):
    def __init__(self: Any, G: Any, S: Any) -> Any:
        ...

class VectorMatrixAction(MatrixMulAction):
    def __init__(self: Any, G: Any, S: Any) -> Any:
        ...

class MatrixPolymapAction(MatrixMulAction):
    def __init__(self: Any, G: Any, S: Any) -> Any:
        ...

class PolymapMatrixAction(MatrixMulAction):
    def __init__(self: Any, G: Any, S: Any) -> Any:
        ...

class MatrixSchemePointAction(MatrixMulAction):
    def __init__(self: Any, G: Any, S: Any) -> Any:
        ...
