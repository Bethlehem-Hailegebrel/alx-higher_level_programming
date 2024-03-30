#!/usr/bin/python3
#  prints all possible different combinations of two digits
for i in range(0, 10):
    for j in range(0, 10):
        if (i >= j):
            continue
        print("{}{}, ".format(i, j), end="")
print()
