### PythonLineCounter.run.py ###
# Author: T. Bauwens
# Date: 2020-2-4

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("pathname", help="selects boot mode")
parser.add_argument("-c", "--containing", help="specifies which substrings make files and folders should be ignored", nargs="+")
parser.add_argument("-m", "--matching", help="specifies which file and folder names should be ignored", nargs="+")

args = parser.parse_args()

import FolderCounter

print("======================================\nTOTAL LINES:",
    FolderCounter.countLines(args.pathname[:-1] if args.pathname.endswith("\\") else args.pathname,
                               None if not args.containing else args.containing,
                               None if not args.matching else args.matching, do_blank_counting=True),
      "\n======================================\n"
)
print("======================================\nNET LINES:",
    FolderCounter.countLines(args.pathname[:-1] if args.pathname.endswith("\\") else args.pathname,
                               None if not args.containing else args.containing,
                               None if not args.matching else args.matching, do_blank_counting=False),
      "\n======================================\n"
)