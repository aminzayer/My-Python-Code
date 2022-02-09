# write a python program to produce fibonacci series
a = int(input("Enter the terms :"))
first = 0
Sum = 1
if a <= 0:
    print("The requested series is ", first)
else:
    print(first, Sum, end=" ")
    for x in range(2, a):
        Next = first + Sum
        print(Next, end=" ")
        first = Sum
        Sum = Next
print("\n")