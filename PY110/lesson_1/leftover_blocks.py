# Understand Problem
#   Inputs: number of available blocks
#   Outputs: The number of blocks left over 
#   (after building tallest possible valid structure)
#   Explict: 
#       The blocks are cubes - 3D and 6 equilateral sides
#       Built in layers - top layer single block (point)
#       Each upper block requires four lower blocks
#       A lower block can support more than one upper block
#       Cannot leave gaps between blocks
#   Implicit:
#       The supporting blocks will stack their supports - overlapping
#       The progressive layer sizes are square numbers
#          - Direct relationship between layer number and number of blocks
#           along side each side of that layer - squares
#   Questions:
#       How to handle inputs with less than 4 blocks?
#       Do all blocks below a block count as supporting or only the
#           immediate lower row?
#       How are you suppose to stack the blocks? (shape)
#       Is a lower layer valid if it has more blocks than it needs?
#       Will there always be left-over blocks?

# Examples and test cases

# below

# Must have a minimum of 1 block to have a layer
# The layers are all or nothing
# There are not always leftover blocks

# Data Structures
#   For the pyramid building: use a nested list, each sublist a layer
#   Also could use dictionary, each value would hold the number of
#       elements in that layer

# Algorithm

# calculate_leftover_blocks function definition:
    # check if valid number of blocks exists
    # build a valid structure
    # return left-over blocks

# build_structure function definition:
#   initialize variable to the amount of blocks passed in
#   initialize empty list structure to represent pyramid
#   stack blocks starting from the top down
#   stop stacking once valid layer conditions no longer met
#   return structure and leftover blocks


# LS's pseudocode:
# 1. Start with:
#      - The "number of blocks remaining" is equal to the input.
#      - The "current layer number" is layer 0.

# 2. Calculate the "current layer number" for the next layer by
#    adding 1 to the "current layer number".

# 3. Using the new "current layer number", calculate the "number of
#    blocks required in this layer" by multiplying the "current
#    layer number" by itself.

# 4. Determine whether the "number of blocks remaining" is greater
#    than or equal to the "number of blocks required in this layer".
#      - If there are enough blocks:
#          - Subtract the "number of blocks required in this layer"
#            from the "number of blocks remaining".
#          - Go to step 2.
#      - If there aren't enough blocks:
#          - Return the "number of blocks remaining".

# What's different - I tried building the data structure to represent the
# pyramid structure. Seems like I don't really need to do that
#   Need to do a better job of writing pseudocode based off of the rules
#   I generated in the problem description - like the square relationship


# Code

def calculate_leftover_blocks(blocks):
    number_blocks_remaining = blocks
    current_layer = 0
    if number_blocks_remaining == 0:
        return 0
    while True:
        current_layer += 1
        blocks_required = current_layer**2
        if blocks_required <= number_blocks_remaining:
            number_blocks_remaining -= blocks_required
        else:
            return number_blocks_remaining
# or LS's:

def calculate_leftover_blocks(n):
    current_layer = 0
    remaining_blocks = n

    required_blocks = (current_layer + 1) ** 2

    while remaining_blocks >= required_blocks:
        remaining_blocks -= required_blocks
        current_layer += 1
        required_blocks = (current_layer + 1) ** 2

    return remaining_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True