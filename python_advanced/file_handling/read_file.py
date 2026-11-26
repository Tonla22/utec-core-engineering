#!/usr/bin/env python3
"""Module for reading and printing UTF-8 text files."""


def read_file(filename=""):
    """Read a text file and print its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
