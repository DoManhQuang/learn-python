def arrayChange(a):
    increasing = 0
    for i in range(1,len(a)):
        if a[i] <= a[i-1]:
            a[i] += a[i-1]
            print(a[i-1])
            print(a[i])
            increasing += a[i-1]
            print(increasing)
    return increasing

a = [-1000, 0, -2, 0]
print(arrayChange(a))
