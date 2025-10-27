import os

dir_path = os.path.join(os.path.expanduser("~"), "randomfiles")
numfiles = 0

def numberoffiles():
    for x in os.listdir(dir_path):
        numfiles = numfiles + 1

print("Files:", numfiles)
