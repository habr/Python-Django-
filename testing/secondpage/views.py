import vk
from django.shortcuts import render
from django.http import  HttpResponse

session = vk.Session()
vkapi = vk.API(session)

def index (request, var):
    countries = vkapi.database.getCities(country_id=var,need_all=0,count=1000)
    a = ("")
    for country in countries:
        a += str(str(country['title']) + '<br>')

    return HttpResponse('<html><head><title>Hello VK</title></head><body>' + '<form action="http://127.0.0.1:8000/testingapp/city/sort/' + str(var) + '" method="post"> <input type="submit" name="mysubmit" value="Нажмите для сортировки"></form>' + a + '</body></html>')
