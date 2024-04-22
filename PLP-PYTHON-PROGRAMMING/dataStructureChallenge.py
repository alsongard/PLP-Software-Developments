"""
Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
"""
my_list = []

number =int(input("enter any number : \n"))
my_list.append(number)
print(my_list)
sum = 0
for item in my_list:
    sum+=item
print(f"The sum of all the numbers in my_list is {sum}")

"""
Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
"""

my_books = ("Harry Porter", "Rich and Poor Dad", "Bible", "The Hobbit", "Twilight")
for book in my_books:
    print(book)

"""
Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. 
Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
"""
person = {}
name = input("Enter users name : ")
age = input("Enter age of user : ")
fav_color = input("Enter your Favourite color : ")
person["Name"] = name
person["Age"] = age
person["Color"] = fav_color
print(person)


#enter multiple user_data
numbers = list(map(int, input("Enter a list of numbers seperated by a comma").split(",")))
print(numbers)
