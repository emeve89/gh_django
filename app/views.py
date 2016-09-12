from django.shortcuts import render, HttpResponse
import requests
import json

def index(request):
    return HttpResponse('Hello World!')

def second(request):
    return HttpResponse('Second view!')

def profile(request):
    jsonList = []
    req = requests.get('https://api.github.com/users/emeve89')
    jsonList.append(json.loads(req.content))
    parsedData = []
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
    parsedData.append(userData)
    return HttpResponse(parsedData)
