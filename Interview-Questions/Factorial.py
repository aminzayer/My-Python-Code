# write a python program to find Factorial of a number
import validator
from tkinter import N
import test_framework

def factorial(n):
    if n < 0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact =1
        while n>1:
            fact *=n
            n-=1
        return fact

num = int(input("Enter the Number: "))
print ("Factorial of",num," is ",factorial(num))

# Write Test Function
def Validate_factorial_Function(n):
    return
