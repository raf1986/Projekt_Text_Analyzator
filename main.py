'''
author = Roman Kolar
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

oddelovac = 30 * "-"
reg_users = { "bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
username = input("Enter username: ")
password = input("Enter password: ")
print(oddelovac)
if reg_users.get(username) == password:
    print(f"Welcome to the app, {username} \nWe have 3 texts to be analyzed.")
else:
    print("Username or password is wrong")
    exit()
print(oddelovac)

select_text = int(input("Enter a number btw. 1 and 3 to select: "))

mode = 1
while mode == 1:
    if select_text <= 3 and select_text > 0:
        print("ok")
        break
    else:
        select_text = int(input("Enter a number btw. 1 and 3 to select: "))


text_list = list(TEXTS[select_text - 1].split(" "))
text_clean = []
for slovo in text_list:
  text_clean.append(slovo.strip("@{}&~ˇ^˘°˛`„'´˝÷<>*,.()#đ“\n"))

count_words = len(text_clean)

print(oddelovac)
print(f"There are {count_words} words in the selected text.")


upper_words = 0
lower_words = 0
title_words = 0
count_numbers = 0
sum_numbers = 0

for slovo in text_clean:
    if slovo.isupper() and slovo.isalpha():
        upper_words += 1
    elif slovo.islower():
        lower_words += 1
    elif slovo.istitle():
        title_words += 1
    elif slovo.isnumeric():
        count_numbers += 1
        sum_numbers += int(slovo)
    else:
        print("End")


print(f"There are {title_words} titlecase words.")
print(f"There are {upper_words} uppercase words.")
print(f"There are {lower_words} lowercase words.")
print(f"There are {count_numbers} numeric strings.")
print(f"The sum of all the numbers {sum_numbers} ")


vyskyt_slov = []
for slovo in text_clean:
  vyskyt_slov.append(len(slovo))

print(oddelovac)
print("LEN|".ljust(3) + "OCCURENCES".ljust(16) + "|NR")
for number in range(1,12):
     vyskyt = vyskyt_slov.count(number)
     graf = "*" * vyskyt
     print(f"{str(number).rjust(3)}|{graf.ljust(16)}|{vyskyt}")
