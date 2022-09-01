def nonDivisibleSubset(k, s):
    worst_fit = 0
    for i in s:
        s_copy = s.copy()
        count = 0
        for j in s_copy.remove(i):
            if (i + j) % k == 0:
                count += 1
        if count > worst_fit:
            worst_fit = count
    if worst_fit == 0:
        return len(s)
    else:
        nonDivisibleSubset(k,s.rem)

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
    nonDivisibleSubset(k1, s1)
