"""Compatibility entry point for the original app filename."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name("app-cities.py")), run_name="__main__")
