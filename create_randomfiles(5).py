import os
import random
import string

def ranNUM(length=7):
    """ will generate random file name with lower & uppercase letters"""
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=length)) + '.txt'

def fetch_User_Folder():
    """ fetches the user profile folder name for directory creation """
    return os.path.expanduser("~")

def createFILES(directory='randomFiles', count=5):
    """ Create Directory 'randomFiles' and create 10 files with randomly generated names (using the ranNUM function)"""
    user_folder = fetch_User_Folder()
    target_dir = os.path.join(user_folder, directory)
    os.makedirs(target_dir, exist_ok=True)
    for x in range(count):
        filename = ranNUM()
        filepath = os.path.join(target_dir, filename)
        with open(filepath, 'w') as j:
            j.write(f"this is file: {filename}\n")
    print(f"{count} files created in '{target_dir}'")

createFILES()