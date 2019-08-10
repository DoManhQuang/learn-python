
def created_chess(n):
	Matrix = [[0 for x in range(n)] for y in range(n)]
	return Matrix
	pass

def display_chess(chess):
	print()
	for i in range(0,len(chess)):
		for j in range(0,len(chess[i])):
			print(" ",chess[i][j], end=" ")
		print()
	pass

def isSafe(chess, row, col) : 
      
    for i in range(col):  
        if (board[row][i]):  
            return False
  
    # kiểm tra đường chéo trái trên  
    i = row 
    j = col 
    while i >= 0 and j >= 0: 
        if(board[i][j]): 
            return False; 
        i -= 1
        j -= 1
  
    # kiểm tra đường chéo trái dưới  
    i = row 
    j = col 
    while j >= 0 and i < 4: 
        if(board[i][j]): 
            return False
        i = i + 1
        j = j - 1
  
    return True

def in_arrays(x, y, columns, rows):
	if x in rows or y in columns:
		return True
	return False
	pass

def problem_8queens(columns, chess):
	if columns == len(chess):
		# print("Solution ",solution)
		display_chess(chess)
		print(stackgo)
		return 0
	else:
		for i in range(0, len(chess)):
			if isSafe(chess, i, columns):
				chess[i][columns] = 1
				stackgo.append([i,columns])
				problem_8queens(columns+1, chess)
				chess[i][columns] = 0
				stackgo.pop()
				# solution +=1
	pass


n = 4
chess = created_chess(n)
columns = 0
solution = 1
stackgo = []
problem_8queens(columns, chess)
# print("Sum Solution : ", solution)
# chess[4][4] = 1
# chess[0][0] = 1
# chess[4][0] = 1
# chess[0][4] = 1
# chess[1][2] = 1
# display_chess(chess)
# print(check_diagonal_line(5,5,chess))
# print("\nrows : ", rows)
# print("columns : ",columns)
# print("stackgo : ",stackgo)
# print("queens : ",queens)

