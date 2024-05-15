# using the try and except block to handle errors
try:
    x = 10 / 0
    print("Value of x is {} is a result of 10/0".format(x))
    # expecting a ZeroDivisionError
except ZeroDivisionError:
    print("Error : Cannot Divivde by Zero")
