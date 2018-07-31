import unittest
from pprint import pprint

def find_possibilities(x, y, puzzle):
    possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, 9):
        if 0 not in puzzle[x][i] and puzzle[x][i][0] in possibilities:
            possibilities.remove(puzzle[x][i][0])
        if 0 not in puzzle[i][y] and puzzle[i][y][0] in possibilities:
            possibilities.remove(puzzle[i][y][0])

    # because who doens't like a little bit of code smell
    if x < 3 and y < 3:
        # top left
        for i in range(0, 3):
            for j in range(0, 3):
                if 0 not in puzzle[i][j] and puzzle[i][j][0] in possibilities:
                    possibilities.remove(puzzle[i][j][0])

    if x < 3 and 6 > y > 2:
        # top middle
        for i in range(0, 3):
            for j in range(3, 6):
                if 0 not in puzzle[i][j] and puzzle[i][j][0] in possibilities:
                    possibilities.remove(puzzle[i][j][0])

    if x < 3 and y > 5:
        # top right
        for i in range(0, 3):
            for j in range(6, 9):
                if 0 not in puzzle[i][j] and puzzle[i][j][0] in possibilities:
                    possibilities.remove(puzzle[i][j][0])

    if 2 < x < 6 and y < 2:
        # middle left
        for i in range(3, 6):
            for j in range(0, 3):
                if 0 not in puzzle[i][j] and puzzle[i][j][0] in possibilities:
                    possibilities.remove(puzzle[i][j][0])

    if 2 < x < 6 and 6 > y > 2:
        # middle middle
        for i in range(3, 6):
            for j in range(3, 6):
                if 0 not in puzzle[i][j] and puzzle[i][j][0] in possibilities:
                    possibilities.remove(puzzle[i][j][0])

    if 2 < x < 6 and y > 5:
        # middle right
        for i in range(3, 6):
            for j in range(6, 9):
                if 0 not in puzzle[i][j] and puzzle[i][j][0] in possibilities:
                    possibilities.remove(puzzle[i][j][0])
    
    if x > 5 and y < 2:
        # bottem left
        for i in range(6, 9):
            for j in range(0, 3):
                if 0 not in puzzle[i][j] and puzzle[i][j][0] in possibilities:
                    possibilities.remove(puzzle[i][j][0])

    if x > 5 and 6 > y > 2:
        # bottom middle
        for i in range(6, 9):
            for j in range(3, 6):
                if 0 not in puzzle[i][j] and puzzle[i][j][0] in possibilities:
                    possibilities.remove(puzzle[i][j][0])

    if x > 5 and y > 5:
        # bottom right
        for i in range(6, 9):
            for j in range(6, 9):
                if 0 not in puzzle[i][j] and puzzle[i][j][0] in possibilities:
                    possibilities.remove(puzzle[i][j][0])

    if len(possibilities) == 1:
        puzzle[x][y][0] = possibilities[0]
        return puzzle

def find_all_possibilities(puzzle):
    thereAreZeros = False
    for x in range(0, 9):
        for y in range(0, 9):
            if puzzle[x][y][0] == 0:
                thereAreZeros = True
                find_possibilities(x, y, puzzle)
    if thereAreZeros:
        find_all_possibilities(puzzle)
    else:
        print("Final Solution:")
        print_puzzle(puzzle)
    return puzzle

def print_puzzle(puzzle):
    for x in range(0, 9):
        for y in range(0, 9):
            print(puzzle[x][y], end=" ")
        print()

class TestSolver(unittest.TestCase):

    puzzle = [
        [[3], [8], [0], [2], [0], [9], [0], [0], [1]],
        [[0], [0], [1], [0], [5], [0], [0], [0], [3]],
        [[0], [0], [0], [0], [0], [0], [2], [7], [0]],
        [[0], [0], [0], [6], [0], [0], [3], [0], [0]],
        [[0], [0], [0], [0], [0], [7], [0], [0], [0]],
        [[0], [0], [9], [0], [0], [0], [0], [5], [8]],
        [[0], [0], [0], [0], [0], [1], [9], [0], [0]],
        [[9], [2], [5], [3], [0], [8], [0], [4], [0]],
        [[0], [0], [0], [9], [7], [0], [0], [8], [0]],
    ]
    answer = [
        [[3], [8], [7], [2], [4], [9], [5], [6], [1]],
        [[2], [4], [1], [7], [5], [6], [8], [9], [3]],
        [[5], [9], [6], [8], [1], [3], [2], [7], [4]],
        [[7], [5], [2], [6], [8], [4], [3], [1], [9]],
        [[8], [1], [3], [5], [9], [7], [4], [2], [6]],
        [[4], [6], [9], [1], [3], [2], [7], [5], [8]],
        [[6], [7], [8], [4], [2], [1], [9], [3], [5]],
        [[9], [2], [5], [3], [6], [8], [1], [4], [7]],
        [[1], [3], [4], [9], [7], [5], [6], [8], [2]],
    ]

    missingOne = [
        [[3], [8], [7], [2], [4], [9], [5], [6], [1]],
        [[0], [4], [1], [7], [5], [6], [8], [9], [3]],
        [[5], [9], [6], [8], [1], [3], [2], [7], [4]],
        [[7], [5], [2], [6], [8], [4], [3], [1], [9]],
        [[8], [1], [3], [5], [9], [7], [4], [2], [6]],
        [[4], [6], [9], [1], [3], [2], [7], [5], [8]],
        [[6], [7], [8], [4], [2], [1], [9], [3], [5]],
        [[9], [2], [5], [3], [6], [8], [1], [4], [7]],
        [[1], [3], [4], [9], [7], [5], [6], [8], [2]],
    ]

    def test_canary(self):
        self.assertTrue(True)
    
    def test_fill_element_one_missing(self):
        find_all_possibilities(self.missingOne)
        self.assertEqual(self.missingOne[1][0][0], 2)

    def test_puzzle(self):
        find_all_possibilities(self.puzzle)
        print("----------------")
        pprint(self.puzzle)
        self.assertEqual(self.puzzle, self.answer)

if __name__ == '__main__':
    unittest.main()