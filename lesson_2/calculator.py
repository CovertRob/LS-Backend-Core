"""Small calculator program. """

import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

LANGUAGE = 'en'

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


def messages(message, lang='en'):
    return MESSAGES[lang][message]

def set_language():
    global LANGUAGE
    print("For Spanish, please enter 'es', otherwise hit enter.")
    lang = input()
    if lang == 'es':
        LANGUAGE = lang
    else:
        print("Continuing program in English")

# Global variable that will server as tracker for status of user wanting to continue with another calculation or not.
execution_tracker = True

# Function to ask user if they want to conntinue for another calculation or exit the program.
def continue_yes_no():
    
    prompt(messages('continue_prompt', LANGUAGE))
    
    user_continue = input()
    
    while user_continue not in ['yes', 'no']:
        prompt(messages('invalid_yes_no', LANGUAGE))
        user_continue = input()
    
    if user_continue == 'yes':
        return prompt(messages('continue', LANGUAGE))
    elif user_continue == 'no':
        global execution_tracker
        execution_tracker = False
        return prompt(messages('exit', LANGUAGE))
    
# Operator prompt to ask user what calculation they want to perform 
def operator_prompt():
    return prompt(messages('operator_prompt', LANGUAGE))

def main():

    prompt(messages('welcome', LANGUAGE))
    set_language()

    while execution_tracker:
        # Ask the user for the first number.
        prompt(messages('number1', LANGUAGE))
        number1 = input()

        while invalid_number(number1):
            prompt(messages('invalid_number', LANGUAGE))
            number1 = input()
        
        # Ask user for the second number.
        prompt(messages('number2', LANGUAGE))
        number2 = input()

        while invalid_number(number2):
            prompt(messages('invalid_number', LANGUAGE))
            number2 = input()

        operator_prompt() # prints out the operator prompt
        operation = input()

        while operation not in ['1', '2', '3', '4']:
            prompt(messages('invalid_operator', LANGUAGE))
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