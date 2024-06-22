# 1. Create an emtpy 'rows' list to contain the rows
# 2. Create a 'row' list and add it to the overall 'rows' list
# 3. Repeat step 2 until all necesary rows have been created
#   - All rows have been created when length of rows list is equal to input
# 4. Sum the final row
# 5. Return the sum

# Calculating start integer:
# Rule: First integer of row == last integer of preceding row + 2
# Algorithm:
#   - Get the last row of the rows list
#   - Get the last integer of the preceding row
#   - add 2
def sum_even_number_row(row_number):
    rows = []
    start_integer = 2
    for row_length in range(1, row_number + 1):
        row = create_row(start_integer, row_length)
        rows.append(row)
        start_integer = row[-1] + 2 
    return sum(rows[-1])


# 1. Create an empty 'row' list to contain the integers
# 2. Add the starting integer
# 3. Increment the starting integer by 2 to get the next in the sequence
# 4. Repeat steps 2 and 3 until the list has reached the correct length
# 5. Return the row list

# Start the loop
#   Add start_integer to row
#   Increment start_integer by 2
#   Break out of loop if length of row equals row_length

def create_row(start_integer, row_length):
    row = []
    current_integer = start_integer
    while len(row) < row_length:
        row.append(current_integer)
        current_integer += 2
    return row

# Test cases below

# row number: 1 -> sum is 2
# row number: 2 -> sum is 10
# row number: 3 -> sum is 68

print(sum_even_number_row(1) == 2)
print(sum_even_number_row(2) == 10)
print(sum_even_number_row(4) == 68)

# print(create_row(2,1) == [2])
# print(create_row(4, 2) == [4, 6])
# print(create_row(8, 3) == [8, 10, 12])