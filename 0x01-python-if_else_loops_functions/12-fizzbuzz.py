#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    """Prints nums from 1 to 100 separated by a space.

    For multiples of 3, print Fizz instead of the num.
    For multiples of 5, print Buzz instead of the num
    For multiples of 3 and 5, print FizzBuzz instead of the num
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(num), end="")
