class pointgraph(object):
	def __init__(self, name, x, y, path):
		self.name = name
		self.x = x
		self.y = y
		self.path = path

	def getName(self):
		print(self.name)
		
	def getX(self):
		print(self.x)
		
	def getY(self):
		print(self.Y)
		
	def getPath(self):
		print(self.path)


def created_Matrix(n):
	Matrix = [[0 for x in range(n)] for y in range(n)]
	return Matrix

def process_point(Matrix, index):
	for a in index:
		Matrix[a[0]][a[1]] = 1
		Matrix[a[1]][a[0]] = 1
	return Matrix

def display_Matrix(chess):
	print()
	for i in range(0,len(chess)):
		for j in range(0,len(chess[i])):
			print(" ",chess[i][j], end=" ")
		print()

n = 7
index = [[0,1],[1,2],[1,3],[2,5],[3,4],[4,6],[5,6]]
Matrix = created_Matrix(n)
		




		