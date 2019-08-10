def checkElements(c):
    for i in range(0,len(c)):
        if c[i] != 0:
            return i
    return -1
def areSimilar(a, b):
    c = []
    if sum(a) != sum(b):
        return False
    else:
        for i in range(0,len(a)):
            c.append(a[i]-b[i])
        if checkElements(c) != -1:
            countSwap = 0
            for i in range(0,len(a)):
                for
        return True

a = [2, 3, 1]
b = [1, 3, 2]
print(areSimilar(a,b))
