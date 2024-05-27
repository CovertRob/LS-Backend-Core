"""Small calculator program. """

import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# PSEUDOCODE ->
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

# Global variable that will server as tracker for status of user wanting to continue with another calculation or not.
execution_tracker = True

# Function to ask user if they want to conntinue for another calculation or exit the program.
def continue_yes_no():
    
    prompt(MESSAGES['continue_prompt'])
    
    user_continue = input()
    
    while user_continue not in ['yes', 'no']:
        prompt(MESSAGES['invalid_yes_no'])
        user_continue = input()
    
    if user_continue == 'yes':
        return prompt(MESSAGES['continue'])
    elif user_continue == 'no':
        global execution_tracker
        execution_tracker = False
        return prompt(MESSAGES['exit'])
    
# Operator prompt to ask user what calculation they want to perform 
def operator_prompt():
    return prompt(MESSAGES['operator_prompt'])

def main():

    prompt(MESSAGES['welcome'])
    
    while execution_tracker:
        # Ask the user for the first number.
        prompt(MESSAGES['number1'])
        number1 = input()

        while invalid_number(number1):
            prompt(MESSAGES['invalid_number'])
            number1 = input()
        
        # Ask user for the second number.
        prompt(MESSAGES['number2'])
        number2 = input()

        while invalid_number(number2):
            prompt(MESSAGES['invalid_number'])
            number2 = input()

        operator_prompt() # prints out the operator prompt
        operation = input()

        while operation not in ['1', '2', '3', '4']:
            prompt(MESSAGES['invalid_operator'])
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

        prompt(f"The result is: {output}")
        continue_yes_no()



# Execution control function
if __name__ == "__main__":
    main()

# JSON implementation ___