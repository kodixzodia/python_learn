import os

dir_path= os.path.join(os.path.expanduser("~"), "randomFiles")

if not os.path.isdir(dir_path):
    print(f"Directorey does not exist: {dir_path}")
    exit(1)

for n in os.listdir(dir_path):
    filename = os.path.join(dir_path, n)
    if  n.endswith(".txt"):
        try:
            os.remove(filename)
            print("Successfully Deleted", filename)
        except:
            print("Unable to delete file", filename)
    else:
        print("Did NOT Delete:", filename)