# write a python program to find Factorial of a number

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact

def Test_Factorial():
    assert factorial(2) == 2, "Test 1 Not Passed."
    assert factorial(3) == 6, "Test 2 Not Passed."
    assert factorial(4) == 24, "Test 3 Not Passed."
    assert factorial(5) == 120, "Test 4 Not Passed."


if __name__ == "__main__":
    Test_Factorial()
    print("All Tests are passed")
