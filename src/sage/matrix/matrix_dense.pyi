from typing import Any
import sage.matrix.matrix

class Matrix_dense(sage.matrix.matrix.Matrix):
    def __copy__(self) -> "Matrix_dense":
        ...
    def transpose(self) -> "Matrix_dense":
        ...
    def antitranspose(self) -> "Matrix_dense":
        ...
