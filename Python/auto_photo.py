import requests

token = "EAAAAUaZA8jlABAGlOkNstZC4FzlESuZBErsL9APg4YmZAvOvGdqZCxMZBq6AnvIEmVXYFb2td6UYDm7opgHdzqDF3llzhH27yqkfIMvdl6ReWWQ49oiXKax9tU3c0NEZAQfsdeYI7owjcLbxmI8YguMhXv4vwbLWvsLjAH9SGjeiVEgzsJuZBaLx"
url = 'https://sites.google.com/site/doctruyentranhconanonlinectp/_/rsrc/1399456474860/truyen-tranh-conan-online-tren-dien-thoai/doc-truyen-tranh-conan-online-tren-dien-thoai-1.jpg'
noidung = { 'url' : url , 'caption': 'hi','access_token' : token}
#id_me = '100027119442350'
a = requests.post('https://graph.facebook.com/v3.0/me/photos',data = noidung)
print (a)