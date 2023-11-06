def ctr(clics, impressions):
    if not (isinstance(clics, int) and isinstance(impressions, int)):
        return "Les clics et les impressions doivent être des nombres entiers"
    elif clics < 0 or impressions < 0:
        return "Les clics et les impressions ne peuvent pas être des nombres négatifs"
    elif impressions < clics:
        return "Le nombre d'impressions ne peut pas être inférieur au nombre de clics"
    elif impressions == 0:
        return "Il n'y a pas d'impressions donc impossible"
    elif clics == 0:
        return "Il n'y a pas de clics donc impossible"
    else:
        ctr = (clics / impressions) * 100
        return "Le CTR est de", ctr, "%"

print(ctr(0, 1021))
print(ctr(0, 0))
print(ctr(803, 99))
print(ctr(715, 1500))
print(ctr(215.2, 143.8))
print(ctr(-2, 1300))