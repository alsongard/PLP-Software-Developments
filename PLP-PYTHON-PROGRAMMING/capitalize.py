# write a function that capitalize each word in mystring
def capitalize(mystring):
    if type(mystring) == str:
        mystring = mystring.title()
        print(mystring)

capitalize("my name is dreamer lover willer")