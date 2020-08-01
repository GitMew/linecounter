### LineCounter.FileCounter.py ###
# Author: T. Bauwens
# Date: 2020-2-4

from pathlib import Path

def countLines(filepath, do_blank_counting=True):
    with open(filepath) as handle:
        lines = handle.readlines()
    if not(do_blank_counting):
        lines = list(filter(lambda line: line != "\n", lines))
    return len(lines)

if __name__ == "__main__":
    this = Path(__file__)
    print(this)
    print(countLines(this))
