#1.Figūra(print)
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#2.Mainīgie(variables)
character_name = "George"
character_age = "70"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")


character_name = "Mike"
character_age = "45"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")

#Python galvenie datu tipi: strings("teksts"), numbers("11"), boolean value(True/False)  u.c.

#3.Strings - ir teksts
print("Giraffe\nAcedamy")  # \n pārnes vārdu, pirms kura atrodas, nākamajā rindā.
print("Giraffe\"]}(Acedamy")  #ja grib, lai izprintē zīmes, pirms tām jaliek  \  ,lai dators saprot, ka tā ir daļa no teksta nevis koda. 

phrase = "Giraffe Acedamy"
print(phrase.upper())  #upper() - teksts pārveidots ar lielajiem burtiem, lower() - zemajiem.
print(len(phrase))  #len(mainīgais) - izskiata burtu sk. Len atvasināts no lenght
print(phrase[0])  #izraksta 0. burtu no phrase
print(phrase.index("G")) #izvada G burta lokāciju no phrase.
print(phrase.replace("Giraffe", "Elephant")) #repleace("v., kas jāaizvieto", "v., ar kuru aizvieto")
