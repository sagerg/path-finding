def pathInGrid(grid):
    visited = set()
    reached = False
    path = []
    
    def dfs(grid,i,j):
        nonlocal visited
        nonlocal reached
        nonlocal path
        
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == 1 or (i,j) in visited:
            return
        visited.add((i,j))
        dfs(grid,i+1,j)
        dfs(grid,i-1,j)
        dfs(grid,i,j+1)
        dfs(grid,i,j-1)
        
        if (i,j) == (len(grid)-1,len(grid[0])-1):
            reached = True
        if reached:
            path += [(i,j)]
    
    dfs(grid,0,0)
    return path[::-1]

grid = [[0,1,0,1],
        [0,1,0,1],
        [0,1,0,1],
        [0,0,0,0]]
out = pathInGrid(grid)
print(out)