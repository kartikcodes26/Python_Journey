import os

path = os.path.join("kartik", "Music", "newsong.mp4")
print(path)

file = os.listdir()

for element in file:
    if(element.endswith(".txt")):
        print(element)
        
os.rename("test.txt", "rest.txt") # From, To