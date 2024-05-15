"""
handling multiple errors by using a single except block
"""
try:
    number = int(input("Enter any number : "))
    answer = 10000 / number
    print("You guessed correctly")
except (ValueError, ZeroDivisionError):
    print("Error : Enter a non-zero numberic number. ")