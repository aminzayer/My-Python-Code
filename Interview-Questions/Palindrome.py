# write a program in python to check if a given sequence is a palindrome

a = input("enter sequence:")
b = a[::-1]  # Revrese Sequence
if a==b:
    print("Palindrome")
else:
    print("Not Palindrome")
