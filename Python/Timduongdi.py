# bài toán kiểm tra đường đến đích
def Kiemtradich(_input):
	if _input == "*":
		return True
	return False

def Luuvitrixuatphat(bando, stack, root):
	start = []
	for i in range(len(bando)):
		for j in range(len(bando[i])):
			if bando[i][j] == 's':
				bando[i][j] = 1
				start.append(i)
				start.append(j)
				stack.append(start)
				root.append(start)
				return True
	return False

def Dungchuongtrinh(stack):
	if len(stack) == 0:
		return True
	return False

def Kiemtraduongdi(_input):
	if _input == 0 or _input == "*":
		return True
	return False

def Ketquatimkiem(bando, stack):
	# index = []
	btree = {}
	# if Luuvitrixuatphat(bando, stack):
	start_i = stack[0][0]
	start_j = stack[0][1]
	# index.append([start_i, start_j])
	# print("stack : ",stack)
	# print("\n",bando)
	while True:

		# khởi tạo xây dựng node trong dict
		namenode = str(start_i) + "," + str(start_j)
		datanode = []

		# kiểm tra đi lên 
		if Kiemtraduongdi(bando[start_i-1][start_j]):
			stack.append([start_i-1, start_j])
			datanode.append([start_i-1, start_j])
			# index.append([start_i-1, start_j])
			# print("\nstack : ",stack)

		# kiểm tra đi xuống
		if Kiemtraduongdi(bando[start_i+1][start_j]):
			stack.append([start_i+1, start_j])
			datanode.append([start_i+1, start_j])
			# index.append([start_i+1, start_j])
			# print("\nstack : ",stack)

		# kiểm tra đi sang trái
		if Kiemtraduongdi(bando[start_i][start_j-1]):
			stack.append([start_i, start_j-1])
			datanode.append([start_i, start_j-1])
			# index.append([start_i, start_j-1])
			# print("\nstack : ",stack)

		# kiểm tra đi sang phải
		if Kiemtraduongdi(bando[start_i][start_j+1]):
			stack.append([start_i, start_j+1])
			datanode.append([start_i, start_j+1])
			# index.append([start_i, start_j+1])
			# print("\nstack : ",stack)

		# cập nhập dữ liệu
		btree.update({ namenode: datanode})

		# di chuyển
		start_new = stack.pop()
		# print("\nstart_new", start_new)
		start_i = start_new[0]
		start_j = start_new[1]

		# kiểm tra đích
		if Kiemtradich(bando[start_i][start_j]):
			print("Tìm thấy đích ở vị trí : bando["+str(start_i)+"]["+str(start_j)+"]")
			return [start_i, start_j], btree

		bando[start_i][start_j] = 1
		# print("\n", bando)

		# kiểm tra dừng chương trình
		if Dungchuongtrinh(stack) == True:
			print("Không tìm thấy đường đi")
			break
		start_new.clear()
		# print("index : ", index)
	pass

def Layvitri(index):
	index = index.split(",")
	return list(map(int, index))

def Timduongdi(index, btree, root, _map):
	node = []
	for x in btree:
		if index in btree[x]:
			# print("btree[x] : ", btree[x])
			node = Layvitri(x)
			# print("node : ", node)
			_map.append(node)
			# print("map : ", _map)
	if node == root[0]:
		return _map
	return Timduongdi(node, btree, root, _map)
	pass

bando1 = [
		[-1,  -1, -1, -1, -1,-1,  -1,-1],
		[-1,   0, -1,  0, -1,-1,   0,-1],
		[-1, 's', -1,  0, -1, 0,  -1,-1],
		[-1,   0,  0,  0,  0, 0, '*',-1],
		[-1,   0, -1, -1,  0,-1,   0,-1],
		[-1,  -1, -1, -1, -1,-1,  -1,-1]
]

bando2 = [
		[-1,  -1, -1, -1, -1,-1,  -1,-1],
		[-1,   0,  0,  0,  0,-1,   0,-1],
		[-1, 's', -1, -1, -1, 0,  -1,-1],
		[-1,   0, -1,  0,  0, 0, '*',-1],
		[-1,   0, -1, -1,  0,-1,   0,-1],
		[-1,  -1, -1, -1, -1,-1,  -1,-1]
]

bando3 = [
		[-1,  -1, -1, -1, -1,-1,  -1,-1],
		[-1,   0,  0,  0,  0, 0,   0,-1],
		[-1, 's', -1, -1, -1, 0,   0,-1],
		[-1,   0, -1,  0,  0, 0, '*',-1],
		[-1,   0, -1, -1,  0,-1,   0,-1],
		[-1,  -1, -1, -1, -1,-1,  -1,-1]
]

stack = []
root = []
_map = []
if Luuvitrixuatphat(bando1, stack, root):
	# print(root)
	index, btree = Ketquatimkiem(bando1, stack)
	_map.append(index)
	# print(index)
	# print(btree)
	_map = Timduongdi(index, btree, root, _map)
	_map.reverse()
	print("Đường đi :",_map)

else:
	print("Không tìm thấy điểm xuất phát")

'''
	dong : i, cot : j
	# up : đi lên	i = i-1
	# down : đi xuống i = i+1
	# left : sang trái j = j-1
	# right : sang phải j = j+1
	stack : mảng 2D lưu vị trí chưa đi.
	hàm kiểm tra vị trí có thể đi
	hàm kiểm tra đích
	hàm kiểm tra kết thúc
	hàm lưu vị trí bắt đầu đi
'''

'''
 Bài toán : kiểm tra xem có tồn tại ít nhất 1 
 đường đi từ 1 điểm bất kỳ trên bản đồ đến điểm đích.
 Quy ước :
 	-1 là vật cản không thể đi.
 	0 là điểm có thể đi vào.
 	2 là điểm bắt đầu
 	3 là điểm đích
 	Chỉ được di chuyển sang trái, phải, lên, xuống 
 	không được phép đi chéo. 
 	input :
 		dòng 1 : số test case
 		dòng 2 : kích thước ma trận
 		dòng 3 : ma trận

 	output:
 		#testcase 1 : true
 		#testcase 2 : false

VD :
	2
	6	8
	-1  -1 -1 -1 -1 -1 -1 -1
	-1   0 -1  0 -1 -1  0 -1
	-1   2 -1  0 -1  0 -1 -1
	-1   0  0  0  0  0  3 -1
	-1   0 -1 -1  0 -1  0 -1
	-1  -1 -1 -1 -1 -1 -1 -1
	6	8
	-1  -1 -1 -1 -1 -1 -1 -1
	-1   0 -1  0 -1 -1  0 -1
	-1   2 -1  0 -1  0 -1 -1
	-1   0  0  0 -1  0  3 -1
	-1   0 -1 -1  0 -1  0 -1
	-1  -1 -1 -1 -1 -1 -1 -1

'''
