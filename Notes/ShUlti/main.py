import os
import shutil as sh


sh.move("example.txt", "./Test Folder") # From, To
sh.copy2("Test Folder/example.txt", "Test Folder/ex2.txt")
# Copy while preserving most of the metadata
os.mkdir("Test Folder 2")
sh.copytree("Test Folder", "Test Folder 2") # Creates a nre folder, error if folder already exists

sh.rmtree("Test Folder 2") # Remove a folder whith the contents in it

total, used, free = sh.disk_usage("/")

print(f"Total: {total / (2**30):.2f} GB")
print(f"Used: {used / (2**30):.2f} GB")
print(f"Free: {free / (2**30):.2f} GB")

os.chdir("..")
print(os.getcwd())

os.system("cls")

