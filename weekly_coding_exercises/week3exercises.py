
# Solution 1:
def order_price(quantity):
    price = 3
    total = quantity * price
    if total > 50:
        return int((total + 3.49) * 100)
    else:
        return int((total + 4.99) * 100)

# order = int(input("Please enter the weight of the bananas in Kilos: "))
# print(order_price(order))

# Solution 2:
def maximum_heart_rate(age):
    max_rate = (208 - 7) * age
    return int(max_rate)

def training_zone(age, rate):
    max_heart_rate = maximum_heart_rate(age)
    if rate >= 0.9 * max_heart_rate:
        return "Interval training"
    elif 0.7 * max_heart_rate <= rate < 0.9 * max_heart_rate:
        return "Threshold training"
    elif 0.5 * max_heart_rate <= rate < 0.7 * max_heart_rate:
        return "Aerobic training"
    else:
        return "Couch potato"

# input_age = int(input("Please enter your age: "))
# input_rate = int(input("Please enter your heart rate: "))
# print(training_zone(input_age, input_rate))

# Solution 3:
def is_valid_password(password):
    min_length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    if has_upper and has_lower and has_digit and min_length:
        return True
    else:
        return False

# input_password = str(input("Please enter your password: "))
# print(is_valid_password(input_password))

# Solution 4:
def sum_digits(number):
    return sum([int(digit) for digit in str(number)])

num_input = int(input("Please enter a number: "))
print(sum_digits(num_input))

# Solution 5:
def pairwise_digits(number_a, number_b):
    maximum = max(len(number_a), (len(number_b)))
    a = number_a.ljust(maximum, "0")
    b = number_b.ljust(maximum, "0")
    result = []

    for num in range (maximum):
        if a[num] == b[num]:
            result.append(1)
        else:
            result.append(0)
    return str(result)

# a_input = str(input("Please enter a whole number: "))
# b_input = str(input("Please enter a second whole number: "))
# print(pairwise_digits(a_input, b_input))
