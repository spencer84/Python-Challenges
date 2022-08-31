def nonDivisibleSubset(k, s):
    subsets = [s]
    def all_non_divisible(arr, k):
        """
        Iterate over a given subset of values and identify if all are non-divisible by a given integer.
        :param arr: Array to iterate over
        :param k: Divisor
        :return: Boolean
        """
        all_non_divisible = True
        for i in range(0, len(arr)-1):
            for j in range(1, len(arr)):
                if (arr[i]+arr[j]) % k == 0:
                    all_non_divisible = False
                    return all_non_divisible
                else:
                    pass
        return all_non_divisible

    running = True
    while running:
        for i in subsets:
            if all_non_divisible(i, k):
                print(len(i))
                running = False
                return len(i)
            else:
                pass
        # If we haven't broken out of the loop, break each subset into smaller subsets
        for i in subsets:
            print(i)
            for j in range(0, len(i)):
                new_arr = i.copy()
                new_arr.remove(new_arr[j])
                new_arr = sorted(new_arr)
                if new_arr not in subsets:
                    subsets.append(new_arr)
        subsets.remove(i)
        print(subsets)


    # def go_deeper(subsets):
    #     for i in subsets:


    # div_dict = {}
    # max_nondivisors = []
    # for i in s:
    #     # Number of pairs that are non-divisible by K
    #     nondivisors = 0
    #     div_dict[i] = []
    #     # Remove the current value and iterate through others
    #     s.remove(i)
    #     for j in s:
    #         if (i + j) % k != 0:
    #             nondivisors += 1
    #             div_dict[i].append(j)
    #     max_nondivisors.append(nondivisors)
    #     s.insert(0, i)
    # max_vals = sorted(list(set(max_nondivisors)), reverse=True)
    # endnotfound = True
    # while endnotfound:
    #     pair_counts = {}
    #     for val in div_dict:
    #         if len(div_dict[val]) >= max_vals[0]:
    #             for i in div_dict[val]:
    #                 if i in pair_counts:
    #                     pair_counts[i] += 1
    #                 else:
    #                     pair_counts[i] = 1
    #     print(len(pair_counts))
    #     print(pair_counts)
    #     if len(pair_counts) >= max_vals[0]:
    #         endnotfound = False
    #         max_vals.remove(max_vals[0])
    #     else:
    #         pass
    #
    # print(len(pair_counts))
    # return len(pair_counts)


s0 = [1, 7, 2, 4]
k0 = 3
s1 = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
k1 = 7
if __name__ == "__main__":
    nonDivisibleSubset(k0, s0)
