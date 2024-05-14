# reading filec contents using the readlines() and readline() methods
file = open("./newfile.txt", "r")
contents = file.readlines()
print(contents, end="\n")
file.close()
