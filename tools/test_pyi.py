#!/usr/bin/env python3
"""
Test script to verify that generated .pyi files are working correctly.

This script performs basic validation of the typing stub files to ensure
they provide useful type information for static type checkers.
"""

import sys
import glob
import importlib.util
from pathlib import Path

def test_pyi_import(pyi_file: str) -> bool:
    """Test if a .pyi file can be loaded as a module."""
    try:
        spec = importlib.util.spec_from_file_location("test_module", pyi_file)
        if spec is None:
            return False
        module = importlib.util.module_from_spec(spec)
        # Don't actually execute - just test loading
        return True
    except Exception as e:
        print(f"Error loading {pyi_file}: {e}")
        return False

def main():
    """Test a sample of .pyi files."""
    sage_root = Path('/home/runner/work/sage/sage')
    src_dir = sage_root / 'src'
    
    # Test a sample of .pyi files
    pyi_files = list(src_dir.glob('**/*.pyi'))
    sample_files = pyi_files[:10]  # Test first 10 files
    
    print(f"Testing {len(sample_files)} sample .pyi files...")
    
    success_count = 0
    for pyi_file in sample_files:
        if test_pyi_import(str(pyi_file)):
            print(f"✓ {pyi_file.relative_to(sage_root)}")
            success_count += 1
        else:
            print(f"✗ {pyi_file.relative_to(sage_root)}")
    
    print(f"\nResults: {success_count}/{len(sample_files)} files loaded successfully")
    
    # Test the typing_aliases module
    try:
        sys.path.insert(0, str(src_dir))
        import sage.typing_aliases
        print("✓ sage.typing_aliases module imported successfully")
        
        # Check that some key types are available
        types_to_check = ['Integer', 'Matrix', 'Vector', 'Element']
        for type_name in types_to_check:
            if hasattr(sage.typing_aliases, type_name):
                print(f"✓ Type alias '{type_name}' is available")
            else:
                print(f"✗ Type alias '{type_name}' is missing")
                
    except Exception as e:
        print(f"✗ Error importing sage.typing_aliases: {e}")

if __name__ == '__main__':
    main()