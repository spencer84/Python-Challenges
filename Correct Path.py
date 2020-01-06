# Have the function CorrectPath(str) read the str parameter being passed, which will represent
# the movements made in a 5x5 grid of cells starting from the top left position.
# The characters in the input string will be entirely composed of: r, l, u, d, ?. 
# Each of the characters stand for the direction to take within the grid, for example:
# r = right, l = left, u = up, d = down. Your goal is to determine what characters the question
# marks should be in order for a path to be created to go from the top left of the grid all the 
# way to the bottom right without touching previously travelled on cells in the grid.

# For example: if str is "r?d?drdd" then your program should output the final correct
# string that will allow a path to be formed from the top left of a 5x5 grid to the bottom right. 
# For this input, your program should therefore return the string rrdrdrdd. 
# There will only ever be one correct path and there will always be at least one question mark within the input string.

from random import seed
from random import choice
st = 'drdr??rrddd?'
def CorrectPath(st):
    Directions = ['u','d','l','r']
    seed(10)
    def Tabulate(st): #Tabulates the coordinates of each character to determine end location of string
        Rlist = []
        x = 0
        y = 0
        for i in st:
            if 'r' in i:
                y+=1
            if 'l' in i:
                y-=1
            if 'd' in i:
                x+=1
            if 'u' in i:
                x-=1
        return(x,y)
    Tabulate(st)
    x = Tabulate(st)[0]
    y = Tabulate(st)[1]
    def Random(st): # create a list of random directions
        Rlist = []
        for j in st:    
            if j == '?':
                Rlist.append('?')
        for i in range(0,len(Rlist)):
            Rlist[i] = choice(Directions)
        return(Rlist)
    def loop(st): # iterate through the string to replace question marks with a random direction
        Rlist = Random(st)
        st_list = list(st)
        Qindex = 0
        for num in range(0,len(st)):
            if st_list[num] =='?':
                st_list[num] = Rlist[Qindex]
                Qindex+=1
        st_new = ''.join(st_list)
        return(st_new)
    st_new = loop(st)
    while Tabulate(st_new) != (4,4): # Until all directions add up to the final coordinates, keep trying random combinations
        Rlist = Random(st)
        st_new = loop(st)
        Random(st)
        loop(st)
        print(st_new, Tabulate(st_new))
    print(st)
    return(st_new)
CorrectPath(st)


