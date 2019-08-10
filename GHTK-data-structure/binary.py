def binarys(number, strbi):
	if number == 0:
		return "00" + strbi
	if number == 1:
		return "01" + strbi
	strbi = str(int(number%2)) + strbi
	number = int(number/2)
	return binarys(number, strbi)


def display_binarys(maxlength, start, binaryArrays):
	binary = binarys(start, "")
	# minlength = len(binary)
	if len(binary) > maxlength:
		return 0
	# print(binary)
	binaryArrays.append(binary)
	start += 1
	return display_binarys(maxlength, start, binaryArrays)

# binaryArrays = []
# display_binarys(3, 0, binaryArrays)
# x = binarys(1000,"")
# binaryArrays.append(x)
# print(x)

def backtracking(k, a, n):
	if  k == n:
		print(a)
	for i in range(0,2):
		a.append(i)
		backtracking(k+1)

a = []
n = 3
backtracking(0,a,n)







