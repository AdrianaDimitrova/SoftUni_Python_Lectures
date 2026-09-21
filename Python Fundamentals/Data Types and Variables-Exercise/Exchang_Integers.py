num1 = int(input())
num2 = int(input())

print(f"Before: a = {num1} b = {num2} ")

temp = num1
num1 = num2
num2 = temp

print(f"After: a = {num1} b = {num2}")