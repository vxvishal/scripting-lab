#print biggest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("Biggest number is: ", a)
elif b > a and b > c:
    print("Biggest number is: ", b)
elif c > a and c > b:
    print("Biggest number is: ", c)
else:
    print("All numbers are equal")
