import os
from os import path
import datetime
from time import time

# printing os name
print(os.name)

# check if items exists and its type
print("item exist=>" + str(path.exists("testfile.txt")))
print("Is file=>" + str(path.isfile("testfile.txt")))
print("Is directory =>" + str(path.isdir("testfile.txt")))

# Printing real path
print("File real path: " + str(path.realpath('testfile.txt')))

# Get modification time
# t = time.ctime(path.getmtime("textfile.txt"))
# print(t)
