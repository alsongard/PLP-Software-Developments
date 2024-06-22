"""
Contenxt manager in file handling:
"""

with open("./names.txt", "w+") as file:
    file.write("Using context manager does not require one to close the file\nas these will be performed automatically")
    file.seek(0)
    contents = file.readlines()
    print(f"The file content of the filename names.txt are {contents}")
