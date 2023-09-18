# OS Functions
import os
os.chdir(r"C:\Users\AKATY\Desktop\Python")
base_dir = os.getcwd()
print(os.getcwd())
print((os.listdir()))

rel_path = r"test"
abs_path = os.path.join(base_dir, rel_path)
print(abs_path)
print(os.listdir(abs_path))

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
