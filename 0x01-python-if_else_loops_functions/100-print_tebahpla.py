#!/usr/bin/python3
# 100-print_tebahpla.py

""""Prints alphabet in reverse alternating upper and lower-case."""
j = 0
for k in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(k - j)), end="")
    j = 32 if j == 0 else 0
