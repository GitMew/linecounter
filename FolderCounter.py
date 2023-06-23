### LineCounter.FolderCounter.py ###
# Author: T. Bauwens
# Dates: 2020-02-04 / 2020-05-19
from collections import Counter
import os

import FileCounter as fc

IGNORE_MATCHING = [".idea", "__pycache__", ".git", ".gitignore"]
IGNORE_CONTAINING = [".wav", ".png", ".svg", ".jpg", ".jpeg", ".pdn", ".pdf", ".mp4", ".mp3", ".docx", ".zip", ".ipynb",
                     ".synctex.gz", ".bbl", ".log", ".bcf", ".aux", ".ind", ".idx", ".toc", ".out", ".pygtex",
                     ".pygstyle", ".xml", ".lof", ".lot", ".loa", ".blg", ".ilg", ".bib", ".nav", ".snm"]

INDENTOR = "    "
TOC_CHAR = "."
TRAILING_TOC_CHAR_AMOUNT = 4


def isIgnored(string, matching_list, containing_list):
    return (string in matching_list) \
           or any([contained_string in string for contained_string in containing_list])


def countLines(folderpath: fc.Path, ncontaining=None, nmatching=None, do_blank_counting=True):
    # Default values
    if ncontaining is None:
        ncontaining = []
    if nmatching is None:
        nmatching = []

    ncontaining += IGNORE_CONTAINING
    nmatching += IGNORE_MATCHING

    # Extension distribution
    extensions = Counter()

    # Build full tree of directory
    walked_path = list(os.walk(folderpath))

    # --- Determine maximum indentation of directory/file name ---
    # "Depth" == amount of folder jumps in path; nildepth == amount of folder jumps to expect by default
    nildepth = len(str(folderpath).split("\\"))

    max_indent = 0
    for tup in walked_path:
        pathname, folders, files = tup

        if not(any(
                [isIgnored(path_part, matching_list=nmatching, containing_list=ncontaining)
                for path_part in pathname.split("\\")]
        )):
            depth = len(pathname.split("\\"))
            for file in files:
                if not(isIgnored(file, matching_list=nmatching, containing_list=ncontaining)):
                    max_indent = max(                                                   # Increase maximally found length
                        max_indent,
                        len((depth - nildepth) * INDENTOR + pathname.split("\\")[-1]),  # Directory names
                        len((depth - nildepth + 1) * INDENTOR + file)                   # Filenames
                    )

    # --- Walk through tree, print it, and count up lines ---
    count = 0

    for tup in walked_path:
        pathname, folders, files = tup

        if not(any(
                [isIgnored(path_part, matching_list=nmatching, containing_list=ncontaining)
                for path_part in pathname.split("\\")]
        )):
            # Print folder name
            depth = len(pathname.split("\\"))
            print((depth-nildepth)*INDENTOR + pathname.split("\\")[-1])

            # Print file names with counts
            for file in files:
                if not(isIgnored(file, matching_list=nmatching, containing_list=ncontaining)):
                    local_count = fc.countLines(pathname + "\\" + file, do_blank_counting=do_blank_counting)
                    display_string = (depth - nildepth + 1) * INDENTOR + file
                    print(display_string, TOC_CHAR*(max_indent-len(display_string) + TRAILING_TOC_CHAR_AMOUNT), local_count)
                    count += local_count
                    extensions[file.split(".")[-1]] += local_count

    print("\nDISTRIBUTION:")
    for ext, ext_count in sorted(extensions.items(), key=lambda t: t[1], reverse=True):
        print(ext, ext_count, f"{round(100*ext_count/count,2)}%", sep="\t")
    return count


if __name__ == "__main__":
    this_parent = fc.Path(__file__).parents[0]
    print("Total:", countLines(this_parent))
