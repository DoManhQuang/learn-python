
def tohop(start_i, start_j, start_z, arr):
	if start_i ==  len(arr):
		return 0
	if start_j == len(arr):
		start_i +=1
		start_j = start_i + 1
		start_z = start_j + 1
		return tohop(start_i, start_j, start_z, arr)
	if start_z == len(arr):
		start_j += 1
		start_z = start_j + 1
		return tohop(start_i, start_j, start_z, arr)
	print(str(arr[start_i])+""+str(arr[start_j])+str(arr[start_z]))
	start_z +=1
	return tohop(start_i, start_j, start_z, arr)

arr = [1,2,3,4]
start_i = 0
start_j = 1
start_z = 2
tohop(start_i, start_j, start_z, arr)
