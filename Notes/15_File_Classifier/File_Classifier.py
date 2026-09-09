import os
import random
import shutil

folder_path = "D:/02_Deep Python/15_File_Classifier"
filetypes = ("pdf", "doc", "csv", "png", "txt")

# Populate the directory for testing
def populate(n):
    for i in range(n):
        choice = random.choice(filetypes)
        file_path = os.path.join(folder_path, f"file{i}.{choice}")
        open(file_path, 'w').close() # Create the file

# Depopulate the directory
def depopulate():
    i = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.endswith(filetypes):
            os.remove(file_path)
            i += 1

        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            i += 1



    print(f"Removed {i} files and folders")

def classify():
    # Create necessary folders
    for folder in filetypes:
        target_folder_path = os.path.join(folder_path, f"{folder} files")
        os.makedirs(target_folder_path, exist_ok=True)

    # Place files into their respective folders
    for filenames in os.listdir(folder_path):
        if(filenames.endswith(filetypes) == False):
           continue;
        curr_path = os.path.join(folder_path, filenames)
        file_ext = os.path.splitext(filenames)[1][1:] # Take the extension out
        to_move = os.path.join(folder_path, f"{file_ext} files", filenames)
        os.rename(curr_path, to_move)




populate(100)
classify()
a = input("Press anything to depopulate : ")
depopulate()

