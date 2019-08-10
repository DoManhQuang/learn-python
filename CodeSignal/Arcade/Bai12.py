def searchMin(a):
    mi = 0
    for i in range(0,len(a)):
        if a[i] != -1:
            mi = i
            break
    return mi
    pass
def sortByHeight(a):
    print(searchMin(a))
    for i in range(searchMin(a),len(a)-1):
        if a[i] != -1 :
            mi = i
            for j in range(i+1,len(a)):
                if a[j] < a[mi] and a[j] != -1:
                    mi = j
            if mi != i:
                a[i],a[mi] = a[mi],a[i]
                print(a)
    return a
    pass

a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(a)
print(sortByHeight(a))
