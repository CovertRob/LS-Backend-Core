# Builda mortage calculator that determines the monthly payment assuming
# that interest is compounded monthly.

# Inputs:
# 1. Loan amount
# 2. Annual Percentage Rate (APR) - entered as X%
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

