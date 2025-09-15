# Python Type Stubs for Sage Cython Modules

This directory contains Python type stub files (`.pyi`) for all Cython modules (`.pyx`) in the Sage library. These stub files provide type information that can be used by static type checkers like mypy, PyCharm, and other tools that support Python typing.

## What are Type Stub Files?

Type stub files (`.pyi`) are files that contain only type information for Python modules. They are used by static type checkers to understand the types of functions, classes, and variables in modules, especially when the actual implementation is in C/C++ or Cython code that doesn't contain explicit type annotations.

## Generated Files

The type stub files in this repository were automatically generated using the `tools/generate_pyi.py` script. This script analyzes Cython source code and extracts:

- Function signatures with parameter types and return types
- Class definitions with inheritance relationships  
- Method definitions within classes
- Basic type mappings from Cython types to Python types

## Usage

These `.pyi` files are meant to be used by static type checkers and IDEs, not imported directly in Python code. They work automatically when:

1. **Using mypy**: The type checker will automatically find and use `.pyi` files alongside `.pyx` files
2. **Using PyCharm/VS Code**: IDEs will use the stub files for autocompletion and type checking
3. **Using other type checkers**: Most modern Python type checkers support stub files

### Example with mypy

```bash
# Type check a Python file that imports Sage modules
mypy your_script.py
```

The type checker will use the `.pyi` files to understand the types of Sage objects and methods.

## Type Aliases

The `src/sage/typing_aliases.py` module provides common type aliases for Sage mathematical objects:

```python
from sage.typing_aliases import Integer, Matrix, Vector, Element

def my_function(x: Integer, m: Matrix) -> Vector:
    # Your code here
    pass
```

## Common Types

The most frequently used Sage types include:

- `Integer`: Sage integers (arbitrary precision)
- `Rational`: Sage rational numbers  
- `RealNumber`: Sage real numbers
- `ComplexNumber`: Sage complex numbers
- `Matrix`: Sage matrices
- `Vector`: Sage vectors
- `Element`: Base class for all Sage algebraic elements
- `Parent`: Base class for Sage algebraic structures

## Limitations

The automatically generated stub files have some limitations:

1. **Generic types**: Most types are annotated as `Any` for simplicity
2. **Complex signatures**: Some complex Cython signatures may not be perfectly represented
3. **Template types**: Cython template-like constructs are simplified
4. **Private methods**: Methods starting with `_` (except `__special__` methods) are excluded

## Regenerating Stub Files

To regenerate all stub files after changes to Cython code:

```bash
cd /path/to/sage
python3 tools/generate_pyi.py --all
```

To generate stub files for specific modules:

```bash
python3 tools/generate_pyi.py  # Generates first 10 files as test
```

## Contributing

When adding new Cython modules to Sage, consider running the generation script to create corresponding `.pyi` files. This helps maintain type checking support across the entire codebase.

## Technical Details

The type stub generation process:

1. Parses Cython `.pyx` files using regular expressions
2. Extracts function and class definitions
3. Maps Cython types to Python typing annotations
4. Generates syntactically correct Python stub files
5. Validates the generated files for syntax errors

The generator handles:
- `cdef class` definitions
- `cpdef` and `def` function definitions  
- Function parameters with default values
- Basic inheritance relationships
- Cython-specific syntax like `not None` type constraints