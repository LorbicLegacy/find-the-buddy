import requests as web
import json

f = open("websites.json")

webs = json.load(f)
print(webs["social"])
print(len(webs))
websitesList = webs["social"]
user = "narendramodi"
for w in websitesList:
    r = web.get(w + user)
    print(w, " : ", "Found" if str(r) == "<Response [200]>" else "Not Found")
