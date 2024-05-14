# appending data to a file use the append mode and write() method
file = open("./README.md", "a+")
file.seek(0)
contents = file.read()

print(contents)
file.write("### Modes \n >>1. Append Mode :\n The append mode is used to addd data to file")
