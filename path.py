def find_path(grid: list[list], start: tuple, end: tuple) -> list:
    visited = set()
    has_visited_target = False
    path = []
    
    def dfs(grid, i, j):
        nonlocal visited, has_visited_target, path
        
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 1 or (i, j) in visited:
            return None
        
        else:
            visited.add((i,j))
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
            
            if (i,j) == end:
                has_visited_target = True

            if has_visited_target:
                path += [(i,j)]
    
    row, col = start
    dfs(grid, row, col)

    return path[::-1]


##############################
#          TESTING           #
##############################

grid = [
    [0,1,0,1],
    [0,1,0,1],
    [0,1,0,1],
    [0,0,0,0],
    [0,1,0,1],
    [0,1,0,1],
    [0,1,0,1],
    [0,0,0,0],
    [0,1,0,1],
    [0,1,0,1],
    [0,1,0,1],
    [0,0,0,0],
]

##############################
#           PARAMS           #
##############################

start = (0, 0)
end = (len(grid) - 1,len(grid[0]) - 1)

path = find_path(grid, start, end)
print("path to take:", path)
print("illustrated with grid")
for i, j in path:
    grid[i][j] = 2

# Print grid with format

for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end=', ')
    print()
print()
        