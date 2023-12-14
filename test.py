from maze_factory import create_and_export_a_maze
from path import find_path
from colorama import Fore, Back, Style


""" Test path finding algorithm with generated mazes
"""
def test():
    height = 11
    width = 27

    start_pos = (0, 1)
    target = (10, 25)

    print("Fetching 5 mazes from factory...")
    print()

    for i in range(5):
        print("Maze Number", i + 1)

        cw_maze = create_and_export_a_maze()
        path = find_path(cw_maze, start_pos, target, wall='w')

        for i, j in path:
            cw_maze[i][j] = 'o' # 'o' is the path we are taking
        
        print(Fore.WHITE + "Path printed on maze:\n")

        for i in range(0, height):
            for j in range(0, width):
                if (cw_maze[i][j] == 'o'):
                    print(Fore.YELLOW + 'o', end=" ")
                elif (cw_maze[i][j] == 'w'):
                    print(Fore.RED + 'w', end=" ")
                else:
                    print(Fore.GREEN + 'c', end=" ")
            
            print('\n')
            
        print()

        path = []


if __name__ == "__main__":
    test()