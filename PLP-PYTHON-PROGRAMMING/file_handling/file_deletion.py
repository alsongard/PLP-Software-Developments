# to delete a file we use the os module
import os
filename = input("Enter the name of the file you wish to delete")
if os.path.exists(filename):
    os.remove(filename)
    print("The filename {} has been deleted.".format(filename))
else:
    print(f"The file name {filename} does not exist")

