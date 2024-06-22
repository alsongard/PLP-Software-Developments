def large_power(base, exponent):
    power_result = base ** exponent
    if power_result > 5000:
        return True
    else:
        return False
print(f"The result of the 2 numbers is {large_power(5,10)}")

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
print(f"the result of the number if its's divisible by ten is  {divisible_by_ten(100)}")