### PythonLineCounter.FolderCounter.py ###
# Author: T. Bauwens
# Date: 2020-2-4

import FileCounter as fc
import os

IGNORE_MATCHING = [".idea", "__pycache__", ".git"]
IGNORE_CONTAINING = [".wav", ".png", ".svg", ".jpg", ".jpeg", ".pdn", ".pdf", ".mp4", ".mp3", ".docx"]

def isIgnored(string, matching_list, containing_list):
    return (string in matching_list) \
           or any([contained_string in string for contained_string in containing_list])

def countLines(folderpath:fc.Path, ncontaining=None, nmatching=None, do_blank_counting=True):
    # Default values
    if ncontaining is None:
        ncontaining = []
    if nmatching is None:
        nmatching = []

    ncontaining += IGNORE_CONTAINING
    nmatching += IGNORE_MATCHING

    # Build tree of directory
    walked_path = os.walk(folderpath)

    # Walk through tree, print it, and count up lines
    count = 0
    nildepth = len(str(folderpath).split("\\"))

    for tup in walked_path:
        pathname = tup[0]
        folders  = tup[1]
        files    = tup[2]

        if not(any([
                isIgnored(path_part, matching_list=nmatching, containing_list=ncontaining)
                for path_part in pathname.split("\\")]
        )):
            depth = len(pathname.split("\\"))
            print((depth-nildepth)*"    " + pathname.split("\\")[-1])

            for file in files:
                if not(isIgnored(file, matching_list=nmatching, containing_list=ncontaining)):
                    tempcount = fc.countLines(pathname + "\\" + file, do_blank_counting=do_blank_counting)
                    print((depth-nildepth+1)*"    " + file, tempcount)
                    count += tempcount

    return count


if __name__ == "__main__":
    #this_parent = fc.Path(__file__).parents[0]
    #print(countLines(this_parent))

    print(countLines("D:\\Programming\\Python\\PO3-SoundBytes", IGNORE_CONTAINING, IGNORE_MATCHING))