inputArray = [19, 32, 11, 23]
inputArray.sort(reverse=True) # sort max to min
sum = 0
for i in range(0,len(inputArray)-1):
    sum += inputArray[i] - inputArray[i+1]

print (sum)
