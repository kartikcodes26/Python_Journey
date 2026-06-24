import os

print(os.getcwd()) # Currrnt working directory

files = os.listdir(".") # Gives the list of all files
for element in files:
    print(f"{element}", end = '\n')
   
os.mkdir("New Folder") # Create Folder 
os.rmdir("New Folder") # Delete Folder

os.chdir("./") # Change directory

os.makedirs("newfolder/nestedfolder")