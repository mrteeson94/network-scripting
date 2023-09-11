# practice
# score = float(input("Please provide your mark:"))
#
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 50:
#     print("D")
# elif score < 50:
#     print("E")

# EX1: GET score from user
# score = int(input("What score did you get (0-100):"))
# if 80 <= score <= 100:
#     print("High Distinction")
# elif 50 <= score < 80:
#     print("Pass")
# else:
#     print("FAIL")

# EX2: GET user input age, australian permanent resident ?, are they are student
# GET 3 inputs age, isResident, isStudent
# age = int(input("What is your age:"))
# isResident = input("Are you permanent resident (yes or no):").lower() == "yes"
# isStudent = input("Are you currently a student(yes or no):").lower() == "yes"
# CHECK IF 18 <= age <=25
# if 18 <= age <= 25:
#     if isResident and isStudent:
#         print("You are eligible for this job!")
# else:
#     print("Sorry, you are not eligible for this job!")

# EX3: check person eligible with citizenship status,20 <= age <= 50, 4years work exp
# age = int(input("What is your age:"))
# isResident = input("Are you permanent resident or citizen (yes or no):").lower() == "yes"
# hasStdExperience = int(input("How many years of IT experience do you have:")) >= 4
# # Pass initial check: ASK user for full name AND postal code PRINT "[name] with [postcode] to progress application"
# if 20 <= age <= 50 and isResident and hasStdExperience:
#     fullname = input("whats your full name:")
#     userPostcode = input("whats your postcode:")
#     print(f"{fullname} with {userPostcode} is registered as an eligible job candidate")
# else:
#     print("Sorry, you are not eligible for this role")

# EX4: GET user price and quantity of purchased item.
# def calculate_total_price(price, quantity):
#     total = price * quantity
#     return total
# def calculate_total_price(user_price, user_quantity):
#     total = price * quantity
#     if total > 1000:
#         print(f"Yay, discount applied, you saved 10% or ${total*0.1}")
#         total = total - (total*0.1)
#     return total
#
#
# price = float(input("What is the price of your item:"))
# quantity = float(input("What is the quantity of your item:"))
# # assign var to function
#
# total_price = calculate_total_price(price, quantity)
# print(f"Your total is: ${total_price}")

