# Builda mortage calculator that determines the monthly payment assuming
# that interest is compounded monthly.

# Inputs:
# 1. Loan amount
# 2. Annual Percentage Rate (APR) - entered as 0.XX
# 3. Loan duration - entered as X months

# Outputs from Inputs:
# monthly interest rate (APR / 12)
# loan duration in months

# Monthly payment formula: m = p * (j / (1 - (1 + j) ** (-n)))
# m = monthly payment
# p = loan amount
# j = monthly interest rate
# n = loan duration in months

# Edge cases - no interest loans, loans that aren't for an integer number
# of years

# GLOBAL CONSTANTS
LOAN_AMMOUNT = 0.0

APR = 0.0

LOAN_DURATION = 0.0

# Helper function to keep track of prompt lines.
def prompt(message):

    print(f'==> {message}')

# input() returns string. Using ,'s assigns more than one value.
# Check for TypeError and ValueError if empty.
def check_value(value):
    try:
        float(value)
    except TypeError:
        return True
    except ValueError:
        return True
    return False

# Used to check if user wants to do another calculation.
def check_continue(message):

    another_calc = message.lower()
    while another_calc not in ['yes', 'no']:
        prompt('Please enter either yes or no.')
        another_calc = input().lower()
    if another_calc == 'yes':
        return True
    if another_calc == 'no':
        prompt('Exiting calculator.')
        return False

# Gets from input and returns loan ammmount, APR, and loan duration.
# Returns not currently used but for future implementations.
def user_inputs():
    global LOAN_AMMOUNT
    global APR
    global LOAN_DURATION
    prompt('Loan Amount (XXXXXX.XX):')
    LOAN_AMMOUNT = input()
    while check_value(LOAN_AMMOUNT):
        prompt('Please enter a correctly formatted loan amount (XXXXXX.XX):')
        LOAN_AMMOUNT = input()
    while LOAN_AMMOUNT == str(0):
        prompt('Please enter a non-zero loan ammount')
        LOAN_AMMOUNT = input()

    prompt('APR (0.XX):')
    APR = input()
    while check_value(APR):
        prompt('Please enter a correctly formatted APR (0.XX):')
        APR = input()

    prompt('Loan Duration (X.X in months):')
    LOAN_DURATION = input()
    while check_value(LOAN_DURATION):
        prompt('Please enter a corrected formatted loan duration (X.X in months):')
        LOAN_DURATION = input()
    while LOAN_DURATION == str(0):
        prompt('Please enter a non-zero loan duration')
        LOAN_DURATION = input()

    return LOAN_AMMOUNT, APR, LOAN_DURATION

# Used to set up program with beginning user inputs.
def initialize():
    prompt('Please enter the following values.')
    user_inputs() # sets globals and returns loan ammount, APR, loan duration

# Calculates the monthly loan payment.
def monthly_payment():
    if APR != '0':
        return float(LOAN_AMMOUNT) * ((float(APR) / 12) / (1 - (1 + (float(APR) / 12)) ** (-float(LOAN_DURATION))))
    return float(LOAN_AMMOUNT) / float(LOAN_DURATION)

# Execute program.
def main():
    prompt('Welcome to loan calculator!')
    while True:
        initialize()
        prompt(f'Your monthly payment is ${monthly_payment():.2f}')
        prompt('Would you like to perform another calculation? Please enter yes or no.')
        if check_continue(input()) is True:
            prompt('Continuing with next calculation')
        else:
            break

# Execution control function.
if __name__ == "__main__":
    main()
