# SageMath - Open Source Mathematics Software

SageMath is a free open-source mathematics software system licensed under the GPL v2+. It is an open source alternative to Magma, Maple, Mathematica, and MATLAB. The system uses Python as its primary language and integrates many open-source mathematical packages.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Fresh Installation and Build Process

Bootstrap, configure, and build the repository from scratch:

1. **Install system prerequisites** (Ubuntu/Debian):
   ```bash
   sudo apt update
   sudo apt install -y binutils make m4 perl flex python3 tar bc gcc libbz2-dev bzip2 g++ ca-certificates patch pkg-config
   ```

2. **Bootstrap the build system**:
   ```bash
   make configure
   ```
   - **NEVER CANCEL**: Takes approximately 1 minute. Set timeout to 5+ minutes.

3. **Configure the build** (recommended with parallel build optimization):
   ```bash
   export MAKEFLAGS="-j$(nproc) -l$(nproc).5"
   ./configure --enable-build-as-root
   ```
   - **NEVER CANCEL**: Takes approximately 30 seconds. Set timeout to 5+ minutes.
   - Use `--config-cache` for faster subsequent configure runs during development
   - Use `--enable-ccache` to enable disk cache for object files (speeds up branch switching)

4. **Build Sage**:
   ```bash
   make build
   ```
   - **NEVER CANCEL**: Takes 60-90 minutes on modern hardware. Set timeout to 120+ minutes.
   - For full build with documentation: `make` (takes longer)
   - For minimal build without docs: `make build`

5. **Test the installation**:
   ```bash
   ./sage -c "print('Sage works!')"
   ```

### Running Tests

- **Quick doctest on a single file**:
  ```bash
  ./sage -t path/to/file.py
  ```
  - **NEVER CANCEL**: Individual files typically take 5-30 seconds. Set timeout to 5+ minutes.
  - Example: `./sage -t src/sage/rings/integer.py`

- **Test multiple files**:
  ```bash
  ./sage -t src/sage/rings/  # Test entire directory
  ./sage -t --optional src/sage/rings/finite_rings/  # Include optional tests  
  ```

- **Quick test suite**:
  ```bash
  make test
  ```
  - **NEVER CANCEL**: Takes 15-30 minutes. Set timeout to 60+ minutes.

- **Long test suite** (comprehensive):
  ```bash
  make ptestlong
  ```
  - **NEVER CANCEL**: Takes 10 minutes to several hours (over 200,000 lines of tests). Set timeout to 300+ minutes.

- **Parallel testing** (faster):
  ```bash
  ./sage -t --optional --all --parallel 4  # Use 4 cores
  ```

### Development Workflow

- **Start Sage interactive session**:
  ```bash
  ./sage
  ```

- **Run Sage in notebook mode**:
  ```bash
  ./sage --notebook=jupyter
  ```

- **Run Python script with Sage**:
  ```bash
  ./sage script.py
  ```

## Validation

### Always Manually Validate Changes
After making any code changes, you MUST run through complete validation scenarios:

1. **Basic functionality test**:
   ```bash
   ./sage -c "print('Basic arithmetic:', 2+2); print('Plotting available:', 'plot' in dir())"
   ```

2. **Mathematical computation test**:
   ```bash
   ./sage -c "print('Prime factorization:', factor(12345)); print('Symbolic math:', expand((x+1)^3))"
   ```

3. **Advanced mathematical test**:
   ```bash
   ./sage -c "
   from sage.all import *
   print('Matrix computation:', matrix([[1,2],[3,4]]).det())
   print('Number theory:', next_prime(1000))
   print('Calculus:', integrate(x^2, x))
   "
   ```

4. **Build validation** (after source changes):
   ```bash
   make build && ./sage -c "print('Build successful')"
   ```

5. **Doctest validation** (critical for any code changes):
   ```bash
   ./sage -t src/sage/rings/integer.py  # Test a core file
   ./sage -t changed_file.py  # Test your modified file
   ```

### Pre-Commit Validation
Always run these before committing changes:

- **Code quality checks**: Currently, Sage uses various linters integrated into the build process
- **Documentation build**: If you modify docs, run `make doc-html` to verify documentation builds correctly

## Common Tasks

### Package Management
- **List optional packages**: `./sage --optional`
- **Install optional package**: `./sage -i package_name`
- **Get package info**: `./sage --info package_name`

### Building Documentation
- **HTML documentation**: 
  ```bash
  make doc-html
  ```
  - **NEVER CANCEL**: Takes 30-60 minutes. Set timeout to 90+ minutes.

- **PDF documentation**:
  ```bash
  make doc-pdf
  ```
  - Requires LaTeX to be installed
  - **NEVER CANCEL**: Takes 45-90 minutes. Set timeout to 120+ minutes.

### Git Workflow
- **Create development branch**: `git checkout -b my_branch develop`
- **Standard development cycle**: Edit code → Test → Commit → Push → Create PR

## Important File Locations

### Core Directories
- **Source code**: `src/` - Main Sage source code
- **Build system**: `build/` - Build configuration and package definitions
- **Documentation**: `src/doc/` - Documentation source files
- **Built Sage**: `local/` - Installation directory (created after build)

### Configuration Files
- **Main Makefile**: `Makefile` - Top-level build targets
- **Build configuration**: `build/make/Makefile` - Detailed build rules
- **Package definitions**: `build/pkgs/*/` - Individual package configurations
- **Project config**: `pyproject.toml` - Python packaging configuration

### Key Scripts
- **Main Sage launcher**: `./sage` - Primary entry point
- **Build tools**: `build/bin/` - Build helper scripts
- **Source tools**: `src/bin/` - Source tree utilities

## Build System Details

### Build Targets (from root directory)
- `make configure` - Bootstrap and create configure script
- `make build` - Build Sage (minimal, no docs)
- `make` or `make all` - Build Sage with documentation
- `make test` - Run test suite
- `make ptestlong` - Run comprehensive tests
- `make doc-clean` - Clean documentation
- `make distclean` - Clean everything (forces complete rebuild)

### Time Expectations and Timeouts
- **Bootstrap (`make configure`)**: 1 minute (timeout: 5+ minutes)
- **Configure (`./configure`)**: 30 seconds (timeout: 5+ minutes)  
- **Full build from scratch (`make build`)**: 60-90 minutes on modern hardware (timeout: 120+ minutes)
- **Incremental build**: 5-15 minutes (timeout: 30+ minutes)
- **Quick test (`./sage -t file.py`)**: 5-30 seconds per file (timeout: 5+ minutes)
- **Test suite (`make test`)**: 15-30 minutes (timeout: 60+ minutes)
- **Long tests (`make ptestlong`)**: 10 minutes to several hours (timeout: 300+ minutes)
- **Documentation build (`make doc-html`)**: 30-60 minutes (timeout: 90+ minutes)

**CRITICAL**: NEVER CANCEL any build or test command. Builds may take over an hour and tests may take several hours. Use appropriate timeouts and wait for completion.

### Build Progress Indicators
During build, you'll see packages being compiled in this typical order:
1. **Base toolchain** (zlib, mpfr, mpc, gcc if needed) - 10-20 minutes
2. **Mathematical libraries** (m4ri, flint, pari, etc.) - 20-40 minutes  
3. **Higher-level packages** (python, ecl, gap, etc.) - 20-30 minutes
4. **SageMath core** (sagelib, documentation) - 10-20 minutes

## Environment Setup

### Required Environment Variables
```bash
export MAKEFLAGS="-j$(nproc) -l$(nproc).5"  # Parallel build
export V=0  # Reduce verbosity (optional)
```

### macOS Specific (if using Homebrew)
```bash
source ./.homebrew-build-env
```

### Development Environment
- **Python version**: Python 3.4+ required for build system
- **Git**: Required for development workflow
- **Disk space**: Several GB required for full build
- **RAM**: 4GB+ recommended, 8GB+ for comfortable development

## Troubleshooting

### Common Issues
- **Missing system packages**: Run the apt install command above
- **Build fails**: Check `logs/install.log` for detailed error messages
- **Long build times**: This is normal - Sage builds many mathematical libraries from source
- **Test failures**: 2-3 test failures are typically acceptable in complex mathematical software

### Clean Rebuild
If build issues persist:
```bash
make distclean
make configure
./configure --enable-build-as-root
make build
```

## Repository Structure

### Main Components
- **Core mathematics**: Number theory, algebra, geometry, calculus
- **Interfaces**: Wrappers for external mathematical software
- **Graphics**: 2D and 3D plotting capabilities
- **Notebooks**: Jupyter notebook integration
- **Documentation**: Comprehensive mathematical documentation

### Package System
Sage uses a sophisticated package management system with:
- **Standard packages**: Core mathematical functionality
- **Optional packages**: Additional mathematical tools
- **Experimental packages**: Cutting-edge mathematical software

This build system ensures Sage can be built consistently across different platforms while providing access to a vast ecosystem of mathematical software.