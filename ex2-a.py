depensesmarket = [2300, 5600, 5890, 4300, 2300, 2100, 4000, 3400, 3000, 2800, 2100, 3950]

def depenseannuelle(depenses):
    if not depenses:
        return "La liste des dépenses est vide"

    for depense in depenses:
        if isinstance(depense, str):
            return "La liste ne peut pas contenir des chaînes de caractères"
        if depense < 0:
            return "La liste ne peut pas contenir des nombres négatifs"
        
    total = 0
    for i in depensesmarket:
        total = total + i
    return total

print(depenseannuelle(depensesmarket))