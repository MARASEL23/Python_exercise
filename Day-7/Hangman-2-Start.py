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


print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
        display[position] = letter

print(display)