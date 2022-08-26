def formMagicSquare(s):
    total_costs = []
    # A magic square in a 3x3 arrangement can only contain the following sets
    magic = [[8,3,4],[1,5,9],[6,7,2]]
    # Best way is probably to calculate all possible magic squares and compare the minimum absolute difference
    magic_squares = [[[8,3,4],[1,5,9],[6,7,2]]]
    def flip(x):
        s = list(x)
        "Rotate a 3x3 matrix 90 degrees clockwise"
        top_row = [s[0][0],s[0][1],s[0][2]]
        right_col = [s[0][2],s[1][2],s[2][2]]
        bottom_row = [s[2][0], s[2][1], s[2][2]]
        left_col = [s[2][0],s[1][0],s[0][0]]
        # top row becomes the right col
        s[0][2],s[1][2],s[2][2] = top_row[0],top_row[1],top_row[2]
        # right col becomes bottom row
        s[2] = right_col
        s[2][2] = top_row[2]
        # bottom row becomes left col
        s[0][0], s[1][0], s[2][0] = bottom_row[0], bottom_row[1], bottom_row[2]
        # left col becomes top row
        s[0] = left_col
        return s
    def transpose(s):
        x = list(s)
        x[0][1], x[1][0] = s[1][0], s[0][1]
        x[1][2], x[2][1] = s[2][1], s[1][2]
        x[0][2], x[2][0] = s[2][0], s[0][2]
        return x
    print(magic_squares)
    for _ in range(3):
        magic = flip(magic)
        magic_squares.append(magic.copy())
        print(magic_squares)
    print(magic_squares)

    transposed = []
    for square in magic_squares:
        #print(square)
        magic_transposed = transpose(square)
        transposed.append(list(magic_transposed))
    # for x in transposed:
    #     print(x)
    magic_squares = magic_squares + transposed
    for square in magic_squares:
        #print(square)
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
