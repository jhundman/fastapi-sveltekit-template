#!/bin/bash

# Function to display usage information
usage() {
    echo "Usage: $0 [-f | --fix]"
    echo "  -f, --fix    Enable auto-fixing for ruff check"
    exit 1
}

# Initialize variables
FIX_MODE=false

# Parse command line options
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--fix)
            FIX_MODE=true
            shift
            ;;
        *)
            echo "Invalid option: $1" >&2
            usage
            ;;
    esac
done

# Determine the backend directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$(dirname "$SCRIPT_DIR")"

# Change to the backend directory
cd "$BACKEND_DIR" || exit 1

echo "Running checks in: $BACKEND_DIR"

# Run ruff format
echo "Running ruff format..."
ruff format .

# Run ruff check with optional --fix
if $FIX_MODE; then
    echo "Running ruff check with auto-fix..."
    ruff check --fix .
else
    echo "Running ruff check..."
    ruff check .
fi
