#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
message = "Last digit of {} is {} and is "
if last_digit > 5:
    print(message.format(number, last_digit) + "greater than 5")
elif last_digit == 0:
    print(message.format(number, last_digit) + "0")
else:
    print(message.format(number, last_digit) + "less than 6 and not 0")
