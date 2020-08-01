### LineCounter.run.py ###
# Author: T. Bauwens
# Date: 2020-2-4

import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("pathname", help="specifies the full file or folder path to analyse")
parser.add_argument("-c", "--containing", help="specifies which substrings make files and folders should be ignored", nargs="+")
parser.add_argument("-m", "--matching", help="specifies which file and folder names should be ignored", nargs="+")

args = parser.parse_args()

import FolderCounter
import FileCounter
SEPARATOR = "======================================"

input_name = args.pathname[:-1] if args.pathname.endswith("\\") or args.pathname.endswith("/") else args.pathname
containing_args = None if not args.containing else args.containing
matching_args = None if not args.matching else args.matching

if Path(input_name).is_dir():
    print(SEPARATOR + "\nTOTAL LINES:",
          FolderCounter.countLines(input_name, containing_args, matching_args, do_blank_counting=True),
          "\n" + SEPARATOR + "\n")
    print(SEPARATOR + "\nTOTAL LINES W/O BLANKS:",
          FolderCounter.countLines(input_name, containing_args, matching_args, do_blank_counting=False),
          "\n" + SEPARATOR + "\n")
elif Path(input_name).is_file():
    print(input_name)
    print(SEPARATOR + "\nTOTAL LINES:",
          FileCounter.countLines(input_name, do_blank_counting=True),
          "\n" + SEPARATOR + "\n")
    print(input_name)
    print(SEPARATOR + "\nTOTAL LINES W/O BLANKS:",
          FileCounter.countLines(input_name, do_blank_counting=False),
          "\n" + SEPARATOR + "\n")
else:
    print("Invalid path. Please pass the full path to an existing file or folder.")