# write a function that converts mystring to lowercase
def lower_case(mystring):
    if type(mystring) == str:
        mystring = mystring.lower()
        print(mystring)