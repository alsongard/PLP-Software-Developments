"""
another example to illustrate try... except... clause

"""
try: 
    number = int(input("Enter any number"))
    answer = 10000 / number
    print("You guessed correctly")
except ValueError:
    print("Error: Enter a valid number (0,1....10...) or a floating number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

