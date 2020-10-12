import requests

BASE = "http://127.0.0.1:5000/"



data =[{"name":"Gnome","views": 1000, "likes": 700},
       {"name":"Dick","views": 9999999, "likes": 9},
       {"name":"Harry","views": 5505, "likes": 788}]

row = 99
for each in data:
    response = requests.put(BASE + "video/" +str(row),each)
    print(row, response.json())
    row +=1



# response = requests.delete(BASE + "video/0")
# print(response)

response = requests.get(BASE + "video/1")
print(response.json())