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
    for i in reversed(range(0,len(w_list))):
        word = w_list.copy()
        word[i] = w_list[i-1]
        word[i-1] = w_list[i]
        word = ''.join(word)
        if word > w:
            print(word)
            return
        elif i == 1:
            print('no answer')
            return

biggerIsGreater('ab')
biggerIsGreater('bb')
biggerIsGreater('hefg')
biggerIsGreater('dhck')
biggerIsGreater('dkhc')