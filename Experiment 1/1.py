n = int(input("Enter a number: "))
n1 = n
sum = 0
current = 1
while n1!=0:
    sum += current
    current += 2
    n1 -= 1
print("Sum of first", n, "odd numbers is", sum)