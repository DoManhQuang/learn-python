import requests 

token = 'EAACmFvGTAKkBAO7xRMKfzArshY68Jghzjfw1wU4K6ayyTgIwnGWZA8Loo1GA74ZBHJRpYg0cp6tnexr9UX8D5o9W9JApOf1a57EM8deikRI89aTzrfMOqZCkilpnnDZCJgTl09tzCUC8JMy45md9e6s6fIGRbBvkZBiuUmxM2gYVUDJZAH8DHyZBE5NV63c23sZD'
noidung = {'message': 'Hello World', 'access_token': token }
a = requests.post('https://graph.facebook.com/v3.2/171219290458718/feed', data=noidung)
print(a)
