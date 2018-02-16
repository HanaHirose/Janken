import random

PersonA = int(random.random()*3)
PersonB = int(random.random()*3)

if PersonA == 0:
    print("Tomo played scissors\n")
elif PersonA == 1:
    print("Tomo played rock\n")
elif PersonA == 2:
    print('Tomo played paper\n')

if PersonB == 0:
    print("Hana played scissors\n")
elif PersonB == 1:
    print("Hana played rock\n")
elif PersonB == 2:
    print("Hana played paper\n")


if PersonA == PersonB:
    print("Oh, it was Aiko")
elif (PersonA - PersonB)%3 == 1:
    print("Tomo won")
else:
    print("Hana won")