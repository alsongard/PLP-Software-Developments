"""
One can assign an exception to a variable
"""
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Error : ", e)
    print("Exception type : ", type(e))
    print("Exception arguments : ", e.args)