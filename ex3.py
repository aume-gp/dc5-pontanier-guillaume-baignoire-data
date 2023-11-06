coutcampagne = 34000
revenucampagne  = 54000

if coutcampagne <= 0 or revenucampagne <= 0:
    print("Les valeurs de coût et de revenu ne peuvent pas être nulles.")
elif coutcampagne < 0:
    print("Le coût de la campagne ne peut pas être négatif.")
elif revenucampagne < 0:
    print("Le revenu de la campagne ne peut pas être négatif.")
else:
    if revenucampagne > coutcampagne:
        print("La campagne est rentable.")
    else:
        print("La campagne n'est pas rentable.")