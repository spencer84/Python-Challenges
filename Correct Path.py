from random import seed
from random import choice
st = 'drdr??rrddd?'
def CorrectPath(st):
    Directions = ['u','d','l','r']
    seed(1)
    Rlist = []
    def Tabulate(st):
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
    def Random(st):
        Rlist = []
        for j in st:    
            if j == '?':
                Rlist.append('?')
        for i in range(0,len(Rlist)):
            Rlist[i] = choice(Directions)
        return(Rlist)
    def loop(st):
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
    while Tabulate(st_new) != (4,4):
        Random(st)
        loop(st)
        print(st_new)
    print(st)

CorrectPath(st)
        


#st ='?????????'

#Input: "???rrurdr?"
#Output: dddrrurdrd

#Input: "drdr??rrddd?"
#Output: drdruurrdddd


Directions = ['u','d','l','r']
seed(1)
def Tabulate(st):
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


    x = Tabulate(st)[0]
    y = Tabulate(st)[1]   

def Random(st):
    Directions = ['u','d','l','r']
    seed(1)
    Rlist = []
    for j in st:    
        if j == '?':
            Rlist.append('?')
    for i in range(0,len(Rlist)):
        Rlist[i] = choice(Directions)
    return(Rlist)

def Change(st):
    Rlist = Random(st)
    st_list = list(st)
    Qindex = 0
    for num in range(0,len(st)):
        if st_list[num] =='?':
            st_list[num] = Rlist[Qindex]
            Qindex+=1
    st_new = ''.join(st_list)
    return(st_new)
