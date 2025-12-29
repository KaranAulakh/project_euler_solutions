#!/usr/bin/env python3
"""Entry point to run Project Euler problems."""

import sys
import importlib.util
from pathlib import Path


def run_problem(problem_number: int) -> None:
    """Run a specific Project Euler problem by number."""
    problem_file = Path(__file__).parent / "Promblems" / f"{problem_number}.py"
    
    if not problem_file.exists():
        print(f"Problem {problem_number} not found")
        return
    
    spec = importlib.util.spec_from_file_location(f"problem{problem_number}", problem_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py <problem_number>")
        sys.exit(1)
    
    try:
        run_problem(int(sys.argv[1]))
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a valid number")
        sys.exit(1)


if __name__ == "__main__":
    main()
