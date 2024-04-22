#Week 2 Assignment
#appending
my_list = []
for item in [10, 20, 30, 40]:
    my_list.append(item)
print(my_list)

#insert(index, value)
my_list.insert(2, 15)
print(my_list)

#extend(list)
my_list.extend([50, 60, 70])
print(my_list)

print(my_list.pop())
print(my_list)

my_list.sort()
print(my_list)
i = 0
for item in my_list:
    if item == 30:
        print(f"The index of 30 is {i}")
    i+=1
