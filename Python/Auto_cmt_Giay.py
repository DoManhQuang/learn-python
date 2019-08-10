import requests
import time 
import random

def Auto_cmt_giay() :
	token_Quangblue = 'EAACmFvGTAKkBAErBR0Cx0ZAZAAiJcYsfhddnyDdkEWZC2BnkyD0IuHkbFNrlZBuzSP0GIKmIZCcfA5k2iQSA8poL6hmwjdMa1290MEq1ACIOJJ7dB8qm6BVRfjihRO0DSELxWapHewD7q4Fv3GPIm15V4To50oopzycKm4epMB65JTokO0XfnkKPvK4tZAp0qGQjW7gMGgpgZDZD'
	Key_cmt = 'Chung'
	id = '1049738478521138'
	a = requests.get('https://graph.facebook.com/v3.2/'+id+'/feed?limit=10&access_token='+token_Quangblue).json()
	b = []
	j = 0
	for i in a['data'] :
		if (i['message'].find(Key_cmt) != -1 ): # Kiểm tra xem message có key_cmt hay không
			j = i # Gán giá trị vị trí của i
			b.append(j['id']) # add ID cần cmt vào mảng B
			print (j['id'])
	'''	
	while True:		
		array = ['Hi','Hello','Hello World']
		for j in b:
			noidung = random.choice (array)
			url = 'https://graph.facebook.com/'+j+'/comments'
			dulieu = {'access token' : token_Quangblue , 'message' :noidung}
			q = requests.post(url,data = dulieu)
			print (q)
		time.sleep(100)
'''
Auto_cmt_giay()

	
	
