from typing import Any, Optional, Union, List, Dict, Callable
from sage.structure.global_options import GlobalOptions

def matrix(
    base_ring: Optional[Any] = None,
    nrows: Optional[Union[int, Any]] = None, 
    ncols: Optional[Union[int, Any]] = None,
    entries: Optional[Union[List, Dict, Callable, Any]] = None,
    *,
    sparse: Optional[bool] = None,
    row_keys: Optional[Any] = None,
    column_keys: Optional[Any] = None, 
    space: Optional[Any] = None,
    immutable: bool = False,
    **kwds: Any
) -> Any:
    ...

class options(GlobalOptions):
    ...
