#!/usr/bin/env python

import os
import sys

# Check if PyInstaller is installed
try:
    import PyInstaller
except ImportError:
    print("Error: PyInstaller is not installed")
    sys.exit(1)

# Get the names of the Python files to compile
if len(sys.argv) < 2:
    print("Usage: python compile_exe.py <file1> [file2] [file3] ... [fileN]")
    sys.exit(1)

filenames = sys.argv[1:]

# Check if the files exist
for filename in filenames:
    if not os.path.exists(filename):
        print("Error: file not found")
        sys.exit(1)

# Compile the Python files into an executable
try:
    PyInstaller.main(["--onefile"] + filenames)
except:
    print("Error: unable to compile files")
    sys.exit(1)

print("Success: executable created successfully")