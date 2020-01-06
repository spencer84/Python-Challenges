# Have the function ClosestEnemyII(strArr) read the matrix of numbers stored
# in strArr which will be a 2D matrix that contains only the integers 1, 0, or 2. 
# Then from the position in the matrix where a 1 is, return the number of spaces 
# either left, right, down, or up you must move to reach an enemy which is represented
# by a 2. You are able to wrap around one side of the matrix to the other as well.
# For example: if strArr is ["0000", "1000", "0002", "0002"] then this looks like the following:

# 0 0 0 0
# 1 0 0 0
# 0 0 0 2
# 0 0 0 2

# For this input your program should return 2 because the closest enemy (2) is 2 spaces 
# away from the 1 by moving left to wrap to the other side and then moving down once. 
# The array will contain any number of 0's and 2's, but only a single 1. It may not contain
# any 2's at all as well, where in that case your program should return a 0.

strArr = ["0000", "2010", "0000", "2002"] # Initialize the list/matrix
def ClosestEnemyII(strArr):
    one = []
    two = []
    all_twos = []
    def two(strArr): # Identify the number of twos (enemies) in the matrix
        twos = 0
        for i in strArr:
            for j in i:
                if j == '2':
                    twos +=1
        return(twos)
    if two(strArr) == 0:
        print(0)
    else: # Iterate through the array to identify the coordinates of the twos and one. 
        for i in range(0,len(strArr)):
            for j in range(0,len(strArr[i])):
                k = strArr[i]
                l = k[j]
                if l == '1':
                    one = [j,i]
                elif l == '2':
                    two = [j,i]
                    all_twos.append(two)
        if len(all_twos) == 1: # If there is only one enemy, then find the distance from that enemy
            dif_x = two[0] - one[0]
            if dif_x <0:
                dif_x = dif_x*-1
            dif_y = two[1] - one[1]
            if dif_y <0:
                dif_y = dif_y*-1
            dif = dif_x+dif_y
            print(dif)
        else: # Since there is more than one enemy, create an 'options' variable to identify distance between each enemy
            options = []
            for x in all_twos:
                dif_x = x[0] - one[0]
                if dif_x <0:
                    dif_x = dif_x*-1
                dif_y = x[1] - one[1]
                if dif_y <0:
                    dif_y = dif_y*-1
                dif = dif_x+dif_y
                options.append(dif)
            options.sort()
            print(options[0])
ClosestEnemyII(strArr)
