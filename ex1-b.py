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

nbmots = 0
for i, char in enumerate(phrase):
    if char.isalnum():
        if i + 1 == len(phrase) or not phrase[i + 1].isalnum():
            nbmots += 1
    else:
        if not char.isspace():
            if i + 1 == len(phrase) or phrase[i + 1].isspace() or phrase[i + 1].isalnum():
                nbmots += 1

print("La phrase en majuscules :", phrasemaj)
print("La phrase en miniscules :", phrasemin)
print("Il y a", nbmots, "mots dans la phrase")