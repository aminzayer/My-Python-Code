# Write a Python Program to Produce Star Triangle.
def PyFuncStarTriangle(size):
    for x in range(size):
        print(" " * (size-x-1) + "*" * (2 * x + 1))

PyFuncStarTriangle(10)