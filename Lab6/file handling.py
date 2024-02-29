#1 - list only directories, files in a specified path and all directories/files
import os
path = r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab6"
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])

#2 - check for access to a specified path
import os
path = r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab6\file handling.py"
print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))

#3 - test whether a path exist
from pathlib import Path
path = Path(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab6\demo.txt")
if path.exists():
    print("The path exists.")
else:
    print("The path doesn't exist!")

#4 - count the number of lines in a text file
f = open(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab6\demo.txt", "r")
sum = 0
for line in f:
    sum += 1
f.close()
print(sum)

#5 - write a list to a file
str = input()
list = str.split()
with open(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab6\text.txt", "w") as f:
    for item in list:
        f.write(item + "\n")


#6 - generate 26 text  files from A to Z
for i in range(65, 65+26):
    filename = chr(i) + ".txt"
    f = open(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab6\Alphabet\\" + filename, "x")
    f.close()

#7 - copy the contents of the file to another file
with open(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab6\copytext.txt", "r") as f1:
    with open(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab6\text.txt", "a") as f2:
        f2.write("\n" + f1.read())

#8 - delete file by specified path
import os
path = r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab6\delete.txt"
if os.path.exists(path):
    os.remove(path)
else:
    print("The path doesn't exist! Try again.")
