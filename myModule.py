# Contains 4 functions


# Function 1: get full username, age and return them
def func1():
    first_name = input("What is your firstname? ")
    last_name = input("What is your firstname? ")
    age = int(input("what is your age? "))
    return first_name, last_name, age


# Function 2: 3 INT args, return average
def func2(num1, num2, num3):
    count = 3
    return (num1+num2+num3)/count


# Function 3: 2 INT args, return greater num
def func3(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        print("Both numbers are equal")


# Function 4: 1 INT arg, calculate the avg of numbers leading up to that num
def func4(num1):
    total = 0
    for i in range(1, num1+1):
        total = total + i
        print(total)
    print(f"average from 1 - {num1} is {total/num1}")
    return total/num1

