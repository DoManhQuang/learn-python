import requests
import time
import random

access_token = "EAAAAUaZA8jlABAGEdVNjLcWJLXTi7liu4gKrjYjwtmGC2jKsLAXmAfFQOZCGQVC5N2HgRoJIrCGsWZCoG04wlJyzTP1tRrkQJUO030AY52RZA1swRUDoKCZBbbtdSQerAuZBrGXbZCiOOxMbAeReQjUZA4ZAqOpYESn5ewEToZBJC0SQZDZD"
id_1 = '1663480907113085'
id_2 = '214304085934102'
id_3 = '2001892706499465'
id_4 = '1663480907113085'
Id_Tus = [id_1,id_2,id_3,id_4] 
Cmt = [' Cám Ơn Bạn Rất Nhiều ', 'Xin Lỗi Vì Đã Làm Phiền Bạn ', 'Buổi Tối Tốt Lành', 'Ngày Mới May Mắn' , ' Thank You <3 ']

while True :
	for id in Id_Tus :
		Noidung = random.choice(Cmt)
		url = 'https://graph.facebook.com/'+id+'/comments'
		dulieu = {'access token' : access_token , 'message' : Noidung }
		q = requests.post(url,data = dulieu)
		print (q)
	time.sleep(1800)
	
	