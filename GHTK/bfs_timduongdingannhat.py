def output(maparr):
	for i in range(0,len(maparr)):
		for j in range(0,len(maparr[i])):
			print(" ",maparr[i][j])
		print("\n")

def duyetdinhdothi(i, start, theend, arr):
	flag = 0
	for j in range(0,len(arr[i])):
		# print(" ",arr[i][j])
		# print('start : ',start)
		if arr[i][j] == 1 and j == theend:
			result.insert(0,j)
			return -2
		if arr[i][j] == 1 and j != start and j not in stack and j != theend:
			queue.insert(0,j)
			stack.insert(0,j)
			flag = 1
			# print('queue2 : ',queue)
			# print('stack2 : ',stack)
	return flag
	pass

def xulyduyetdinh(start, theend,  arr):
	for i in range(start, len(arr)):
		# print('i : ',i)
		end = duyetdinhdothi(i, start, theend, arr)
		# print('end : ',end)
		if end == -2:
			print('Tim thay duong di')
			print('result : ',result)
			return 0
		if end == 0 and len(queue) == 0:
			print('Khong tin thay duong di')
			return 0
		if end == 1 or end == 0 and len(queue) != 0:
			start_new = queue.pop(0)
			result.insert(0,start_new)
			# print('result : ',result)
			if start_new == theend:
				print('Tim thay duong di')
				# print('queue4 : ',queue)
				# print('stack4 : ',stack)
				return 0
			else:
				return xulyduyetdinh(start_new, theend, arr)
	pass
		


createmap = [
				[0,1,0,0,0],
				[1,0,1,1,0],
				[0,1,0,1,1],
				[0,1,1,0,0],
				[0,0,1,0,0]
			]

createmap1 = [
				[0,1,0,0,0,0],
				[1,0,1,1,0,0],
				[0,1,0,1,1,0],
				[0,1,1,0,0,0],
				[0,0,1,0,0,0],
				[0,0,0,0,0,0]
			]
queue = []
stack = []
result = []
start = 1
theend = 4
stack.append(start)
xulyduyetdinh(start, theend, createmap)
# print('queue : ',queue)
# print('stack : ',stack)


# def createdmap(col, row):
# 	maparr = []
# 	for i in range(0,col):
# 		for j in range(0,row):
# 			maparr[i][j] = 0
# 	return maparr

# def input(arr):
# 	for x, y in arr:
# 		arr[x-1][y-1] = 1
# 		arr[y-1][x-1] = 1

# col = 4
# row = 4

# arr = [[1,2],[2,3],[3,4],[2,4]]
# createmap = createdmap(col, row)
# input(createmap)
# print(createmap)

