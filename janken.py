import random

PersonA = int(random.random()*3)
PersonB = int(random.random()*3)

if PersonA == PersonB:
    print("Oh, it was Aiko")
elif PersonA - PersonB == 1:
    print("Tomo won")
elif PersonA - PersonB == -2:
    print("Tomo won")
else:
    print("Hana won")

