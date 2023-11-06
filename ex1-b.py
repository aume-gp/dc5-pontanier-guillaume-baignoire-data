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

def caracterespecial(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')

nbmots = 0
for i, char in enumerate(phrase):
    if caracterespecial(char):
        if i + 1 == len(phrase) or not caracterespecial(phrase[i + 1]):
            nbmots += 1
    else:
        if not char.isspace():
            if i + 1 == len(phrase) or phrase[i + 1].isspace() or caracterespecial(phrase[i + 1]):
                nbmots += 1

print("La phrase en majuscules :", phrasemaj)
print("La phrase en miniscules :", phrasemin)
print("Il y a", nbmots, "mots dans la phrase")