import glob
import os
# create a directory
new_dir = "linux"
# path to the current directory
parent_directory = os.path.dirname(__file__)

mode = 0o700
# set the path
file_path = os.path.join(parent_directory, new_dir)

if (os.path.isfile(file_path)):
    print("Directory linux exists")
else:
    os.mkdir(file_path, mode)
    print("Directory created")

new_txt= open("test.txt", "x")
new_java= open("test.java", "x")
new_txt= open("test.txt", "x")

