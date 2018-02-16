import random

PersonA = int(random.random()*3)
PersonB = int(random.random()*3)

if PersonA == PersonB:
    print("Oh, it was Aiko")
elif (PersonA - PersonB)%3 == 1:
    print("Tomo won")
else:
    print("Hana won")

