def CheckLengthMax(inputArray):
    ma = len(inputArray[0])
    for i in range(0,len(inputArray)):
        if len(inputArray[i]) > ma:
            ma = len(inputArray[i])
    return ma

def addBorder(picture):
    addPic = []
    lenMax = CheckLengthMax(picture)
    print(lenMax)
    x = ""
    for i in range(0,lenMax+2):
        x += "*"
    addPic.append(x)
    for i in range(0,len(picture)):
        picture[i] = "*" + str(picture[i]) + "*"
        addPic.append(picture[i])
    addPic.append(x)
    return addPic

#picture = ["abc","ded"]
picture = ["aa","**", "zz"]
print(CheckLengthMax(picture))
print(addBorder(picture))
