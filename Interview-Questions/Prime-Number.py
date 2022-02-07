# write a python program to check if a given number is prime

num = int (input("Enter Number : "))
print(not any(num % a == 0 for a in range(2, num)))
