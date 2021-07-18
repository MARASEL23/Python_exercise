"""
import random


import my_module

random_int = random.randint(1, 10)
print(random_int)

random_float = random.random()
print(random_float)
print(my_module.pi)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}!")
"""
city_of_turkey = ["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya",
                   "Ankara", "Antalya", "Ardahan", "Artvin", "Aydın", "Balıkesir",
                   "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis",
                   "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum",
                   "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan",
                   "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane",
                   "Hakkâri", "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir",
                   "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu",
                   "Kayseri", "Kilis", "Kırıkkale", "Kırklareli", "Kırşehir",
                   "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin",
                   "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu",
                   "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa",
                   "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat",
                   "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat",
                   "Zonguldak"]

city_of_turkey[2] = "Afyon"

city_of_turkey.append("Marasel")

print(city_of_turkey)
