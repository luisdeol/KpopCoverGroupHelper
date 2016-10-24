from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
from pymongo import MongoClient
from datetime import datetime
import pymongo

# Create your views here.
client = MongoClient()
db = client.test
kpopgroups = db.kpopgroups
headers_c = db.kpopgroups_headers

def index(request):
    return render_to_response('index.html',{})

def search(request):
    headers = ["Groups", "Has changed"]
    keyword = request.GET.get('search_query', '')
    if int(keyword) == 1:
        groupsFound = list(kpopgroups.find({'Membros': 1}, {"Membros": 0 }).sort("Grupo", pymongo.ASCENDING))
    else:
        groupsFound = list(kpopgroups.find({'Membros_originais': int(keyword)}, {"Membros": 0 }).sort("Grupo", pymongo.ASCENDING))
    for a in groupsFound:
        a["Grupo"] = a["Grupo"].replace("_", " ").replace("%27", "'")
    return render_to_response('search.html',{
            'headers_list':headers,
            'year':datetime.now().year,
            'list':groupsFound
    })