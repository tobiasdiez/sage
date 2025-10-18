# SageMath - Open Source Mathematics Software

SageMath is a free open-source mathematics software system licensed under the GPL v2+. It is an open source alternative to Magma, Maple, Mathematica, and MATLAB. The system uses Python as its primary language and integrates many open-source mathematical packages.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Fresh Installation and Build Process

Build SageMath using the modern Meson build system with conda dependencies:

1. **Install Miniforge** (recommended conda distribution):
   ```bash
   # Download and install Miniforge for your platform
   # Linux/macOS: https://github.com/conda-forge/miniforge#install
   # Or use system package manager: sudo apt install miniforge3 (Ubuntu 22.04+)
   ```

2. **Create conda environment** with all dependencies:
   ```bash
   # Linux
   mamba env create --file environment-3.12-linux.yml --name sage-dev
   
   # macOS
   mamba env create --file environment-3.12-macos.yml --name sage-dev
   
   # Windows (experimental)
   mamba env create --file environment-3.12-win.yml --name sage-dev
   ```
   - **NEVER CANCEL**: Takes 5-15 minutes to download and install conda packages. Set timeout to 30+ minutes.
   - Use different Python versions by replacing `3.12` with `3.11` or `3.13` in filename

3. **Activate conda environment**:
   ```bash
   mamba activate sage-dev
   ```

4. **Build and install Sage** (editable mode):
   ```bash
   pip install --no-build-isolation --editable .
   ```
   - **NEVER CANCEL**: Takes 5-15 minutes for compilation. Set timeout to 30+ minutes.
   - Much faster than old build system since dependencies come pre-built from conda
   - `--no-build-isolation` allows reusing conda dependencies
   - `--editable` enables hot-reloading of changes without rebuild

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

- **Modern pytest-based testing**:
  ```bash
  pytest --doctest --doctest-ignore-import-errors -x src/sage/categories
  ```
  - **NEVER CANCEL**: Takes 5-30 minutes depending on scope. Set timeout to 60+ minutes.

- **Full test suite** (all tests):
  ```bash
  ./sage -t --all -p4 --format github
  ```
  - **NEVER CANCEL**: Takes 30 minutes to several hours (over 200,000 lines of tests). Set timeout to 300+ minutes.

- **Test only new/changed files** (faster for development):
  ```bash
  ./sage -t --new --long -p4 --format github
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

- **Rebuild after changes**:
  ```bash
  # For Cython files - automatic rebuild in editable mode
  # Just restart Sage, no manual rebuild needed
  
  # For substantial changes, reinstall
  pip install --no-build-isolation --editable .
  ```

- **Work with conda environment**:
  ```bash
  mamba activate sage-dev                    # Activate development environment
  mamba list                                 # List installed packages
  mamba env update --file environment-3.12-linux.yml  # Update environment
  ```

- **Direct meson commands** (advanced):
  ```bash
  meson setup builddir                       # Configure build directory
  meson compile -C builddir                  # Compile changes
  meson install -C builddir                  # Install to environment
  ```

- **Update conda lock files** (maintainers):
  ```bash
  python tools/update-conda.py              # Update environment files
  ```

### Git and Development Best Practices

- **Create development branch from develop**:
  ```bash
  git checkout develop
  git pull origin develop
  git checkout -b feature/my-feature develop
  ```

- **Standard development cycle**:
  1. Activate conda environment: `mamba activate sage-dev`
  2. Edit source files in `src/sage/`
  3. Changes auto-rebuild in editable mode (for Cython files)
  4. Test changes: `./sage -t modified_file.py`
  5. Commit changes: `git add . && git commit -m "Description"`
  6. Push and create pull request

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
   pip install --no-build-isolation --editable . && ./sage -c "print('Build successful')"
   ```

5. **Doctest validation** (critical for any code changes):
   ```bash
   ./sage -t src/sage/rings/integer.py  # Test a core file
   ./sage -t changed_file.py  # Test your modified file
   ```

### Pre-Commit Validation
Always run these before committing changes:

- **Code quality checks**: Use integrated linters with meson build system
- **Documentation build**: If you modify docs, install sage-docbuild and run:
  ```bash
  pip install --no-build-isolation -v --editable ./pkgs/sage-docbuild
  sage --docbuild all html
  ```

## Common Tasks

### Package Management
- **Conda environment management**: All dependencies managed via conda environment files
- **Update environment**: `mamba env update --file environment-3.12-linux.yml --name sage-dev`
- **List packages**: `mamba list` (in activated environment)

### Building Documentation
- **HTML documentation**: 
  ```bash
  pip install --no-build-isolation -v --editable ./pkgs/sage-docbuild
  sage --docbuild all html
  ```
  - **NEVER CANCEL**: Takes 10-30 minutes. Set timeout to 60+ minutes.

- **PDF documentation**:
  ```bash
  # First install docbuild package, then:
  sage --docbuild all pdf
  ```
  - Requires LaTeX to be installed
  - **NEVER CANCEL**: Takes 15-45 minutes. Set timeout to 90+ minutes.

### Git Workflow
- **Create development branch**: `git checkout -b my_branch develop`
- **Standard development cycle**: Edit code → Test → Commit → Push → Create PR

## Important File Locations

### Core Directories
- **Source code**: `src/` - Main Sage source code
- **Build system**: `meson.build` files throughout source tree - Meson build configuration
- **Documentation**: `src/doc/` - Documentation source files
- **Conda environments**: `environment-*.yml` - Conda dependency specifications
- **Build directory**: `builddir/` or `build/cp*/` - Meson build artifacts (created after build)

### Configuration Files
- **Meson build**: `meson.build` - Modern build system configuration throughout source tree
- **Conda environments**: `environment-3.X-{linux,macos,win}.yml` - Platform-specific dependencies
- **Python packaging**: `pyproject.toml` - Python packaging configuration with meson-python backend
- **Development tools**: `tox.ini`, `pyrightconfig.json` - Testing and type checking configuration

### Key Scripts
- **Main Sage launcher**: `./sage` - Primary entry point (works after pip install)
- **Conda environment tools**: `tools/update-conda.py` - Update conda lock files
- **Meson utilities**: `tools/update-meson.py` - Update meson.build files

## Build System Details

### Build Targets (using meson + conda)
- `mamba env create --file environment-3.12-linux.yml --name sage-dev` - Create conda environment
- `mamba activate sage-dev` - Activate development environment
- `pip install --no-build-isolation --editable .` - Build and install Sage in editable mode
- `./sage -t --all` - Run test suite
- `sage --docbuild all html` - Build documentation
- `mamba env remove --name sage-dev` - Clean remove environment (complete cleanup)

### Time Expectations and Timeouts
- **Conda environment creation**: 5-15 minutes (timeout: 30+ minutes)
- **Sage build and install (`pip install --editable`)**: 5-15 minutes (timeout: 30+ minutes)  
- **Incremental rebuild**: 1-5 minutes (timeout: 15+ minutes)
- **Quick test (`./sage -t file.py`)**: 5-30 seconds per file (timeout: 5+ minutes)
- **Full test suite (`./sage -t --all`)**: 30 minutes to several hours (timeout: 300+ minutes)
- **Documentation build (`sage --docbuild all html`)**: 10-30 minutes (timeout: 60+ minutes)

**CRITICAL**: NEVER CANCEL any build or test command. Even with conda dependencies, compilation may take 15+ minutes and tests may take several hours. Use appropriate timeouts and wait for completion.

### Build Progress Indicators
During build with conda+meson, you'll see this typical progression:
1. **Conda environment setup** - Package downloading and dependency resolution (5-15 minutes)
2. **Meson configuration** - Build system setup and dependency detection (30 seconds - 2 minutes)
3. **Cython compilation** - Core mathematical modules compilation (5-10 minutes)  
4. **Python package installation** - Final installation steps (1-3 minutes)

**Current validated build progress** (conda + meson):
- Environment creation: 5-15 minutes ✓
- Meson setup: 30 seconds ✓  
- Pip install (editable): 5-15 minutes ✓
- All mathematical libraries come pre-built from conda ✓
- Much faster than traditional source builds ✓

**All validation commands tested and working correctly ✓**

This approach leverages pre-built conda packages for mathematical libraries, dramatically reducing build time compared to building everything from source.

### Monitoring Build Progress
```bash
# Watch meson build in real-time
ninja -C builddir -v

# Check conda environment packages
mamba list

# Check build directory contents
ls -la builddir/

# Check for meson build errors
cat builddir/meson-logs/meson-log.txt
```

## Environment Setup

### Required Environment Setup
```bash
# Activate conda environment (must be done each session)
mamba activate sage-dev

# Set environment variable for verbose editable builds (optional)
export MESONPY_EDITABLE_VERBOSE=1  # Shows Cython recompilation messages

# For Windows additional setup
export LIB="$LIB;$CONDA_PREFIX\\Library\\lib"
export INCLUDE="$INCLUDE;$CONDA_PREFIX\\Library\\include"
```

### Platform-Specific Setup

#### Linux
- Use `environment-3.12-linux.yml` or `environment-3.12-linux-aarch64.yml` for ARM

#### macOS  
- Use `environment-3.12-macos.yml` or `environment-3.12-macos-x86_64.yml` for Intel Macs

#### Windows (Experimental)
- Install Visual Studio Build Tools first
- Use `environment-3.12-win.yml`
- Use "VS x64 Native Tools Command Prompt"

### Development Environment
- **Python version**: Python 3.11+ (specified in environment file)
- **Conda/Mamba**: Required for dependency management
- **Git**: Required for development workflow
- **Disk space**: 2-5GB for conda environment + source (much less than old build system)
- **RAM**: 4GB+ recommended, 8GB+ for comfortable development

## Troubleshooting

### Common Issues
- **Missing conda/mamba**: Install Miniforge or Mambaforge
- **Environment creation fails**: Retry with `mamba env create` (network issues are common)
- **Build fails**: Check `builddir/meson-logs/meson-log.txt` for detailed error messages
- **Import errors**: Make sure conda environment is activated with `mamba activate sage-dev`
- **Test failures**: 2-3 test failures are typically acceptable in complex mathematical software
- **Out of disk space**: Conda environments require 2-5GB (much less than old build system)
- **Editable install issues**: Run `pip install --no-build-isolation --editable .` again

### Build Logs and Debugging
- **Meson build log**: `builddir/meson-logs/meson-log.txt` - Contains complete build output
- **Conda environment**: `mamba list` - See all installed packages and versions
- **Real-time monitoring**: `ninja -C builddir -v` - Watch compilation progress
- **Check environment**: `mamba info` - Conda environment details
- **Build failure debugging**: Check meson logs and ensure conda environment is activated

### Performance Optimization
```bash
# Use parallel compilation (automatic with meson)
pip install --no-build-isolation --editable . -v

# Enable verbose editable builds
export MESONPY_EDITABLE_VERBOSE=1

# Use ccache for faster recompilation
export CC="ccache gcc"
export CXX="ccache g++"
```

### Clean Rebuild
If build issues persist:
```bash
# Remove build directory
rm -rf builddir/

# Recreate conda environment  
mamba env remove --name sage-dev
mamba env create --file environment-3.12-linux.yml --name sage-dev
mamba activate sage-dev

# Clean reinstall
pip install --no-build-isolation --editable .
```

## Repository Structure

### Main Components
- **Core mathematics**: Number theory, algebra, geometry, calculus, combinatorics
- **Interfaces**: Wrappers for external mathematical software (GAP, PARI, Maxima, etc.)
- **Graphics**: 2D and 3D plotting capabilities (matplotlib, tachyon, etc.)
- **Notebooks**: Jupyter notebook integration for interactive mathematics
- **Documentation**: Comprehensive mathematical documentation system

### Package System
Sage now uses conda for dependency management instead of building packages from source:
- **Conda packages**: All mathematical libraries come pre-built from conda-forge
- **Environment files**: `environment-*.yml` specify exact versions and dependencies  
- **Lock files**: Generated by conda-lock for reproducible environments across platforms
- **Meson build**: Only compiles Sage's own Cython/Python code, not dependencies

### Key Mathematical Libraries (Pre-built from Conda)
- **MPFR, MPC**: Multi-precision floating-point arithmetic
- **FLINT**: Fast Library for Number Theory  
- **PARI/GP**: Computer algebra system for number theory
- **GAP**: Groups, Algorithms, Programming - computational discrete algebra
- **Maxima**: Symbolic computation system
- **SingularL**: Computer algebra system for polynomial computations
- **And 100+ other specialized mathematical packages**

This conda-based approach provides consistent, fast builds across platforms while maintaining access to the full ecosystem of mathematical software.