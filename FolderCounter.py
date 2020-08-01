### LineCounter.FolderCounter.py ###
# Author: T. Bauwens
# Dates: 2020-02-04 / 2020-05-19

import FileCounter as fc
import os

IGNORE_MATCHING = [".idea", "__pycache__", ".git"]
IGNORE_CONTAINING = [".wav", ".png", ".svg", ".jpg", ".jpeg", ".pdn", ".pdf", ".mp4", ".mp3", ".docx", ".zip"]

INDENTOR = "    "
TOC_CHAR = "."

def isIgnored(string, matching_list, containing_list):
    return (string in matching_list) \
           or any([contained_string in string for contained_string in containing_list])


def countLines(folderpath : fc.Path, ncontaining=None, nmatching=None, do_blank_counting=True):
    # Default values
    if ncontaining is None:
        ncontaining = []
    if nmatching is None:
        nmatching = []

    ncontaining += IGNORE_CONTAINING
    nmatching += IGNORE_MATCHING

    # Build tree of directory
    walked_path = list(os.walk(folderpath))

    # Determine maximum indentation of directory/file name
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
                    max_indent = max(max_indent, len((depth - nildepth) * INDENTOR + pathname.split("\\")[-1]), len((depth - nildepth + 1) * INDENTOR + file))

    # Walk through tree, print it, and count up lines
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
                    local_count = fc.countLines(pathname + "\\" + file, do_blank_counting=do_blank_counting)  # Recursive call
                    display_string = (depth - nildepth + 1) * INDENTOR + file
                    print(display_string, TOC_CHAR*(max_indent-len(display_string)+3), local_count)
                    count += local_count

    return count


if __name__ == "__main__":
    this_parent = fc.Path(__file__).parents[0]
    print("Total:", countLines(this_parent))