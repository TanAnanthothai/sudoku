# '''
# Exercise2.1: Improved grid_values()

# As of now, we are recording the puzzles in dictionary form, where the keys are the boxes ('A1', 'A2', ... , 'I9') 
# and the values are either the value for each box (if a value exists) or '.' (if the box has no value assigned yet). 
# What we really want is for each value to represent all the available values for that box. 
# For example, the box in the second row and fifth column above will have key 'B5' and value '47' 
# (because 4 and 7 are the only possible values for it). The starting value for every empty box will thus be '123456789'.
# Update the grid_values() function to return '123456789' instead of '.' for empty boxes.

# >>> from utils import display
# >>> display(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))
# 123456789 123456789     3     |123456789     2     123456789 |    6     123456789 123456789 
#     9     123456789 123456789 |    3     123456789     5     |123456789 123456789     1     
# 123456789 123456789     1     |    8     123456789     6     |    4     123456789 123456789 
# ------------------------------+------------------------------+------------------------------
# 123456789 123456789     8     |    1     123456789     2     |    9     123456789 123456789 
#     7     123456789 123456789 |123456789 123456789 123456789 |123456789 123456789     8     
# 123456789 123456789     6     |    7     123456789     8     |    2     123456789 123456789 
# ------------------------------+------------------------------+------------------------------
# 123456789 123456789     2     |    6     123456789     9     |    5     123456789 123456789 
#     8     123456789 123456789 |    2     123456789     3     |123456789 123456789     9     
# 123456789 123456789     5     |123456789     1     123456789 |    3     123456789 123456789 
# '''

#1. utils.py ----------------------------
#1.1 define rows: 
rows = 'ABCDEFGHI'

#1.2 define cols:
cols = '123456789'

#1.3 cross(a,b) helper function to create boxes, row_units, column_units, square_units, unitlist
def cross(a, b):
    return [s+t for s in a for t in b]

#1.4 create boxes
boxes = cross(rows, cols)

#1.5 create row_units
row_units = [cross(r, cols) for r in rows]

#1.6 create column_units
column_units = [cross(rows, c) for c in cols]

#1.7 create square_units for 9x9 squares
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

#1.8 create unitlist for all units
unitlist = row_units + column_units + square_units

#1.9 create peers of a unit from all units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

#1.10 display function receiving "values" as a dictionary and display a 9x9 suduku board
def display(values):
    # """
    # Display the values as a 2-D grid.
    # Input: The sudoku in dictionary form
    # Output: None
    # """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return
    
#2. function.py ----------------------------
# '''
# Instruction : Update the grid_values() function to return '123456789' instead of '.' for empty boxes.
# '''
# 2.1 improve grid_values(grid)
# from utils import *
def grid_values(grid):
    # """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    # Args:
    #     grid: Sudoku grid in string form, 81 characters long
    # Returns:
    #     Sudoku grid in dictionary form:
    #     - keys: Box labels, e.g. 'A1'
    #     - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    # """
    grid_list = list(grid)
    for index, g in enumerate(grid_list):
        if grid_list[index]=='.':
            grid_list[index] = "123456789" 
    dictionary_grid = dict(zip(boxes, grid_list))
    return dictionary_grid
#3. Test function.py ----------------------------  
display(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))