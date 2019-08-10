def alphabeticShift(inputString):
    asciis = []
    for i in inputString:
        if i == 'z':
            asciis.append(ord('a'))
        else:
            asciis.append(ord(i)+1)
    outStr = ''.join(chr(i) for i in asciis)
    return outStr


print(alphabeticShift("crazy"))
    
        
