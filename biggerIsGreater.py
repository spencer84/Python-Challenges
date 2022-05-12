# From HackerRank:
#
# Lexicographical order is often known as alphabetical order when dealing with strings.
# A string is greater than another string if it comes later in a lexicographically sorted list.
#
# Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
#
#     It must be greater than the original word
#     It must be the smallest word that meets the first condition
#
# Complete the function biggerIsGreater below to create and return the new string meeting the criteria.
# If it is not possible, return no answer.
#
# Function Description
#
# Complete the biggerIsGreater function in the editor below.
#
# biggerIsGreater has the following parameter(s):
#
#     string w: a word
#
# Returns
# - string: the smallest lexicographically higher string possible or no answer

def biggerIsGreater(w):
    w_list = list(w)

w = 'word'
test_arr = []
w_list = list(w)
def permute(arr ,a, l, r):
    if l == r:
        arr.append(a) # Append to a list to get all total permutations
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(arr, a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack
    return arr
perms = permute(test_arr,w_list,0,len(w_list))

    # Need to create a list of all combinations that are greater
    # Then sort through those to find the smallest, that is greater than initial word
    # Need to get more permutations, rather than just swapping with adjacent characters
    greater = None
    print(perms)
    # for perm in perms:
    #     if perm is not None:
    #         if perm > greater:
    #             greater = perm
    # if greater:
    #     print(greater)
    #     return greater
    # else:
    #     print('no answer')
    #     return 'no answer'
    # for i in (range(0,len(w_list))):
    #     count = i + 1
    #     while count < len(w_list):
    #         word = w_list.copy()
    #         word[i] , word[count] = word[count], word[i]
    #         word = ''.join(word)
    #         if word > w:
    #             # Append to the 'greater' list
    #             if greater == None:
    #                 greater = word
    #             elif word < greater:
    #                 greater = word
    #         break
    #         count +=1
    if greater:
        print(greater)
        return greater
    else:
        print('no answer')
        return 'no answer'
    # Implement a bubble sort





biggerIsGreater('ab')
biggerIsGreater('bb')
biggerIsGreater('hefg')
biggerIsGreater('dhck')
biggerIsGreater('dkhc')