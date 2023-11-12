def factoriel(n):
    if not isinstance(n, int):
        return "N doit être un nombre entier."
    if n < 0:
        return "N ne peut pas être négatif."
    if n == 0:
        return 1
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

print(factoriel(7))
print(factoriel(-2))
print(factoriel(0))
print(factoriel(3.5))