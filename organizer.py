# get the names of all files within this folder

import os
import shutil


import os
import shutil

def organize(folder_path):
    # Check if the provided path exists
    if not os.path.exists(folder_path):
        print("The provided folder path does not exist.")
        return

    # Change to the provided directory
    os.chdir(folder_path)

    list_of_files = os.listdir()

    # find the extension of each file and print it
    for file in list_of_files:
        name, ext = os.path.splitext(file)
        print(ext)

        # create a new folder for each extension
        # move the files into the correct folder
        # if the folder already exists, move the files into the folder
        if ext == "":
            continue
        if os.path.exists(ext):
            shutil.move(file, os.path.join(folder_path, ext))
        else:
            os.makedirs(os.path.join(folder_path, ext))
            shutil.move(file, os.path.join(folder_path, ext))
    print("Sorting and moving completed.")