from __future__ import annotations


""" Trivial path finding algorithm using Depth-first Search.
    
Args:
    grid: 2D array depicting a maze.
    start: Starting coordinate.
    end: Target coordinate.
    wall: Walls to avoid.

Returns:
    Path of coordinates from start to end in grid.

Raises:
    IndexError: If params have invalid sizes relative to the grid.
"""
def find_path(grid: list[list[int]], start: tuple[int], end: tuple[int], wall = 1) -> list[tuple[int]]:
    
    ##############################
    #         CHECK GRID         #
    ##############################

    if not grid:
        return None

    ##############################
    #     CHECK START AND END    #
    ##############################

    allowable_max_row_pos = len(grid)
    allowable_max_col_pos = len(grid[0])
    row, col = start
    if row not in range(0, allowable_max_row_pos) or col not in range(0, allowable_max_col_pos):
        raise IndexError("Start coordinate is invalid.")
    row, col = end
    if row not in range(0, allowable_max_row_pos) or col not in range(0, allowable_max_col_pos):
        raise IndexError("End coordinate is invalid")

    visited = set()
    path = []


    """ Depth-first Search that adds coordinates to a path array
        By default it assumes that we have a grid of integers and '1' is the obstacle to avoid
    """
    def dfs(grid: list, i: int, j: int, wall) -> bool:
        nonlocal visited, path
        
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == wall or (i, j) in visited:
            return False
        
        else:
            visited.add((i,j))
            
            if dfs(grid, i+1, j, wall) or dfs(grid, i-1, j, wall) or dfs(grid, i, j+1, wall) or dfs(grid, i, j-1, wall):
                path += [(i,j)]
                return True
            
            if (i,j) == end:
                path += [(i,j)]
                return True
            
            else:
                return False

    
    row, col = start
    dfs(grid, row, col, wall)

    return path[::-1]
