# a = 100000
# b = 25
# c = 0
# d = round(a+b/c)
# print(d)

salary = int(input("Enter your salary: "))
daysWorked = int(input("Enter the number of days worked: "))
daysInMonth = int(input("Enter the number of days in the month: "))

try:
    pay = round(salary*daysWorked/daysInMonth)
    print(pay)

except ZeroDivisionError as e:
    print("Divided by zero")

except ValueError as e:
    print("A value error occurred")

except Exception as e:
    print("An error occurred", e)

print("Outside exception")
