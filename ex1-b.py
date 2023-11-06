phrase = input("Saisir une phrase : ")

phrasemaj = ""
for lettre in phrase:
    if 'a' <= lettre <= 'z':
        maj = chr(ord(lettre) - 32)
        phrasemaj += maj
    else:
        phrasemaj += lettre

phrasemin = ""
for lettre in phrase:
    if 'A' <= lettre <= 'Z':
        min = chr(ord(lettre) + 32)
        phrasemin += min
    else:
        phrasemin += lettre

nbmots = sum(1 for i, mot in enumerate(phrase) if (not mot.isspace() and (i + 1 == len(phrase) or phrase[i + 1].isspace())))

print("La phrase en majuscules :", phrasemaj)
print("La phrase en miniscules :", phrasemin)
print("Il y a", nbmots, "mots dans la phrase")