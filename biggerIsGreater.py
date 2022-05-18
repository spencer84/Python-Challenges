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
    # Write your code here
    def swap(w, x):
        w_list = list(w)
        # w is the string
        # x is the starting point
        if w_list[x] > w_list[x - 1]:
            w_list[x], w_list[x - 1] = w_list[x - 1], w_list[x]
            w = ''.join(w_list)
            x += 1
            if x > len(w):
                print(w)
                return w
            swap(w, x)
        elif w_list[x] <= w_list[x - 1]:
            x -= 1
            if x < 0:
                print('no answer')
                return 'no answer'
            swap(w, x)
    swap(w,len(w))




biggerIsGreater('ab')
biggerIsGreater('bb')
biggerIsGreater('hefg')
biggerIsGreater('dhck')
biggerIsGreater('dkhc')