import sys
import numpy as np

################################################################################
# Input functions
################################################################################

# Ensure that each char for a row is between 0 and 5 inclusive
def validate_input(userstr, size):
    if len(userstr) is not size:
        print "Length of \"" + userstr + "\" is not " + str(size)
        return False

    for char in userstr:
        try:
            num = int(char)
        except ValueError:
            print char + " is not a valid integer."
            return False

        if num < 0 or num > 5:
            print char + " is not a number between 0 and 5 inclusive."
            return False
    
    return True

################################################################################
# Grid functions
################################################################################

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            sys.stdout.write(str(grid[i][j]) + " ")
        sys.stdout.write('\n')

def print_grid_3d(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            values = grid[i][j]
            for m in range(len(values)):
                sys.stdout.write(str(values[m]) + '   ')
        sys.stdout.write('\n')

def get_input_grid(size):
    grid = [[0 for x in range(size)] for y in range(size)]

    # Print example 
    print "Input example: "
    print "Row [0]: 02340"
    print "Row [1]: 00010"
    print "etc...\n"

    print "Enter each row value: "
    # For each row, get row from user
    for i in range(size):
        input_row = raw_input("Row [" + str(i + 1) + "]: ")
        
        # Ensure row is valid (no invalid chars)
        if validate_input(input_row, size) is False:
            sys.exit(1)

        # Push value of each column from input string to grid  
        for j in range(size):
            grid[i][j] = int(input_row[j])

    return grid

def get_row_values(grid, i):
    size = len(grid)
    row_values = []

    for x in range(size):
        tile = grid[i][x]
        if tile != 0:
            row_values.append(tile)

    return row_values 

def get_col_values(grid, j):
    size = len(grid)
    col_values = []

    for x in range(size):
        tile = grid[x][j]
        if tile != 0:
            col_values.append(tile)

    return col_values
    
################################################################################
# Remnant dec. functions
################################################################################

def find_constraints(grid):
    size = len(grid)
    domain = [1, 2, 3, 4, 5]
    constrained_grid = [[[] for x in range(size)] for y in range(size)]

    # For each tile 
    for i in range(size):
        for j in range(size):
            # Get tile value 
            tile_value = grid[i][j]

            # If empty tile
            if tile_value == 0:
                # Find possible values when considering current row and column
                row_values = get_row_values(grid, i)
                col_values = get_col_values(grid, j)

                used_values = set(row_values).union(set(col_values))
                possible_values = set(domain).difference(used_values)

                constrained_grid[i][j].append(list(possible_values))
            # Else pre-populated, already constrained 
            else:
                #constrained_grid[i][j].append(tile_value)
                value = []
                value.append(tile_value)

                constrained_grid[i][j].append(value)

    return constrained_grid

def convert_constrained(grid):
    converted = [[]]

    size = len(grid)
    for i in range(size):
        for j in range(size):
            print "test"

def get_possible_solutions(grid):
    size = len(grid)
    for i in range(size):
        for j in range(size):
            print "test"

################################################################################
# Main
################################################################################

def main():
    grid = [[]]
    constrained_grid = [[]]
    permutations = []
    size = 0

    # Check arg length
    if len(sys.argv) != 2:
        print "Usage: python main.py <grid width>"
        sys.exit(1)

    # Get and validate grid size 
    try:
        size = int(sys.argv[1])
    except ValueError:
        print size + " is not a valid integer."
        sys.exit(1)

    # Get input grid from stdin
    grid = get_input_grid(size)

    # Display input grid 
    print "\nInput grid: "
    print_grid(grid)

    # --- Shits about to get real 

    # Constrain possible values for each tile in input grid 
    print "\nPossible values for each tile: "
    constrained_grid = find_constraints(grid)
    print_grid_3d(constrained_grid)

    # TODO dont be stupid 
    # Convert 3d array to 2d array 
    constrained_grid = convert_constrained(constrained_grid)

    # Generate permutations of constrained input grid 
    #permutations = get_possible_solutions(constrained_grid)

# ---------------------------------------------------------------------------- #

if __name__ == "__main__": 
    main()
