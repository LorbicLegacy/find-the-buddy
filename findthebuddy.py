import requests as web
websitesUserList = ["https://www.facebook.com/","https://www.twitter.com/","https://github.com/","https://www.instagram.com/"]
user = "narendramodi"
for w in websitesUserList:
    r = web.get(w+user)
    print(w," : ","Found" if str(r)== "<Response [200]>" else "Not Found")
