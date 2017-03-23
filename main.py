import sys
import itertools
import time
import numpy as np

domain = [1, 2, 3, 4, 5]

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

def get_input_grid(size):
    grid = [[0 for x in range(size)] for y in range(size)]

    # Print example 
    print "Input example: (for 5x5 grid)"
    print "Row [0]: 02040"
    print "Row [1]: 00010"
    print "etc...\n"

    print "Enter row data: "
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
    
def get_shape_values(grid, shape_coordinates):
    values = []
    for pair in shape_coordinates:
        i = pair[0]
        j = pair[1]
        values.append(grid[i][j])

    return values

################################################################################
# Remnant dec. functions
################################################################################

def find_constraints(grid):
    size = len(grid)
    constrained_grid = [[[] for x in range(size)] for y in range(size)]

    # For each tile 
    for i in range(size):
        for j in range(size):
            # Get tile at pos i,j 
            tile_value = grid[i][j]

            # If empty tile
            if tile_value == 0:
                # Get all values in current row/col of tile
                row_values = get_row_values(grid, i)
                col_values = get_col_values(grid, j)

                # Subtract used values from domain
                used_values = set(row_values).union(set(col_values))
                possible_values = list(set(domain).difference(used_values))

                # Add new constraints for tile
                constrained_grid[i][j] = possible_values

            # Else pre-populated, already constrained 
            else:
                value = [] # derp
                value.append(tile_value)
                constrained_grid[i][j] = value

    return constrained_grid

def calc_candidate_solutions(grid):
    return list(itertools.product(*grid))

def find_solution(candidates, size):
    num_candidates = len(candidates)
    shapes_5x5 = [
        # Center shape (r#,c#) pairs 
        [[1, 2], [2, 1], [2, 2], [2, 3], [3, 2]],
        # Top left
        [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]],
        # Top right
        [[0, 3], [0, 4], [1, 3], [1, 4], [2, 4]],
        # Bottom right 
        [[3, 3], [3, 4], [4, 2], [4, 3], [4, 4]],
        # Bottom left
        [[2, 0], [3, 0], [3, 1], [4, 0], [4, 1]],
    ]

    # For each potential solution 
    for x in range(num_candidates):
        # Convert from 1d array to 2d
        candidate = np.reshape(candidates[x], (-1, size))

        # Assume candidate is valid 
        valid = True

        for i in range(size):
            for j in range(size):
                # Get tile at pos i,j
                tile = candidate[i][j]
                row_values = get_row_values(candidate, i)
                col_values = get_col_values(candidate, j)

                # Remove self from row/col values 
                row_values.pop(j)
                col_values.pop(i)

                # Apply first two rules
                if tile in row_values or tile in col_values:
                    valid = False
                    break
                
                # Apply third rule 
                if size == 5:
                    for shape in shapes_5x5:
                        shape_values = get_shape_values(candidate, shape)
                        diff = set(domain).difference(set(shape_values))

                        # If shape_values were not all unique
                        if len(diff) != 0:
                            valid = False 
                            break

            # Skip solution if invalid 
            if valid is False:
                break
        
        if valid is True:
            return candidate

    return None

################################################################################
# Main
################################################################################

def main():
    grid = [[]]
    constrained_grid = [[[]]]
    permutation = []
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

    # Constrain possible values for each tile in input grid 
    print "\nPossible values for each tile: "
    constrained_grid = find_constraints(grid)
    print_grid(constrained_grid)

    # Flatten 3d array to 2d array to make life easier 
    converted_grid = []
    for i in range(size):
        for j in range(size):
            converted_grid.append(constrained_grid[i][j])

    # Generate all potential solutions from constrained grid
    print "\nCalculating potential solutions..."
    calct0 = time.time()
    permutation = calc_candidate_solutions(converted_grid)
    calct1 = time.time()
    time_elapsed = (calct1 - calct0)
    num_solutions = len(permutation)
    print str(num_solutions) + " solutions generated in " + str(time_elapsed) + " seconds."

    # Find valid solution from all potential solutions 
    print "\nFinding solution..."
    calct0 = time.time()
    solution = find_solution(permutation, size)
    calct1 = time.time()
    time_elapsed = (calct1 - calct0)
    print "Solution found in " + str(time_elapsed) + " seconds."

    print "\nSolution:"
    print solution

# ---------------------------------------------------------------------------- #

if __name__ == "__main__": 
    main()
