import numpy as np
a = np.array([1, 2, 3])
my_list = [4, 5, 6]
b = np.array(my_list)
print(f"a: {a}\nb : {b}" )
print(f"type of a ; {type(a)}\ntype of b : {type(b)}")

# 2D arrays
array_2d = np.array([[1, 2, 3],[4, 5, 6]])
print("2D array")
print(array_2d)

#performing mathematical operation
#addition of 2 np arrays
print(f"Sum of 2 np_arrays are {a + b}")
#subtraction of 2 np arrays
print(f"Subtraction of 2 np_arrays are {a - b}")
#multiplication of 2 np_arrays
print(f"Mutlipliation of 2 np_arrays are {a * b}")
#division of 2 np_arrays
print(f"Division of 2 np_arrays are {a / b}")
#vice versa of b/a
print(f"Division of b /a {b / a}")# the answer is in float to ensure homogenoues data type


#indexing and slicing
print("Indexing and slicing")
new_array = [10, 11, 12, 13, 14]
print(f"new_array : {new_array}")
#indexing
print("Indexing")
print(f"new_array[0] : {new_array[0]}") # 10
print(f"new_array[1] : {new_array[-1]}") # 14
#slicing
print("Slicing")
print(f"new_array[0:3] : {new_array[0:3]}") # [10, 11, 12] exclusing of the last index
print(f"new_array[1:] : {new_array[1:]}") # [11, 12, 13, 14] starting from index 1 to end


#reshaping 
newer_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Reshaping")
my_newer_array = newer_array.reshape(3, 3)
print(my_newer_array)