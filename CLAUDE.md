# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`django_layui29` is a Django app that integrates the Layui front-end framework (v2.9.25), providing simplified UI components for Django projects. The package includes htmx 1.9.4 and js.cookie.js 3.0.5.

**WARNING:** This project is currently unstable and not recommended for production use.

## Development Commands

### Environment Setup
```bash
# Install dependencies using Poetry
poetry install

# Install with django-tables2 support
poetry install --with tables

# Install pre-commit hooks
pre-commit install
```

### Testing
```bash
# Run all tests (uses pytest-xdist with 3 workers by default)
poetry run pytest

# Run specific test file
poetry run pytest tests/test_layui_loading.py

# Run tests without parallelization
poetry run pytest -n0

# Run tests with Django database
poetry run pytest -m django_db
```

Django test settings are configured in `pyproject.toml` with `DJANGO_SETTINGS_MODULE = "conf.settings"`.

### Development Server
```bash
# Run the testapp development server
cd src
python manage.py runserver

# Run migrations
python manage.py migrate

# Create migrations
python manage.py makemigrations
```

### Code Quality
```bash
# Run all pre-commit hooks manually
pre-commit run --all-files

# Format imports with isort (black profile)
isort --profile black --multi-line=3 --line-width=120 src/

# Format code with black
black --line-length=120 --target-version=py38 src/

# Lint with flake8
flake8 --max-line-length=120 --exclude=__init__.py --ignore=E203,E501,W503,W291,E402 src/
```

### Building and Publishing
```bash
# Build the package
poetry build

# Publish to PyPI
poetry publish

# Or use twine
twine upload dist/*

# Bump version (uses bumpversion)
bumpversion patch  # 0.4.5 -> 0.4.6
bumpversion minor  # 0.4.5 -> 0.5.0
bumpversion major  # 0.4.5 -> 1.0.0
```

Version management automatically updates:
- `pyproject.toml` (version field)
- `src/django_layui29/__init__.py` (__version__ variable)

### Documentation
```bash
# Build documentation with mkdocs
mkdocs build

# Serve documentation locally
mkdocs serve
```

## Project Architecture

### Directory Structure
```
src/
├── conf/              # Django project configuration
│   ├── settings.py    # Main settings file
│   ├── urls.py        # URL routing
│   └── wsgi.py/asgi.py
├── django_layui29/    # Main Django app (the package)
│   ├── static/        # Static assets (Layui files)
│   │   └── layui29/   # Layui CSS/JS/fonts
│   ├── templates/     # Base templates
│   │   └── layui29/
│   │       ├── base.html          # Root base template
│   │       ├── layout/            # Three layout options
│   │       │   ├── center.html    # Centered layout
│   │       │   ├── admin.html     # Admin dashboard layout
│   │       │   └── normal.html    # Standard layout
│   │       └── component/         # Reusable components
│   │           ├── base/          # Header, navigation
│   │           └── tables.html    # Table component
│   ├── utils.py       # Utilities (context processor)
│   └── views.py       # (Currently empty)
└── testapp/           # Example/test Django app
    ├── views.py       # Example views using layouts
    ├── tables.py      # django-tables2 examples
    └── templates/     # Example templates
```

### Key Components

#### Asset Loading System
The app supports two modes for loading Layui assets, controlled by `LAYUI_FROM_LOCAL` setting:

- **Local mode** (`LAYUI_FROM_LOCAL = True`): Loads from `/static/layui29/`
- **CDN mode** (`LAYUI_FROM_LOCAL = False`): Loads from unpkg CDN

The context processor `django_layui29.utils.get_layui_from_local` makes this setting available in all templates. Templates use conditional logic to switch between local and CDN paths.

#### Template Hierarchy
1. **Base template**: `layui29/base.html` - Root template with asset loading logic
2. **Layout templates**: Three pre-built layouts extend base.html
   - `center.html`: Centered content layout
   - `admin.html`: Admin dashboard with left sidebar navigation
   - `normal.html`: Standard page layout
3. **Components**: Reusable template fragments in `component/`
   - `base/header.html`: Site header
   - `base/left_nav.html`: Admin sidebar navigation
   - `tables.html`: django-tables2 integration template

#### Template Customization
Users can override templates by:
1. Placing their app **before** `django_layui29` in `INSTALLED_APPS`
2. Creating templates with matching paths (e.g., `your_app/templates/layui29/component/base/header.html`)

Django's template loader will find the custom template first.

#### django-tables2 Integration
The app provides a custom table template (`layui29/component/tables.html`) that renders django-tables2 tables with Layui styling. Usage pattern:

```python
# tables.py
import django_tables2 as tables

class YourTable(tables.Table):
    class Meta:
        model = YourModel
        template_name = "layui29/component/tables.html"
```

### Configuration Requirements

When integrating this app, users must:

1. Add to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # ...
    'django_layui29',
]
```

2. Add context processor to `TEMPLATES`:
```python
TEMPLATES = [{
    'OPTIONS': {
        'context_processors': [
            # ...
            'django_layui29.utils.get_layui_from_local',
        ],
    },
}]
```

3. (Optional) Configure asset loading:
```python
LAYUI_FROM_LOCAL = True  # or False for CDN
```

## Testing Approach

Tests use pytest-django with parallel execution (pytest-xdist). Key test patterns:

- Mark tests requiring database: `@pytest.mark.django_db`
- Use `override_settings` for testing different configurations
- Test both local and CDN asset loading modes
- Verify rendered HTML contains expected asset URLs

## Code Style

This project uses Chinese comments in some files and follows these formatting rules:

- **Line length**: 120 characters
- **Imports**: isort with black profile
- **Formatting**: black with Python 3.8 target
- **Linting**: flake8 with ignores: E203, E501, W503, W291, E402
- **Commit messages**: Must match pattern `(add|mod|del|fix):.*` (enforced by gitlint)

Pre-commit hooks automatically enforce these standards.

## Python Version Support

- **Minimum**: Python 3.9
- **Maximum**: Python 3.x (not Python 4.0)
- **Django**: <6.0
