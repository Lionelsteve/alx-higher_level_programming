#!/usr/bin/python3
for n in range(0, 100):
    if n < 99:
        print("{}{}, ".format((n // 10), (n % 10)), end = "")
    else:
        print("{}".format(n))
