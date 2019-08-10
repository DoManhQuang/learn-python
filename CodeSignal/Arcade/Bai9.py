


def CheckLengthMax(inputArray):
    ma = len(inputArray[0])
    for i in range(0,len(inputArray)):
        if len(inputArray[i]) > ma:
            ma = len(inputArray[i])
    return ma

def allLongArrays(inputArray):
    longArray = []
    maxlen = CheckLengthMax(inputArray)
    for i in range(0,len(inputArray)):
        if len(inputArray[i]) == maxlen:
            longArray.append(inputArray[i])
            print(inputArray[i])
    return longArray




