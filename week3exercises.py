#  A fruit company sells bananas for £3.00 a kilogram plus £4.99 per order for postage and
# packaging. If an order is over £50.00, the P&P is reduced by £1.50. Write a function
# order_price(quantity) that takes an int parameter quantity representing the number of
# kilo of bananas for the order, and returns the cost of the order in pence (as an int)
# Solution 1:
# def order_price(quantity):
#     price = 3
#     total = quantity * price
#     if total > 50:
#         return int((total + 3.49) * 100)
#     else:
#         return int((total + 4.99) * 100)
#
# order = int(input("Please enter the weight of the bananas in Kilos: "))
# print(order_price(order))

# Write a function maximum_heart_rate(age) that takes the age of the person as
# parameter (an int) and returns the maximum heart rate for that person (as an int). The
# maximum heart rate is given by:
# 𝑚𝑎𝑥𝐻𝑒𝑎𝑟𝑡𝑅𝑎𝑡𝑒 = 208 ― 0.7 × 𝑎𝑔𝑒

# Write a second function training_zone(age, rate) that takes the age (as an int)
# and rate (the heart rate as an int) from the person as parameters and returns a string
# representing one of the four possible training zones of a person based on his or her age and
# training heart rate, rate. The zone is determined by comparing rate with the person's
# maximum heart rate m:
# Solution 2:

# def maximum_heart_rate(age):
#     max_rate = (208 - 7) * age
#     return int(max_rate)
#
# def training_zone(age, rate):
#     max_heart_rate = maximum_heart_rate(age)
#     if rate >= 0.9 * max_heart_rate:
#         return "Interval training"
#     elif 0.7 * max_heart_rate <= rate < 0.9 * max_heart_rate:
#         return "Threshold training"
#     elif 0.5 * max_heart_rate <= rate < 0.7 * max_heart_rate:
#         return "Aerobic training"
#     else:
#         return "Couch potato"
#
#
# input_age = int(input("Please enter your age: "))
# input_rate = int(input("Please enter your heart rate: "))
# print(training_zone(input_age, input_rate))

# Solution 3:

# def is_valid_password(password):
#     if has_upper and has_lower and has_digit and min_length:
#         return True
#     else:
#         return False
#
# input_password = str(input("Please enter your password: "))
# min_length = len(input_password) >= 8
# has_upper = any(char.isupper() for char in input_password)
# has_lower = any(char.islower() for char in input_password)
# has_digit = any(char.isdigit() for char in input_password)
# print(is_valid_password(input_password))

# TODO: write tests for solution 3

# Write a function sum_digits(number) to calculate and return the sum of the digits of a
# given whole number (an int NOT a string) given as a parameter.
# Solution 4:

# def sum_digits(number):
#     return sum([int(digit) for digit in str(number)])
#
# num_input = int(input("Please enter a number: "))
# print(sum_digits(num_input))

# Write a function pairwise_digits(number_a, number_b) that takes two whole
# numbers represented by strings (not int) as parameters and returns a binary string where a
# character 1 is used if the digits at the same index are the same, a 0 otherwise. If the two strings
# have different lengths, the output should be padded with 0s on the right-hand side to match the
# length of the longest string. Examples are given in the table below.

def pairwise_digits(number_a, number_b): # TODO: convert to a list and compare index?

a_input = str(input("Please enter a whole number: "))
b_input = str(input("Please enter a second whole number: "))