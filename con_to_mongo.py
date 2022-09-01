import requests

url = "https://c00e-202-80-249-156.ap.ngrok.io"


get = requests.get(url)

myobj = {'license_plate': 'test',
         'name': 'test',
         'date': 'test',
         'timein': 'test',
         'timeout': 'test',
         'city': 'test',
         'vehicle1':'test',
         'vehicle2':'test',
         'vehicle3':'test',
         'vehicle4':'test',
         'vehicle5':'test',
         'speed' : 'test',
         'color': 'test'}

post = requests.post(url,myobj)



print(post.json())
print(get.json())