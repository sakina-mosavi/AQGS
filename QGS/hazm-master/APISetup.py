import requests
import json

def callApi(url, data, tokenKey):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + tokenKey,
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST", url, data=data.encode("utf-8"), headers=headers)
    return response.text

def tokenkey():
    baseUrl = "http://api.text-mining.ir/api/"
    url = baseUrl + "Token/GetToken"
    querystring = {"apikey":"8beae142-ea1f-ea11-80eb-98ded002619b"}
    response = requests.request("GET", url, params=querystring)
    data = json.loads(response.text)
    tokenKey = data['token']
    return tokenKey

