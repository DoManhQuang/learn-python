
def swap(x,y):
  x,y=y,x 
  
def TrangGiay():
	 my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
	 my_dict.sort(key =  my_dict.values())
	 print(my_dict)
TrangGiay()
