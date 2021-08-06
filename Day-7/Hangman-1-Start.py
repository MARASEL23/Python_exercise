import random

word_list = ["adana", "adıyaman", "afyon", "ağrı", "amasya", "ankara",
             "antalya", "artvin", "aydın", "balıkesir", "bilecik",
             "bingöl", "bitlis", "bolu", "burdur", "bursa", "çanakkale",
             "çankırı", "çorum", "denizli", "diyarbakır", "edirne",
             "elazığ", "erzincan", "erzurum", "eskişehir", "gaziantep",
             "giresun", "gümüşhane", "hakkari", "hatay", "Isparta",
             "mersin", "istanbul", "izmir", "kars", "kastamonu",
             "kayseri", "kırklareli", "kırşehir", "kocaeli", "konya",
             "kütahya", "malatya", "manisa", "kahramanmaraş", "mardin",
             "muğla", "muş", "nevşehir", "niğde", "ordu", "rize", "sakarya",
             "samsun", "siirt", "sinop", "sivas", "tekirdağ", "tokat",
             "trabzon", "tunceli", "şanlıurfa", "uşak", "van", "yozgat",
             "zonguldak", "aksaray", "bayburt", "karaman", "kırıkkale",
             "batman", "şırnak", "bartın", "ardahan", "ığdır", "yalova",
             "karabük", "kilis", "osmaniye", "düzce"
             ]
chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong!")