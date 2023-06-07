#!/usr/bin/python3
# 6-print_comb3.py

"""
Prints all possible combinations of 2 digits in ascending order.

The 2 digits must be different - 01 and 10 are considered identical.
"""

for a in range(0, 10):
    for b in range(a + 1, 10):
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
        else:
            print("{}{}".format(a, b), end=", ")
