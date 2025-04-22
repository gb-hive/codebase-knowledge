#!/usr/bin/env python3

import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure credentials are set
if not os.getenv("GEMINI_API_KEY") and not os.getenv("CLAUDE_API_KEY"):
    raise RuntimeError("Set GEMINI_API_KEY or CLAUDE_API_KEY in .env")

# Set up paths
TOOL_DIR = os.path.abspath("tools/tutorial")
WORKSPACE_DIR = os.getcwd()

def main():
    # Create output directory if it doesn't exist
    output_dir = Path(WORKSPACE_DIR) / "docs" / "tutorial"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Run the tutorial generation script
    subprocess.run([
        "python",
        os.path.join(TOOL_DIR, "main.py"),
        "--dir", WORKSPACE_DIR,
        "--include", ".py",  # Include Python files
        "--exclude", "tests/",  # Exclude test files
        "--output", str(output_dir),
        "--language", "English"
    ], check=True)

if __name__ == "__main__":
    main() 