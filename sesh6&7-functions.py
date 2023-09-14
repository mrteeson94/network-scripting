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


# Ex3 Global variable change and default param
num = 10


def main():
    print("value of num is", num)
    change_num()
    print("new value of num is ", num)
    my_country("Sweden")


def change_num():
    global num
    num = num*10


def my_country(country="Australia"):
    print(f"I am from {country}")


main()
