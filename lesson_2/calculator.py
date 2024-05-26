"""Small calculator program. """
# This is the first small program in lesson 2 of launch school PY101
# Command line calculator
# Ask the user for the first number
# Ask the user for the second number
# Ask the user for an operations to perform
# Perform the operation on the two numbers
# Print the result to the terminal


def prompt(message):
    """Helper function for prompting user. """

    print(f'==> {message}')

def invalid_number(number_str):
    """Number checker for user input. """

    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

# Ask the user for the first number.
prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm.. that doesn't look like a valid number.")
    number1 = input()

#Ask user for the second number.
prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm.. that doesn't look like a valid number.")
    number2 = input()

prompt("""What operation would you like to perform? 
       1) Add 2) Subtract 3) Multiply 4) Divide""")
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

match operation:
    case '1': # '1' represents addition
        output = int(number1) + int(number2)
    case '2': # '1' represents subtraction
        output = int(number1) - int(number2)
    case '3': # '3' represents multiply
        output = int(number1) * int(number2)
    case '4': # '4' represents division
        output = int(number1) / int(number2)

prompt(f'The result is: {output}')
