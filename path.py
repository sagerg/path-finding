from __future__ import annotations


""" Trivial path finding algorithm using Depth-first Search.
    
Args:
    grid: 2D array depicting a maze.
    start: Starting coordinate.
    end: Target coordinate.

Returns:
    Path of coordinates from start to end in grid.

Raises:
    IndexError: If params have invalid sizes relative to the grid.
"""
def find_path(grid: list[list[int]], start: tuple[int], end: tuple[int]) -> list[tuple[int]]:
    # Validate grid
    if not grid:
        return None

    # Validate start and end
    allowable_max_row_pos = len(grid)
    allowable_max_col_pos = len(grid[0])
    row, col = start
    if row not in range(0, allowable_max_row_pos) or col not in range(0, allowable_max_col_pos):
        raise IndexError("Start coordinate is invalid.")
    row, col = end
    if row not in range(0, allowable_max_row_pos) or col not in range(0, allowable_max_col_pos):
        raise IndexError("End coordinate is invalid")
    
    visited = set()
    has_visited_target = False
    path = []
    

    """ Depth-first Search that adds coordinates to a path array
    """
    def dfs(grid: list, i: int, j: int) -> None:
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
