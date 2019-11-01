stArr = [[5, 9], [1, 2, 6, 7]] 
def Scalebalancing(stArr):
    scale = stArr[0]
    weights = stArr[1]
    scale = sorted(scale)
    l = scale[0]
    r = scale[1]
    Balanced = 'Scale is balanced'
    if l != r:
        for i in weights:
            if l + i == r:
                print(Balanced)
                return(i)
            for j in weights:
                if l + i == r + j:
                    print(Balanced)
                    return(i,j)
Scalebalancing(stArr)

