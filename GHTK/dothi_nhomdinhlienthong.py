

def duyetdothi(i, result, arr):
	for j in range(0,len(arr[i])):
		if arr[i][j] == 1 and j not in result:
			result.append(j)
	pass

def xulyphanloaidothi(output, result, arr):
	for i in range(0,len(arr)+1):
		if i == len(arr):
			output.append(result)
		else:
			if i not in result and len(result)>0:
				# print('i1 : ',i)
				copy = result.copy()
				output.append(copy)
				# print('r : ',result)
				# print('o :', output)
				result.clear()
				result.append(i)
				duyetdothi(i, result, arr)
			elif i not in result and len(result)==0:
				# print('i2 : ',i)
				# print('r1 : ',result)
				# print('o1 :', output)
				result.append(i)
				duyetdothi(i, result, arr)
			else:
				# print('i3 : ',i)
				# print('r2 : ',result)
				# print('o2 :', output)
				duyetdothi(i, result, arr)
	pass


createmap = [
				[0,1,0,0,0,0,0],
				[1,0,1,1,0,0,0],
				[0,1,0,1,1,0,0],
				[0,1,1,0,0,0,0],
				[0,0,1,0,0,0,0],
				[0,0,0,0,0,0,1],
				[0,0,0,0,0,1,0],
			]

output = []
result = []
xulyphanloaidothi(output, result, createmap)
print(output)