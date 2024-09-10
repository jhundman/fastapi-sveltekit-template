#!/bin/bash

# Determine the backend directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$(dirname "$SCRIPT_DIR")"

# Change to the backend directory
cd "$BACKEND_DIR" || exit 1

echo "Running checks in: $BACKEND_DIR"

# Run ruff format
echo "Running ruff format..."
ruff format .

# Run ruff check
echo "Running ruff check..."
ruff check .
