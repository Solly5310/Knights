from random import seed, randrange
import sys

knight_count = 0
dim = 10
one_check = False
one_count = 0
grid_counter = 0

def display_grid():
    for row in grid:
        print('    ', ' '.join(str(int(e)) for e in row))

try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        n = 1
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
print()

for x in range(len(grid)):
    for z in range(len(grid)):
        if grid[x][z] == True:
            grid[x][z]=1
            one_count += 1
        elif grid[x][z] == False:
            grid[x][z]=0
if one_count == 0:
    print("No chess knight has explored this board.")
    sys.exit()

def move_index(grid_row,grid_column, grid):
    def move(grid_row,grid_column,grid,row_change,column_change):
        grid_row += row_change
        grid_column +=column_change
        if grid_row > 9 or grid_row<0 or grid_column >9 or grid_column<0:
            return grid
        if grid[grid_column][grid_row] == 1:
            grid[grid_column][grid_row] = 'done'
            return move_index(grid_row,grid_column, grid)
        else:
            return grid
    grid = move(grid_row, grid_column, grid, 1, 2)
    grid = move(grid_row, grid_column, grid, -1, 2)
    grid = move(grid_row, grid_column, grid, 1, -2)
    grid = move(grid_row, grid_column, grid, -1, -2)
    grid = move(grid_row, grid_column, grid, 2, 1)
    grid = move(grid_row, grid_column, grid, -2, 1)
    grid = move(grid_row, grid_column, grid, 2, -1)
    grid = move(grid_row, grid_column, grid, -2, -1)
    return grid
def grid_check(grid):
    for x in grid:
        for y in x:
            if y ==1:
                return False
    return True

#map out the 8 directionsthat a night can go in a recursive manner
#then work out how you could apply that to the next right point in the grid

for x in range(len(grid)):
    grid_column = x
    for z in range(len(grid)):
        grid_row = z
        if grid[grid_column][grid_row] == 1:
            knight_count += 1
            grid[grid_column][grid_row] = 'done'
            grid=move_index(grid_row,grid_column,grid)
        if grid_check(grid) == True:
            print("At least",knight_count,"chess knights have explored this board.")
            sys.exit()