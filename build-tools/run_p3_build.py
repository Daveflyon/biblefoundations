#!/usr/bin/env python3
"""Run the builder against all 16 Part 3 lesson content dicts.
Usage: run from the biblefoundations folder root:
    python3 build-tools/run_p3_build.py
"""
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.expanduser('~/mnt/biblefoundations/build-tools'))

from builder import build
from p3_lessons import LESSONS

built = []
for L in LESSONS:
    fname = build(L)
    built.append(fname)
    print(f"Built: {fname}")

print(f"\nTotal built: {len(built)}")
assert len(built) == 16, "Expected 16 files built"
print("All 16 Part 3 lesson files built successfully.")
