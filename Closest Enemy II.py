strArr = ["0000", "2010", "0000", "2002"]
def ClosestEnemyII(strArr):
    one = []
    two = []
    all_twos = []
    def two(strArr):
        twos = 0
        for i in strArr:
            for j in i:
                if j == '2':
                    twos +=1
        return(twos)
    if two(strArr) == 0:
        print(0)
    else:
        for i in range(0,len(strArr)):
            for j in range(0,len(strArr[i])):
                k = strArr[i]
                l = k[j]
                if l == '1':
                    one = [j,i]
                elif l == '2':
                    two = [j,i]
                    all_twos.append(two)
        if len(all_twos) == 1:
            dif_x = two[0] - one[0]
            if dif_x <0:
                dif_x = dif_x*-1
            dif_y = two[1] - one[1]
            if dif_y <0:
                dif_y = dif_y*-1
            dif = dif_x+dif_y
            print(dif)
        else: 
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