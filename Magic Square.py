import math
def formMagicSquare(s):
    total_cost = 0
    # print(total_cost)
    # Find missing values
    # A magic square in a 3x3 arrangement can only contain the following sets
    magic = [[2, 6, 7], [1, 5, 9], [3, 4, 8], [1, 6, 8], [3, 5, 7], [2, 4, 9], [2, 5, 8], [4, 5, 6]]

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
    def calc_difference(x,y):
        # Calculate the absolute value of difference between sorted lists
        total_diff = 0
        for i in range(0, len(x)):
            diff = x[i] - y[i]
            # Get absolute value
            diff = math.sqrt(diff*diff)
            total_diff += diff
        return total_diff

    while len(possibilities)>0:
        ref_map = {}
        cost_map = {}
        match_map = {}
        for combo in possibilities:
            min_diff = 100
            best_match = None
            for x in magic:
                diff = calc_difference(combo, x)
                if diff == 0:
                    min_diff = diff
                    # Remove perfect matches so other combos don't try to match to them
                    possibilities.remove(combo)
                    magic.remove(x)
                    break
                elif diff < min_diff:
                    min_diff = diff
                    best_match = x
            if min_diff >0:
                cost_map[combo] = min_diff
                match_map[combo] = best_match
                print(f"combo: {combo}")
                print(f"match: {best_match}")
                print(f"diff: {min_diff}")
        # At the end of the loop, go through the values and find the smallest change we can make
        min_change = min(cost_map, key=cost_map.get)
        possibilities.remove(min_change)
        magic.remove(match_map[min_change])
        total_cost += cost_map[min_change]
    print(f"total cost:{total_cost}")




    # def missing(s):
    #     vals = []
    #     for i in s:
    #         for j in i:
    #             vals.append(j)
    #     missing = list(set(range(1, 10)) - set(vals))
    #     return missing
    #
    # missing = missing(s)
    # print(missing)
    #
    # # Get the sum of all values
    # def total(s):
    #     total_val = 0
    #     for i in s:
    #         for j in i:
    #             total_val += j
    #     return total_val
    #
    # total_val = total(s)
    # print(total_val)
    # get


s1 = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
s0 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

if __name__ == "__main__":
    formMagicSquare(s0)
    formMagicSquare(s1)
