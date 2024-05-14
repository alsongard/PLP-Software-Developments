# use the write only exclusive mode to create a file
file = open("./newfile.txt", "x+")
file.writelines(["Hello we are the dreamers", "\nIt's who we are, we are the champions"])
file.close()
