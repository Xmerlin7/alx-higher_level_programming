#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
print(f"Last digit of {number} is {last_digit} ", end="")
if last_digit > 5:
