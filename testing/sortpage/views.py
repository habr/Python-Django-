import vk
from django.shortcuts import render
from django.http import  HttpResponse
from collections import OrderedDict

session = vk.Session()
vkapi = vk.API(session)

def index (request, var):
    countries = vkapi.database.getCities(country_id=var,need_all=0,count=1000)
    a = ('')
    citysorted=()
    htmlcity=''

    for country in countries:
       a += (country['title'] + '\n')

    citysorted=a.split('\n')
    citysorted.sort()
    htmlcity='<br>'.join(citysorted)

    return HttpResponse('<html><head><title>Hello VK sort</title></head><body>' + htmlcity + '</body></html>')
