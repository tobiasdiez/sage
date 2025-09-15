#!/usr/bin/env python3
"""
Script to generate .pyi stub files for Cython .pyx files in the Sage library.

This script analyzes Cython files and creates corresponding Python typing stub files
that provide type information for static type checkers.
"""

import os
import re
import ast
import glob
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple

# Common Sage type mappings
CYTHON_TO_PYTHON_TYPES = {
    # Basic C types
    'int': 'int',
    'long': 'int', 
    'char': 'str',
    'char*': 'str',
    'const char*': 'str',
    'double': 'float',
    'float': 'float',
    'bint': 'bool',
    'void': 'None',
    'size_t': 'int',
    'Py_ssize_t': 'int',
    
    # Python object types
    'object': 'Any',
    'list': 'List[Any]',
    'dict': 'Dict[Any, Any]',
    'tuple': 'Tuple[Any, ...]',
    'str': 'str',
    'bytes': 'bytes',
    
    # Common Sage types - we'll create type aliases for these
    'Integer': 'Integer',
    'Rational': 'Rational', 
    'RealNumber': 'RealNumber',
    'ComplexNumber': 'ComplexNumber',
    'Vector': 'Vector',
    'Matrix': 'Matrix',
    'RingElement': 'RingElement',
    'Element': 'Element',
    'Parent': 'Parent',
    'Ring': 'Ring',
    'Field': 'Field',
    'AlgebraElement': 'AlgebraElement',
    'ModuleElement': 'ModuleElement',
    'GapElement': 'GapElement',
    'MultiplicativeGroupElement': 'MultiplicativeGroupElement',
    'SageObject': 'SageObject',
}

# Common typing imports needed
TYPING_IMPORTS = {
    'Any', 'Dict', 'List', 'Tuple', 'Optional', 'Union', 'Callable', 'Iterator'
}

def extract_imports_from_pyx(content: str) -> Set[str]:
    """Extract import statements from Cython content."""
    imports = set()
    
    # Regular imports
    for match in re.finditer(r'^(?:from\s+[\w.]+\s+)?import\s+([\w\s,.*]+)', content, re.MULTILINE):
        import_list = match.group(1)
        # Handle various import patterns
        if ',' in import_list:
            for item in import_list.split(','):
                item = item.strip()
                if ' as ' in item:
                    item = item.split(' as ')[1].strip()
                imports.add(item)
        else:
            if ' as ' in import_list:
                import_list = import_list.split(' as ')[1].strip()
            imports.add(import_list.strip())
    
    # Cython imports (cimport)
    for match in re.finditer(r'^(?:from\s+[\w.]+\s+)?cimport\s+([\w\s,.*]+)', content, re.MULTILINE):
        import_list = match.group(1)
        if ',' in import_list:
            for item in import_list.split(','):
                item = item.strip()
                if ' as ' in item:
                    item = item.split(' as ')[1].strip()
                imports.add(item)
        else:
            if ' as ' in import_list:
                import_list = import_list.split(' as ')[1].strip()
            imports.add(import_list.strip())
    
    return imports

def parse_function_signature(line: str) -> Optional[Dict[str, str]]:
    """Parse a Cython function definition line."""
    # Match cpdef, cdef, def functions with various return type patterns
    patterns = [
        # Pattern 1: cpdef ReturnType function_name(params):
        r'\s*(cpdef|cdef|def)\s+([^(]+?)\s+(\w+)\s*\((.*?)\)\s*(?:except\s+[^:]*)?:',
        # Pattern 2: def function_name(params):
        r'\s*(def)\s+(\w+)\s*\((.*?)\)\s*(?:except\s+[^:]*)?:',
        # Pattern 3: cpdef function_name(params): (no explicit return type)
        r'\s*(cpdef|cdef)\s+(\w+)\s*\((.*?)\)\s*(?:except\s+[^:]*)?:'
    ]
    
    for i, pattern in enumerate(patterns):
        match = re.match(pattern, line)
        if match:
            if i == 0:  # Pattern 1
                func_type = match.group(1)
                return_type = match.group(2).strip()
                func_name = match.group(3)
                params = match.group(4)
            elif i == 1:  # Pattern 2
                func_type = match.group(1)
                return_type = 'Any'
                func_name = match.group(2)
                params = match.group(3)
            else:  # Pattern 3
                func_type = match.group(1)
                return_type = 'Any'
                func_name = match.group(2)
                params = match.group(3)
            break
    else:
        return None
    
    # Skip private functions starting with underscore (but allow __init__, __new__, etc.)
    if func_name.startswith('_') and not func_name.startswith('__'):
        return None
        
    # Skip cdef functions (they're not accessible from Python)
    if func_type == 'cdef':
        return None
    
    # Special handling for common dunder methods
    special_return_types = {
        '__init__': 'None',
        '__new__': 'Any',
        '__str__': 'str',
        '__repr__': 'str',
        '__hash__': 'int',
        '__len__': 'int',
        '__bool__': 'bool',
        '__bytes__': 'bytes',
        '__reduce__': 'Any',
        '__reduce_ex__': 'Any',
        '__getstate__': 'Any',
        '__setstate__': 'None',
        '__richcmp__': 'Any',
        '__neg__': 'Any',
        '__invert__': 'Any',
        '__abs__': 'Any',
    }
    
    if func_name in special_return_types:
        return_type = special_return_types[func_name]
    
    # Parse parameters
    param_list = []
    if params.strip():
        # Simple parameter parsing - just split by comma and handle basics
        try:
            for param in params.split(','):
                param = param.strip()
                if not param:
                    continue
                    
                # Handle default values
                if '=' in param:
                    param_part, default = param.split('=', 1)
                    param = param_part.strip()
                    default = default.strip()
                else:
                    default = None
                    
                # Enhanced parameter type detection
                param_type = 'Any'
                param_name = param
                
                # Handle Cython-specific syntax like "param not None"
                if ' not None' in param:
                    param = param.replace(' not None', '')
                
                # Try to extract type annotations
                if ' ' in param:
                    parts = param.split()
                    if len(parts) >= 2:
                        # Could be "type name" format
                        potential_type = parts[0]
                        param_name = parts[-1]
                        
                        # Map common Cython types to Python types
                        if potential_type in CYTHON_TO_PYTHON_TYPES:
                            param_type = CYTHON_TO_PYTHON_TYPES[potential_type]
                        elif potential_type in ['bint', 'bool']:
                            param_type = 'bool'
                        elif potential_type in ['int', 'long', 'Py_ssize_t', 'size_t']:
                            param_type = 'int' 
                        elif potential_type in ['double', 'float']:
                            param_type = 'float'
                        elif potential_type in ['str', 'char*', 'const char*']:
                            param_type = 'str'
                        elif potential_type == 'object':
                            param_type = 'Any'
                        else:
                            # Keep the Cython type if it looks like a class name
                            if potential_type[0].isupper():
                                param_type = potential_type
                            else:
                                param_type = 'Any'
                else:
                    # No spaces - just the parameter name
                    param_name = param
                    param_type = 'Any'
                
                # Skip invalid parameter names (like numbers)
                if not param_name.isidentifier():
                    continue
                
                # Special handling for self parameter - don't add type annotation
                if param_name == 'self':
                    if default is not None:
                        param_list.append(f"{param_name} = ...")
                    else:
                        param_list.append(f"{param_name}")
                else:
                    if default is not None:
                        param_list.append(f"{param_name}: {param_type} = ...")
                    else:
                        param_list.append(f"{param_name}: {param_type}")
        except Exception:
            # If parsing fails, just add a generic *args, **kwargs
            param_list = ['*args: Any', '**kwargs: Any']
    
    # Convert return type
    return_type = CYTHON_TO_PYTHON_TYPES.get(return_type, return_type)
    if return_type not in CYTHON_TO_PYTHON_TYPES.values() and return_type not in TYPING_IMPORTS:
        return_type = 'Any'
    
    return {
        'name': func_name,
        'params': param_list,
        'return_type': return_type,
        'type': func_type
    }

def parse_class_definition(line: str) -> Optional[Dict[str, str]]:
    """Parse a Cython or Python class definition line."""
    # Match both cdef class and regular class
    patterns = [
        r'\s*cdef\s+class\s+(\w+)(?:\((.*?)\))?:',  # cdef class
        r'\s*class\s+(\w+)(?:\((.*?)\))?:'          # regular class
    ]
    
    for pattern in patterns:
        match = re.match(pattern, line)
        if match:
            class_name = match.group(1)
            base_classes = match.group(2) if match.group(2) else None
            
            bases = []
            if base_classes:
                for base in base_classes.split(','):
                    base = base.strip()
                    bases.append(base)
            
            return {
                'name': class_name,
                'bases': bases
            }
    
    return None

def generate_pyi_content(pyx_file: str, pyx_content: str) -> str:
    """Generate .pyi content from .pyx file content."""
    lines = pyx_content.split('\n')
    
    # Collect all elements
    functions = []
    classes = []
    current_class = None
    current_class_methods = []
    current_class_indent = 0
    imports = extract_imports_from_pyx(pyx_content)
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Skip empty lines and comments
        if not line.strip() or line.strip().startswith('#'):
            i += 1
            continue
        
        # Calculate indentation level
        indent_level = len(line) - len(line.lstrip())
            
        # Check for class definition
        class_def = parse_class_definition(line)
        if class_def:
            # Save previous class if exists
            if current_class:
                classes.append({
                    'name': current_class['name'],
                    'bases': current_class['bases'],
                    'methods': current_class_methods[:]
                })
            
            current_class = class_def
            current_class_methods = []
            current_class_indent = indent_level
            i += 1
            continue
        
        # Check for function definition
        func_def = parse_function_signature(line)
        if func_def:
            # Determine if this function belongs to the current class
            if current_class and indent_level > current_class_indent:
                current_class_methods.append(func_def)
            else:
                # This is a module-level function, save current class first
                if current_class:
                    classes.append({
                        'name': current_class['name'],
                        'bases': current_class['bases'],
                        'methods': current_class_methods[:]
                    })
                    current_class = None
                    current_class_methods = []
                functions.append(func_def)
        
        i += 1
    
    # Save last class if exists
    if current_class:
        classes.append({
            'name': current_class['name'],
            'bases': current_class['bases'],
            'methods': current_class_methods[:]
        })
    
    # Generate .pyi content
    pyi_lines = []
    
    # Add imports
    needed_typing = set()
    
    # Check what types we need from all functions and classes
    all_functions = functions[:]
    for cls in classes:
        all_functions.extend(cls['methods'])
    
    for func in all_functions:
        for param in func['params']:
            if ': Optional[' in param or ': Union[' in param or ': List[' in param or ': Dict[' in param:
                if 'Optional' in param:
                    needed_typing.add('Optional')
                if 'Union' in param:
                    needed_typing.add('Union')
                if 'List' in param:
                    needed_typing.add('List')
                if 'Dict' in param:
                    needed_typing.add('Dict')
        if func['return_type'] in ['Optional', 'Union', 'List', 'Dict']:
            needed_typing.add(func['return_type'])
    
    # Always include Any
    needed_typing.add('Any')
    
    if needed_typing:
        typing_imports = ', '.join(sorted(needed_typing))
        pyi_lines.append(f"from typing import {typing_imports}")
        pyi_lines.append("")
    
    # Add functions
    for func in functions:
        params_str = ', '.join(func['params'])
        pyi_lines.append(f"def {func['name']}({params_str}) -> {func['return_type']}:")
        pyi_lines.append("    ...")
        pyi_lines.append("")
    
    # Add classes
    for cls in classes:
        bases_str = ""
        if cls['bases']:
            # Filter out known Cython-specific base classes
            python_bases = []
            for base in cls['bases']:
                if base not in ['object']:  # object is default
                    python_bases.append(base)
            if python_bases:
                bases_str = f"({', '.join(python_bases)})"
        
        pyi_lines.append(f"class {cls['name']}{bases_str}:")
        
        if not cls['methods']:
            pyi_lines.append("    ...")
        else:
            for method in cls['methods']:
                params_str = ', '.join(method['params'])
                pyi_lines.append(f"    def {method['name']}({params_str}) -> {method['return_type']}:")
                pyi_lines.append("        ...")
        pyi_lines.append("")
    
    # If no content was generated, add a basic stub
    if not functions and not classes:
        if not pyi_lines or pyi_lines == ["from typing import Any", ""]:
            pyi_lines = ["from typing import Any", ""]
    
    return '\n'.join(pyi_lines)

def process_pyx_file(pyx_path: str, output_dir: str = None) -> str:
    """Process a single .pyx file and generate corresponding .pyi file."""
    pyx_path = Path(pyx_path)
    
    if output_dir:
        pyi_path = Path(output_dir) / pyx_path.name.replace('.pyx', '.pyi')
    else:
        pyi_path = pyx_path.with_suffix('.pyi')
    
    # Read .pyx file
    try:
        with open(pyx_path, 'r', encoding='utf-8') as f:
            pyx_content = f.read()
    except UnicodeDecodeError:
        # Try with latin-1 encoding as fallback
        with open(pyx_path, 'r', encoding='latin-1') as f:
            pyx_content = f.read()
    
    # Generate .pyi content
    pyi_content = generate_pyi_content(str(pyx_path), pyx_content)
    
    # Write .pyi file
    pyi_path.parent.mkdir(parents=True, exist_ok=True)
    with open(pyi_path, 'w', encoding='utf-8') as f:
        f.write(pyi_content)
    
    return str(pyi_path)

def main():
    """Main function to process all .pyx files in the Sage library."""
    sage_root = Path('/home/runner/work/sage/sage')
    src_dir = sage_root / 'src'
    
    # Find all .pyx files
    pyx_files = list(src_dir.glob('**/*.pyx'))
    print(f"Found {len(pyx_files)} .pyx files")
    
    # Find existing .pyi files
    pyi_files = list(src_dir.glob('**/*.pyi'))
    existing_pyi = {f.with_suffix('.pyx') for f in pyi_files}
    
    # Filter out .pyx files that already have .pyi files
    new_pyx_files = [f for f in pyx_files if f not in existing_pyi]
    print(f"Found {len(new_pyx_files)} .pyx files without corresponding .pyi files")
    
    # Allow processing all files or just a subset
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--all':
        files_to_process = new_pyx_files
        print(f"Processing all {len(files_to_process)} files...")
    else:
        # Process first 10 files as a test
        files_to_process = new_pyx_files[:10]
        print(f"Processing first {len(files_to_process)} files as a test...")
    
    generated_count = 0
    error_count = 0
    
    for pyx_file in files_to_process:
        try:
            pyi_file = process_pyx_file(str(pyx_file))
            print(f"Generated: {pyi_file}")
            generated_count += 1
        except Exception as e:
            print(f"Error processing {pyx_file}: {e}")
            error_count += 1
    
    print(f"\nSummary:")
    print(f"  Generated: {generated_count} .pyi files")
    print(f"  Errors: {error_count} files")
    print(f"  Total processed: {generated_count + error_count} files")
    
    if len(sys.argv) <= 1 or sys.argv[1] != '--all':
        print(f"\nTo process all files, run: python3 {sys.argv[0]} --all")

if __name__ == '__main__':
    main()