# This is the first small program in lesson 2 of launch school PY101
# Command line calculator
# Ask the user for the first number
# Ask the user for the second number
# Ask the user for an operations to perform
# Perform the operation on the two numbers
# Print the result to the terminal

print('Welcome to Calculator!')

# Ask the user for the first number.
print("What's the first number?")
number1 = input()

#Ask user for the second number.
print("What's the second number?")
number2 = input()

#print(f'{number1} {number2}')

print('''What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide''')
operation = input()

if operation == '1': # '1' represents addition
    output = int(number1) + int(number2)
elif operation == '2': # '1' represents subtraction
    output = int(number1) - int(number2)
elif operation == '3': # '3' represents multiply
    output = int(number1) * int(number2)
elif operation == '4': # '4' represents division
    output = int(number1) / int(number2)

print(f'The result is: {output}')
