file = open("./README.md", "a")
file.write("There 4 main modes which can be used with files namely : \n1: write \n2: read \n3:append \n4:x(exclusive write only)")
file.close()
print("File attributes are : ")
print(f"the file name is {file.name}")