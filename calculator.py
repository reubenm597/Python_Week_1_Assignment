#A calculator that performs basic arithmetic operations

#The calculator will be able to perform addition, subtraction, multiplication, division, exponention,floor division, and modulus.

#The calculator will take two numbers and an operator as input and return the result of the operation.

#The calculator will also include float data types.

#Step 1: Input the first number
num1 = float(input("Enter the first number: "))

#Step 2: Input the second number
num2 = float(input("Enter the second number: "))

#Step 3: Input the operator

#Addition
sum = num1 + num2

#Subtraction
difference = num1 - num2

#Multiplication
product = num1 * num2

#Division
division = num1/ num2

#Exponenentiation
exponent = num1 ** num2

#Floor Division
floor_division = num1 // num2

#Modulus
modulus = num1 % num2

#Result output
print(f"Addition: {sum}")
print(f"Subtraction: {difference}")
print(f"Multiplication: {product}")
print(f"Division: {division}")
print(f"Exponentiation: {exponent}")
print(f"Floor Division: {floor_division}")
print(f"Modulus: {modulus}")


