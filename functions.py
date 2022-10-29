# def areaOfCircle(radius):
#     area = 3.14 * radius * radius
#     typeOfCircle = "2D"
#     colorOfCircle = "Red"
#     return area, colorOfCircle

# circleArea, circleColor = areaOfCircle(5)
# print("Area of circle is", circleArea)
# print("Color of circle is", circleColor)

#function to compute factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#function to find reverse of a number
def reverse(n):
    rev = 0
    while n > 0:
        rev = (rev * 10) + (n % 10)
        n = n // 10
    return rev

#function to find addition of cubes of digits of a number
def sumOfCubes(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + (digit * digit * digit)
        n = n // 10
    return sum

#function to check if a number is an armstrong number
def isArmstrong(n):
    if n == sumOfCubes(n):
        return True
    else:
        return False
        