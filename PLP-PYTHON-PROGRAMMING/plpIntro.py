#variables 
site_name = "Power Learn Project"
print(site_name)

student_id = {112, 114, 116, 118, 115}
print(student_id)
print(student_id[0])
print(type(student_id))

#accessing values in a dictionary
# capital_city = dict(country = "Kenya" , city = "nairobi", country1 = "Italy", city = "Rome", country2 = "Nepal", city = "Kathmandu", country3 = "England", city = "London" )oddball
capital_city = {"Nepal":"Kathmandu", "Italy":"Rome", "England":"London"}

print(capital_city)
print(type(capital_city))

#implicit type conversion
num1 = 23
num2 = 19.23
sum = num1 + num2 
print(f"sum value is {round(sum, 2)} and datatype is {type(sum)}")

#explicit type conversion / guided by user using function e.g int(), float(), 
num_string = '12'
num_integer = 23

print(f"print data type of num_string is {type(num_string)} and value is {num_string}")

#perform typecasting
sum = num_integer + int(num_string)
print("value of sum is {}".format(sum))

#floor division return only interger not float number
print(10/3)
print(10//3)
#remainder use modulus sign
print(10%3)
#power
print(2**3)

#comparison
a = 10
b = 5
print(a > b)

#logical operators
print( a > b and a == 10)
#or
print(a > 12 or a > b)
#not
print(not a > 12)#negate the correct value using not expected False but get True 

#print(object= seperator= end= file= flush) All these are option of the print() function 
print("Good Morning!", end="\t")
print("Its a rainy day")
#end option is used to specify values to the end of the line e.g \t " " \n

#concatenated strings
print("Power Learning Project " + "Awesome")

#input
fname = input("enter your name :")
print(fname)

#issubclass()
print(issubclass(bool, int))#confirms that boolean class is a subclass of the int class
del(fname)
print(fname)