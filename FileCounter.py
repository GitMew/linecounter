### LineCounter.FileCounter.py ###
# Author: T. Bauwens
# Date: 2020-02-04

from pathlib import Path


def countLines(filepath, do_blank_counting=True):
    try:    
        with open(filepath, "r+") as handle:
            lines = handle.readlines()
    except:  # .readlines giving an error is most likely a UnicodeDecodeError. Of course, if filepath is unexistent, this try-except will err either way. 
        with open(filepath, "r+", encoding="utf-8") as handle:
            lines = handle.readlines()
        
    if not(do_blank_counting):
        lines = list(filter(lambda line: line != "\n", lines))
    return len(lines)


if __name__ == "__main__":
    this = Path(__file__)
    print(this)
    print(countLines(this))
