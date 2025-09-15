from typing import Any, Optional, Union, Iterator, List

def xsrange(
    start: Union[int, float], 
    end: Optional[Union[int, float]] = None, 
    step: Union[int, float] = 1, 
    universe: Optional[Any] = None, 
    coerce: bool = True, 
    include_endpoint: bool = False, 
    endpoint_tolerance: float = 1e-5
) -> Iterator[Any]:
    ...

def srange(
    start: Union[int, float], 
    end: Optional[Union[int, float]] = None, 
    step: Union[int, float] = 1, 
    universe: Optional[Any] = None, 
    coerce: bool = True, 
    include_endpoint: bool = False, 
    endpoint_tolerance: float = 1e-5
) -> List[Any]:
    ...

def ellipsis_iter(step: Union[int, float] = 1) -> Iterator[Any]:
    ...

def ellipsis_range(step: Union[int, float] = 1) -> List[Any]:
    ...
