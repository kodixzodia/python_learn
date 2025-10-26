import os

dir_path = os.path.join(os.path.expanduser("~"),"randomFiles")
x = 1

for file in os.listdir(dir_path):
    srcpath = os.path.join(dir_path, file)
    newname = f"random_File_{x}" + ".txt"
    dstpath = os.path.join(dir_path, newname)

    if os.path.isfile(srcpath):
        os.rename(src=srcpath, dst=dstpath)
        x = x + 1
    else:
        print("error renamimg file")    