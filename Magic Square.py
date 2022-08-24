import math
def formMagicSquare(s):
    total_cost = 0
    # print(total_cost)
    # Find missing values
    # A magic square in a 3x3 arrangement can only contain the following sets
    magic = [[8,3,4],]
    magic_copy = magic.copy()
    # Best way is probably to calculate all possible magic squares and compare the minimum absolute difference
    magic_squares = []



    def get_matrix_possibilities(s):
        "Return all possible horizontal, vertical, and diagonal. Sort final arrays before returning/"
        combinations = []
        # Find all rows/cols
        col1 = []
        col2 = []
        col3 = []
        diag1 = []
        diag2 = []
        level1 = 0
        level2 = 2
        for i in s:
            combinations.append(sorted(i))
            col1.append(i[0])
            col2.append(i[1])
            col3.append(i[2])
            diag1.append(i[level1])
            diag2.append(i[level2])
            level1 += 1
            level2 -= 1
        combinations.append(sorted(col1))
        combinations.append(sorted(col2))
        combinations.append(sorted(col3))
        combinations.append(sorted(diag1))
        combinations.append(sorted(diag2))
        return combinations

    possibilities = get_matrix_possibilities(s)
    print(possibilities)
    # def calc_difference(x,y):
    #     # Calculate the absolute value of difference between sorted lists
    #     total_diff = 0
    #     for i in range(0, len(x)):
    #         diff = x[i] - y[i]
    #         # Get absolute value
    #         diff = math.sqrt(diff*diff)
    #         total_diff += diff
    #     return total_diff
    # def adjust_s(s, current, future):
    #     "find the current array in s, then change to the future array"
    #     for i in s:
    #         for j in s:
    #
    #
    # while len(possibilities)>0:
    #     next_moves = []
    #     for combo in possibilities:
    #         min_diff = 100
    #         best_match = None
    #         for x in magic_copy:
    #             diff = calc_difference(combo, x)
    #             if diff == 0:
    #                 min_diff = diff
    #                 # Remove perfect matches so other combos don't try to match to them
    #                 possibilities.remove(combo)
    #                 magic_copy.remove(x)
    #                 break
    #             elif diff < min_diff:
    #                 min_diff = diff
    #                 best_match = x
    #         if min_diff >0:
    #             next_moves.append([min_diff, combo, best_match])
    #             print(f"combo: {combo}")
    #             print(f"match: {best_match}")
    #             print(f"diff: {min_diff}")
    #     # At the end of the loop, go through the values and find the smallest change we can make
    #     # small_move looks like this: [cost, combo, best_match]
    #     small_move = [100]
    #     for move in next_moves:
    #         if move[0] < small_move[0]:
    #             small_move = move
    #
    #     possibilities.remove(small_move[1])
    #     magic_copy.remove(small_move[2])
    #     # Need to update 's' then calculate again
    #
    #     total_cost += small_move[0]
    #     magic_copy = magic.copy()
    #     possibilities = get_matrix_possibilities(s)
    # print(f"total cost:{total_cost}")
    #
    #
    #
    #
    # # def missing(s):
    # #     vals = []
    # #     for i in s:
    # #         for j in i:
    # #             vals.append(j)
    # #     missing = list(set(range(1, 10)) - set(vals))
    # #     return missing
    # #
    # # missing = missing(s)
    # # print(missing)
    # #
    # # # Get the sum of all values
    # # def total(s):
    # #     total_val = 0
    # #     for i in s:
    # #         for j in i:
    # #             total_val += j
    # #     return total_val
    # #
    # # total_val = total(s)
    # # print(total_val)
    # # get


s1 = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
s0 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

if __name__ == "__main__":
    formMagicSquare(s0)
    formMagicSquare(s1)
