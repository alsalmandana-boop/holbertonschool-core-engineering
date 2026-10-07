#!/usr/bin/env python3
"""Module for writing to a text file."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
