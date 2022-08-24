#!/usr/bin/python3
def fizzbuzz():
    for y in range(1, 101):
        if y % 3 == 0 and y % 5 == 0:
            print("FizzBuzz", end=" ")
        elif y % 5 == 0:
            print("Buzz", end=" ")
        elif y % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{:d}".format(y), end=" ")
