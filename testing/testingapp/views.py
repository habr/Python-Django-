import vk
from django.shortcuts import render
from django.http import  HttpResponse
import certifi
import getpass

login = input("Введите логин: ")
passw = getpass.getpass("Введите пароль: ")

session = vk.AuthSession(app_id='4775404', user_login=login, user_password=passw)
vkapi = vk.API(session)
vkapi.users.get(user_ids=1)

countries=vkapi.database.getCountries(need_all=1,count=1000, )
a=("")

for country in countries:
    a += (str('<a'+ ' href="http://127.0.0.1:8000/testingapp/city/'+ str(country['cid']) +'">'+str(country['title'])+'</a><br>'))

def index (request):
    return HttpResponse('<html><head><title>Hello VK</title></head><body>' + a +  '</body></html>')
