import os

dir_path = os.path.join(os.path.expanduser("~"), "randomfiles")


def numberoffiles():
    numfiles = 0
    for x in os.listdir(dir_path):
        numfiles = numfiles + 1
        return numfiles

print("Files:", numberoffiles())
