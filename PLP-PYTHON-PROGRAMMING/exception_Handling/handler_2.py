"""
another example to illustrate try... except... clause

"""
try: 
    number = int(input("Enter any number : "))
    answer = 10000 / number
    print("You guessed correctly")
except ValueError:
    print("Error: Enter a valid number between 0 and 100000000*")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

