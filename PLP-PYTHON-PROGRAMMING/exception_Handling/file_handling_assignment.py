"""
file handling assignment
"""
with open("./my_file.txt", "w+") as file:
    file.write("Hello These is my first sentence\n")
    file.write("Favourite number is 1234432423432\n")
    file.write("Born in  1990\n")
    file.write("I am a software developer\n")
    file.seek(0)#to place the file pointer at the beginnig of the file
    contents = file.read()
    print(contents)

try:
    myfile = input("Enter the file name or file path for file you wish to read : ")
    with open(myfile, "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: File name {} cannot be found, please check again or provide the whole file path".format(myfile))
finally:#executed whether error or no error occurs
    print("End of program")