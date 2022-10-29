#print biggest of 2 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Biggest number is: ", a)
elif b > a:
    print("Biggest number is: ", b)
else:
    print("Both numbers are equal")
    