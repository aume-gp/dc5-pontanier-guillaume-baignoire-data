nombres = [32, -10, 3.4, 283, 5.75, 6, 7.258, 28, "a", 100]

nombres_valid = [n for n in nombres if isinstance(n, (int, float)) and n * 100 == int(n * 100)]

maximum = minimum = moyenne = nombres_valid[0]
nombre_nombres = 1

for nombre in nombres_valid[1:]:
    if nombre > maximum:
        maximum = nombre
    if nombre < minimum:
        minimum = nombre
    moyenne += nombre
    nombre_nombres += 1

moyenne /= nombre_nombres

print("Voici le tableau de nombres :", nombres_valid)
print("Voici le nombre le plus grand :", maximum)
print("Voici le nombre le plus petit :", minimum)
print("Voici la moyenne des nombres :", moyenne)