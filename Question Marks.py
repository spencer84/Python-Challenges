string = "test2???8"

def first():
    q = -1
    l = []
    for i in string:
        q+=1
        if i.isnumeric() == True:
            l.append(q)
    print(l)
    a = l[0]
    b = l[1]
    print(a,b)
    c = int(string[a]) + int(string[b])
    print(c)


first()
for i in string[a,b]

        