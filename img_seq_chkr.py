"""Find missing files in a numbered file sequence in a specific directory.""

Provide an absolute path to the directory to be checked. Script prints a list of
missing file numbers. Particularly useful when downloading image sequences from
a cloud rendering service. Sometimes a few frames don't make it, and it can be
time-consuming to find them manually.
"""

import os
import re

def listVisibleFiles(path):
    """Create list of only visible files in directory."""
    files = []
    for file in os.listdir(path):
        if not file.startswith('.'):
            files.append(file)
    return files

def getNumSubString(str):
    """Extract file number from file name."""
    array = re.findall(r'[0-9]+', str)
    val = array[0]
    return val

def getZeroPadding(path):
    """Get original zero padding, so can be re-added."""
    files = listVisibleFiles(path)
    zero_padding = len(getNumSubString(os.path.splitext(files[0])[0]))
    return zero_padding

def getMissingElements(L):
    """Find missing values in sorted sequence of integers using sets."""
    start = L[0]
    end = L[-1]
    return sorted(set(range(start, end + 1)).difference(L))

def checkFileSequence(path):
    """Manages the file sequence check."""
    files = listVisibleFiles(path)
    file_nums = []

    for file in files:
        file_nums.append(int(getNumSubString(os.path.splitext(file)[0])))

    file_nums.sort()
    missing_files = getMissingElements(file_nums)

    return missing_files


if __name__ == "__main__":
    path = input("Paste absolute path to image sequence directory: \n")
    missing_files = checkFileSequence(path)
    missing_files_padded = []
    zero_padding = getZeroPadding(path)
    for file in missing_files:
        missing_files_padded.append(str(file).zfill(zero_padding))

    print("Number of missing files: " + str(len(missing_files)))
    print(*missing_files_padded, sep=', ')
