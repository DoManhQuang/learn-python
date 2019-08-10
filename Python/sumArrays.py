a = [2,3,5,5,10,14]
sum = 0
for i in range(0,len(a)-1):
    print(a[i])
    print(a[i+1])
    sum += a[i+1] - a[i]
    print(sum)
    i += 2
print(sum)
