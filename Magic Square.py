import math
import numpy as np
def formMagicSquare(s):
    s = np.array(s)
    total_costs = []
    # A magic square in a 3x3 arrangement can only contain the following sets
    magic = [[8,3,4],[1,5,9],[6,7,2]]
    magic = np.array(magic)
    # Best way is probably to calculate all possible magic squares and compare the minimum absolute difference
    magic_squares = [magic, magic.T]
    def flip(s):
        "Rotate a 3x3 matrix 90 degrees clockwise"
        top_row = [s[0][0],s[0][1],s[0][2]]
        right_col = [s[0][2],s[1][2],s[2][2]]
        bottom_row = [s[2][2], s[2][1], s[2][0]]
        left_col = [s[2][0],s[1][0],s[0][0]]
        # top row becomes the right col
        s[0][2],s[1][2],s[2][2] = top_row[0],top_row[1],top_row[2]
        # right col becomes bottom row
        s[2] = right_col
        s[2][2] = top_row[2]
        # bottom row becomes left col
        s[0][0], s[1][0], s[2][0] = bottom_row[0], bottom_row[1], right_col[2]
        # left col becomes top row
        s[0] = left_col
        return s

    for _ in range(3):
        magic = flip(magic)
        magic_squares.append(magic)
        magic_squares.append(magic.T)

    for square in magic_squares:
        cost = 0
        for i in range(0,3):
            for j in range(0,3):
                cost += abs(s[i][j]-square[i][j])
        total_costs.append(cost)
    print(min(total_costs))
    return min(total_costs)



s1 = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
s0 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

if __name__ == "__main__":
    formMagicSquare(s0)
    formMagicSquare(s1)
