#!/bin/bash
# Helper script to run Python scripts with the virtual environment

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PYTHON="$SCRIPT_DIR/venv/bin/python"

if [ $# -eq 0 ]; then
    echo "Usage: ./run.sh <script.py>"
    echo "Available scripts:"
    echo "  - tutorial.py          (Vollständiges Tutorial)"
    echo "  - docker_start.py      (Einfacher Test)"
    echo "  - container_loeschen.py (Alle Container löschen)"
    echo "  - images_loeschen.py   (Alle Images löschen)"
    exit 1
fi

"$VENV_PYTHON" "$@"
