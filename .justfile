[default]
_list_available:
    @just --list --unsorted

# Setup venv if not active
[group('Setup')]
_setup_venv:
    #!/usr/bin/env bash
    if [[ ! -n "$VIRTUAL_ENV" ]]; then
        source venv.sh
    fi

# Install dependencies
[group('Setup')]
dependencies: _setup_venv
    pip install -r requirements.txt

# Run unit tests
[group('Build')]
test: _setup_venv
    python -m unittest discover -s tests -p "*_test.py" -v

# Run application
[group('Build')]
run: _setup_venv
    python counter/main.py
