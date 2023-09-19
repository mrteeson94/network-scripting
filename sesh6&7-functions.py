import os
import random

# OS Functions
# os.chdir(r"C:\Users\AKATY\Desktop\Python")
# base_dir = os.getcwd()
# print(os.getcwd())
# print((os.listdir()))
#
# rel_path = r"test"
# abs_path = os.path.join(base_dir, rel_path)
# print(abs_path)
# print(os.listdir(abs_path))
#
# dirname, basename = os.path.split(abs_path)
# print("Directory Name: ", dirname, '\n', "Base Name: ", basename)

# **OS EX student list**
# Open and read studentList.txt
# file_path = r"C:\Users\AKATY\Desktop\studentList.txt"
# dir_path = r"C:\Users\AKATY\Desktop\Std"
# if os.path.exists(file_path):
#     file_list = open(file_path, 'r')
#     for student in file_list:
#         os.chdir(dir_path)
#         student = student.strip()
#         if not os.path.exists(student):
#             os.mkdir(student)
#
#         else:
#             print("exist, therefore skip")
#             continue
#     file_list.close()
# else:
#     print("Cannot locate filepath of studentlist.txt")

# For each new student in the file, create a dir in Std folder.

# EX: Generate 5 random nums from 1 - 100
# for i in range(0, 5):
#     print(random.randint(1, 100))

# map(function, iterate), filter(), Lambda function EX


def function_square(x):
    return x**2


def check_even(x):
    if x % 2 == 0:
        return True


result = lambda x: x*x


def main():
    nums = [1, 2, 3, 4, 5]
    squared_nums = map(function_square, nums)
    list_num = list(squared_nums)
    print(list_num)

    filter_out_odds = filter(check_even, nums)
    print(filter_out_odds)
    print(list(filter_out_odds))
    print(result(5))


main()


# Import libraries
# Create a module file named
# Create 4 functions within module and call the module here
# import myModule
# first, last, age = myModule.func1()
# print(f"Hi {first} {last} aged {age}")
#
# average = myModule.func2(1, 2, 3)
# print(f"The average from provided inputs is {average}")
#
# highest_num = myModule.func3(10, 100)
# print("Highest input number is", highest_num)
#
# total_average = myModule.func4(10)
# print("Total average from incremental sum of 10 is", total_average)

# Ex1 function(printname)
# def main():
#     first_name = input("Hello world, what is your name? ")
#     last_name = input("Can i get your surname? ")
#     message(first_name, last_name)
#
#
# def message(arg1, arg2):
#     print(f"Hello {arg1} {arg2}, I am Python")
#
#
# main()

# Ex2 Provide 2 param to f(x)
# def main():
#     num_min = int(input("Provide a starting number: "))
#     # num_max = int(input("Provide an ending number: "))
#     print_even(num_min, max_=10)
#
#
# def print_even(min_, max_):
#     for i in range(min_, max_):
#         if i % 2 == 0:
#             print(i)
#
#
# main()


# Ex3 Global variable change and default param, recursion
# num = 10


# def main():
#     print("value of num is", num)
#     # change_num()
#     print("new value of num is ", num)
#     my_country("Sweden")
#     sum_of_series(num)


# def change_num():
#     global num
#     num = num*10


# def my_country(country="Australia"):
#     print(f"I am from {country}")
#
#
# # Recursion, remember the function calls on itself until the condition doesn't meet
# # THEN it returns the values up the callback of the function which then executes the 1 + function
# # displaying result in + 1 increments
# def sum_of_series(num_):
#     if num_ > 0:
#         result = num_ + sum_of_series(num_ - 1)
#         print(result)
#     else:
#         result = 0
#     return result
#
#
# main()
