from path import find_path


def main():
    ##############################
    #          TESTING           #
    ##############################

    grid = [
        [0,1,0,1,0],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [0,0,0,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0],
        [0,1,0,0,0],
        [0,1,0,1,1],
        [0,1,0,1,0],
        [0,1,0,0,0],
        [0,1,0,1,0],
        [0,0,1,1,0],
    ]

    ##############################
    #           PARAMS           #
    ##############################

    start = (0, 0)
    end = (len(grid) - 1,len(grid[0]) - 1)

    ### Execute DFS
    path = find_path(grid, start, end)
    
    ### Original Grid
    print("Original Grid")
    if path != []:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(grid[i][j], end=' ')
            print()
        print()
    
    ### Fill in Grid if there is a Path
    for i, j in path:
        grid[i][j] = 2

    print("Steps taken from start to end:", len(path))
    print()
    print("Path to take:", path)
    print()
    print("Illustrated Path with Grid (where '2' is the path taken)")

    if path != []:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    print(grid[i][j], end=' ')
                else:
                    print(' ', end=' ')
            print()
        print()


if __name__ == "__main__":
    main()