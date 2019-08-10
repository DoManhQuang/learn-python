import requests
import time
import random

token = 'EAAEAnbAtedgBAJ8rl0lqDezQLHqEc4ImFASsBjgM3fgQyT2y76kqB5QcuUK3QjhwkMhVugjY4zRgRp8N3b32iZCBL9tLwVZBjlnZCqNVDT2hVQDJxkqXZBP5ee1RDOZAS90jnjHk0ihgbyswsJijKHqBoIUXBqBUdAsRnZAbRZAphu8DiZBz6AFjO6tfBU53EXi7idARBchZBGQZDZD'
id = '1049738478521138'
a = requests.get('https://graph.facebook.com/v3.2/'+id+'/feed?limit=5&access_token='+token).json()
b = []
for i in a['data'] :
	b.append(i['id'])
	print (i['id'])

array = ['<3','Haha','World Cup 2018']

for i in b:
	noidung = random.choice (array)
	url = 'https://graph.facebook.com/'+i+'/comments'
	dulieu = {'access token' : token , 'message' :noidung}
	q = requests.post(url,data = dulieu)
	print (q)
	time.sleep(5)
	