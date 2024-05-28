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

#-----------PSEUDOCODE-----------------#

# Function that handles getting the 3 required inputs from the user
# Does value checking

# Function that contains monthly payment formula and returns payment in dollar and cents format

# main function

# name function

# Helper function to keep track of prompt lines.
def prompt(message):

    print(f'==> {message}')

# input() returns string. Using ,'s assigns more than one value. Check for TypeError.
def check_value(value):
    try:
        float(value)
    except TypeError:
        return True
    return False

# Gets from input and returns loan ammmount, APR, and loan duration
def user_inputs():
    global LOAN_AMMOUNT
    global APR
    global LOAN_DURATION
    prompt('Loan Amount (XXXXXX.XX):')
    LOAN_AMMOUNT = input()
    while check_value(LOAN_AMMOUNT):
        prompt('Please enter a correctly formatted loan amount (XXXXXX.XX):')
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

    return LOAN_AMMOUNT, APR, LOAN_DURATION


def initialize():
    prompt('Welcome to loan calculator!')
    prompt('Please enter the following values.')
    user_inputs() # sets globals and returns loan ammount, APR, loan duration

def monthly_payment():
    global LOAN_AMMOUNT
    global LOAN_DURATION
    global APR

    return float(LOAN_AMMOUNT) * ((float(APR) / 12) / (1 - (1 + (float(APR) / 12)) ** (-float(LOAN_DURATION))))

# Execute program.
def main():
    initialize()
    prompt(f'Your monthly payment is ${monthly_payment():.2f}')

# Execution control function.
if __name__ == "__main__":
    main()
