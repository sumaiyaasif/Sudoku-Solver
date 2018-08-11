from pprint import pprint

class Solver():

    def __init__(self): 
        self.state = 0

    def find_possibilities(self, x, y, puzzle):
        possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 9):
            if 0 not in puzzle[x][i] and puzzle[x][i][0] in possibilities:
                possibilities.remove(puzzle[x][i][0])
            if 0 not in puzzle[i][y] and puzzle[i][y][0] in possibilities:
                possibilities.remove(puzzle[i][y][0])

        top_left_x = (x // 3) * 3
        top_left_y = (y // 3) * 3

        for i in range(3):
            for j in range(3):
                if 0 not in puzzle[i+top_left_x][j+ top_left_y] and puzzle[i+top_left_x][j+top_left_y][0] in possibilities:
                    possibilities.remove(puzzle[i+top_left_x][j+top_left_y][0])
                
        if len(possibilities) == 1:
            puzzle[x][y][0] = possibilities[0]
            return puzzle

    def find_all_possibilities(self, puzzle):
        there_are_zeros = False
        for x in range(0, 9):
            for y in range(0, 9):
                if puzzle[x][y][0] == 0:
                    there_are_zeros = True
                    self.find_possibilities(x, y, puzzle)
        if there_are_zeros:
            self.find_all_possibilities(puzzle)
        return puzzle

    def print_puzzle(self, puzzle):
        for x in range(0, 9):
            for y in range(0, 9):print(puzzle[x][y], end=" ")
            print()
