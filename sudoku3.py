# '''
# Exercise3.1: implement only_choice()
# Time to code it! In the next quiz, finish the code for the function only_choice, 
# which will take as input a puzzle in dictionary form. The function will go through all the units, 
# and if there is a unit with a digit that only fits in one possible box, it will assign that digit to that box.
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

def eliminate(values):
    # """Eliminate values from peers of each box with a single value.

    # Go through all the boxes, and whenever there is a box with a single value,
    # eliminate this value from the set of values of all its peers.

    # Args:
    #     values: Sudoku in dictionary form.
    # Returns:
    #     Resulting Sudoku in dictionary form after eliminating values.
    # """

    for key in values:
        if len(values[key])==1:
            for item in peers[key]:
                values[item] = values[item].replace(values[key],"")
    return values

#2. function.py ----------------------------
# 2.1 implement only_choice(values)
# from utils import *
def only_choice(values):
    # """Finalize all values that are the only choice for a unit.

    # Go through all the units, and whenever there is a unit with a value
    # that only fits in one box, assign the value to this box.

    # Input: Sudoku in dictionary form.
    # Output: Resulting Sudoku in dictionary form after filling in only choices.
    # """
    # for key in values:
    #     for unit in units[key]:
    #         for item_one in unit:
    #             if key != item_one:
    #                 if values[key] not in values[item_one]:
    #                     values[key] = values[item_one]
    # return values
    dict_square_units = dict((s, [u for u in square_units if s in u]) for s in boxes)
    for key in values:
        for dict_square_unit in dict_square_units[key]:
            for dict_square_unit_one in dict_square_unit:
                if key != dict_square_unit_one:
                    if values[key] not in values[dict_square_unit_one]:
                        values[key] = values[dict_square_unit_one]
    return values
 
   
  

#3. Test utils.py ----------------------------  
values = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
print("The original Sudoku board is **********************************************")
display(values)
eliminate(values)
print("\n")
print("After implement eliminate(values) method **********************************")
display(values)
# print(dict_square_units)
#4. Test function.py ----------------------------  
new_values = only_choice(values)
print("\n")
print("After implement only_choice(values) method **********************************")
display(new_values)