import requests
import time
import random

token = "EAAAAUaZA8jlABAIvOkTOlZALrKXuvIpoyx8Ot2GQyWmzbnHNcdtnwivVu5AG2O0jDfkrQAlq20jKVRO7tF5eJJRp8DJ62fXcNVIBCLVz7T1TOYLnV1zZAm4bzpg4ACl3pcMh7p0r2GzZCrHgjsXE2hmF8aeSYjEZD"
id = '1049738478521138'
a = requests.get('https://graph.facebook.com/v3.2/'+id+'/feed?limit=5&access_token='+token).json()
b = []
for i in a['data'] :
	b.append(i['id'])
	print (i['id'])
	
#while True :
	for i in b :
		url = 'https://graph.facebook.com/'+i+'/likes'
		dulieu = {'access token' : token }
		q = requests.post(url,data = dulieu)
		print (q)
		time.sleep(5)
	#time.sleep(900)