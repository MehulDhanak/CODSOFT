# Python program for simple calculator

def add(no1, no2):
	return no1 + no2


def subtract(no1, no2):
	return no1 - no2


def multiply(no1, no2):
	return no1 * no2


def divide(no1, no2):
	return no1 / no2


print("Please select operation -\n" 
		"1. Add\n" 
		"2. Subtract\n" 
		"3. Multiply\n" 
		"4. Divide\n")


cal = int(input("Select operations form 1, 2, 3, 4 :"))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if cal == 1:
	print(a, "+", b, "=",add(a, b))
elif cal == 2:
	print(a, "-", b, "=",subtract(a, b))
elif cal == 3:
	print(a, "*", b, "=",multiply(a, b))
elif cal == 4:
	print(a, "/", b, "=",divide(a, b))
else:
	print("Invalid input")