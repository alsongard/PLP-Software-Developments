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

#enter multiple user_data
#split method is used to seperate data entered
#map() function takes in a function and iterates through the values
numbers = list(map(int, input("Enter a list of numbers seperated by a comma").split(",")))
print(numbers)
sum = 0
for i in numbers:
    sum+=i
print(sum)

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



"""
Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the 
elements that are common to both sets.
"""

#enter data for set 1
my_set = set()
print(type(my_set))

#capture data from user
num_range = input("How many number would you like to enter (1, 2, 3, 4, 5,..) : ")
for i in range(int(num_range)):
    number = input("Enter number : ")
    my_set.add(number)
print(my_set)

new_range = int(input("Enter the number of times you would like to enter numbers : "))
new_set = set()
for i in range(new_range):
    number = input("Enter number :  ")
    new_set.add(number)
print(new_set)

#common set
data = set()
print(f"Common elements in new_set and my_set is {my_set&new_set}")
data = my_set.intersection(new_set)
print(data)

"""
Create a program that stores a list of words. Then, use list comprehension to create a new list
that contains only the words that have an odd number of characters.
"""
#create a list of words
list_words = []
list_words = input("Write a meaningful sentence : \n").strip().split()
print(list_words)
for item in list_words:
    if len(item)%3 == 1:
        print(item)
