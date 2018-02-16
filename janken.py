import getpass

PersonA_win = 0
PersonB_win = 0
Aiko = 0
Hands = [0,1,2]

PersonA_name = input("enter your name\n")
PersonB_name = input("enter your name\n")


while True:
    while True:
        PersonA = int(getpass.getpass(prompt="{}".format(PersonA_name)+", please choose your hand\n0 is scissors, 1 is rock, 2 is paper\n"))
        if PersonA in Hands:
            break
        else:
            print("You did not choose a valid hand! Please input your hand again!\n")
    while True:
        PersonB = int(getpass.getpass(prompt="{}".format(PersonB_name)+", please choose your hand\n0 is scissors, 1 is rock, 2 is paper\n"))
        if PersonB in Hands:
            break
        else:
            print("You did not choose a valid hand! Please input your hand again!\n")
    if PersonA == 0:
        print("{}".format(PersonA_name)+" played scissors\n")
    elif PersonA == 1:
        print("{}".format(PersonA_name)+" played rock\n")
    elif PersonA == 2:
        print("{}".format(PersonA_name)+" played paper\n")
    
    if PersonB == 0:
        print("{}".format(PersonB_name)+" played scissors\n")
    elif PersonB == 1:
        print("{}".format(PersonB_name)+" played rock\n")
    elif PersonB == 2:
        print("{}".format(PersonB_name)+" played paper\n")
    
    
    if PersonA == PersonB:
        print("Oh, it was Aiko")
        Aiko += 1
    elif (PersonA - PersonB)%3 == 1:
        print("{}".format(PersonA_name)+" won")
        PersonA_win += 1
    else:
        print("{}".format(PersonB_name)+" won")
        PersonB_win += 1
    
    cont = input("Do you want to continue the game?[y/n]\n")
    if cont == "n":
        break
    
print("{}".format(PersonA_name)+" won %d times\n" % PersonA_win)
print("{}".format(PersonB_name)+" won %d times\n" % PersonB_win)
print("Aiko %d times\n" % Aiko )
print("{}".format(PersonA_name)+" v.s. {}".format(PersonB_name)+"\n %d : %d" % (PersonA_win/(PersonA_win+PersonB_win)*100, PersonB_win/(PersonA_win+PersonB_win)*100))
