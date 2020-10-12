import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.put(BASE + "video/1",{"likes":100, 
#                                           "name":"Tom",
#                                           "views": 100000})
# print(response.json())
# input('Press Enter to Continue')

response = requests.get(BASE + "video/6")
print(response.json())

