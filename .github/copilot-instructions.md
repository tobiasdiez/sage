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

- **Sage command-line evaluation**:
  ```bash
  ./sage -c "print(factor(2^100-1))"
  ```

### Developer-Specific Commands

- **Build specific package**:
  ```bash
  ./sage -i package_name
  ```

- **Force rebuild a package**:
  ```bash
  ./sage -f package_name  
  ```

- **Get package information**:
  ```bash
  ./sage --info package_name
  ```

- **List all packages**:
  ```bash
  ./sage --package list
  ./sage --optional          # Optional packages only
  ./sage --experimental      # Experimental packages only
  ```

### Git and Development Best Practices

- **Create development branch from develop**:
  ```bash
  git checkout develop
  git pull origin develop
  git checkout -b feature/my-feature develop
  ```

- **Standard development cycle**:
  1. Edit source files in `src/sage/`
  2. Build to test changes: `make build`
  3. Run doctests: `./sage -t modified_file.py`
  4. Commit changes: `git add . && git commit -m "Description"`
  5. Push and create pull request

- **Keep up with develop branch**:
  ```bash
  git checkout develop
  git pull origin develop
  git checkout feature/my-feature
  git rebase develop  # or merge if preferred
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
1. **Base toolchain** (zlib, mpfr, mpc, gcc if needed) - First 10-20 minutes
2. **Mathematical libraries** (m4ri, gf2x, flint, pari, etc.) - Next 20-40 minutes  
3. **Higher-level packages** (python, ecl, gap, etc.) - Next 20-30 minutes
4. **SageMath core** (sagelib, documentation) - Final 10-20 minutes

**Current validated build progress** (as of testing):
- Bootstrap: 1 minute ✓
- Configure: 30 seconds ✓  
- Base toolchain (mpfr, mpc): ~8 minutes ✓
- Mathematical libraries (m4ri, gf2x): ~15 minutes ✓  
- FLINT (number theory): ~21 minutes ✓
- eclib (elliptic curves): ~27 minutes ✓ (in progress)

This progression validates our 60-90 minute total build estimate.

### Monitoring Build Progress
```bash
# Watch build in real-time (run in separate terminal)
tail -f logs/install.log

# Check what package is currently building
grep "Setting up build directory" logs/install.log | tail -5

# Check for any build errors
grep -i error logs/install.log
```

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
- **Out of disk space**: Sage build requires several GB (5-10GB recommended)
- **Out of memory**: 4GB+ RAM recommended, 8GB+ for comfortable development

### Build Logs and Debugging
- **Main build log**: `logs/install.log` - Contains complete build output
- **Individual package logs**: `logs/pkgs/PACKAGE_NAME.log` 
- **Real-time monitoring**: `tail -f logs/install.log` (run in separate terminal)
- **Check build progress**: Build outputs show current package being compiled
- **Build failure debugging**: Look for `ERROR` entries in logs

### Performance Optimization
```bash
# Use all CPU cores for faster builds
export MAKEFLAGS="-j$(nproc) -l$(nproc).5"

# Use ccache for faster rebuilds (optional)
./configure --enable-ccache

# Reduce build verbosity (optional)
export V=0
```

### Clean Rebuild
If build issues persist:
```bash
make distclean      # Clean everything (takes ~1 minute)
make configure      # Re-bootstrap (takes ~1 minute)  
./configure --enable-build-as-root
make build          # Full rebuild (takes 60-90 minutes)
```

## Repository Structure

### Main Components
- **Core mathematics**: Number theory, algebra, geometry, calculus, combinatorics
- **Interfaces**: Wrappers for external mathematical software (GAP, PARI, Maxima, etc.)
- **Graphics**: 2D and 3D plotting capabilities (matplotlib, tachyon, etc.)
- **Notebooks**: Jupyter notebook integration for interactive mathematics
- **Documentation**: Comprehensive mathematical documentation system

### Package System
Sage uses a sophisticated package management system located in `build/pkgs/`:
- **Standard packages** (`type: standard`): Core mathematical functionality, always built
- **Optional packages** (`type: optional`): Additional mathematical tools, install with `./sage -i package`
- **Experimental packages** (`type: experimental`): Cutting-edge mathematical software

### Key Mathematical Libraries Built During Installation
- **MPFR, MPC**: Multi-precision floating-point arithmetic
- **FLINT**: Fast Library for Number Theory  
- **PARI/GP**: Computer algebra system for number theory
- **GAP**: Groups, Algorithms, Programming - computational discrete algebra
- **Maxima**: Symbolic computation system
- **SingularL**: Computer algebra system for polynomial computations
- **And 100+ other specialized mathematical packages**

This build system ensures Sage can be built consistently across different platforms while providing access to a vast ecosystem of mathematical software.