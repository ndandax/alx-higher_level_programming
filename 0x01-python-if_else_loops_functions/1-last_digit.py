#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
y = str(number)
if int(y[-1]) > 5:
    print("Last digit of " + y + " is " + y[-1] + " and is greater than 5")
elif int(y[-1]) == 0:
    print("Last digit of " + y + " is " + y[-1] \
+ " and is 0")
elif int(y[-1]) < 6 and y[-1] != 0:
    print("Last digit of " + y + " is " + y[-1] \
+ " and is less than 6 and not 0")
