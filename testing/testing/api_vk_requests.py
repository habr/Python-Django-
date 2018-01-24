import vk
from my_data import MyVkData

session = vk.Session()
vkapi = vk.API(session)

countries=vkapi.database.getCountries(need_all=1)
[print("<li>", country['title'], "</li>") for country in countries]
