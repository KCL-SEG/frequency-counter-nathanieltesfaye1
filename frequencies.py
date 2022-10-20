"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        iToString = str(i)
        frequencies[iToString] = frequencies.get(iToString, 0) + 1
    return frequencies
