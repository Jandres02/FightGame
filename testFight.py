from random import randint
from fight import warrior

game = True
Player1 = warrior("Player1", 200)
Player2 = warrior("Player2", 200)
while game == True:
    election = int(input("1. Start game \n2. Exit\n"))
    if election == 1:
        while Player1.health > 0 and Player2.health > 0:
            print("Player1: ", Player1.health)
            print("Player2: ", Player2.health)

            movement = int(input("Choose your movement: \n 1. Superior \n 2. Inferior \n 3. Head \n 4. Protect Superior \n 5. Protect Inferior \n 6. Protect Head \n"))
            cpuMovement = randint(1, 6)

            print("Player1: ", movement)
            print("Player2: ", cpuMovement)
            print("")

            if movement == 1:
                Player1.atackSuperior(Player2)
            elif movement == 2:
                Player1.atackInferior(Player2)
            elif movement == 3:
                Player1.atackHead(Player2)
            elif movement == 4:
                Player1.protectSuperior()
            elif movement == 5:
                Player1.protectInferior()
            elif movement == 6:
                Player1.protectHead()

            if cpuMovement == 1:
                Player2.atackSuperior(Player1)
            elif cpuMovement == 2:
                Player2.atackInferior(Player1)
            elif cpuMovement == 3:
                Player2.atackHead(Player1)
            elif cpuMovement == 4:
                Player2.protectSuperior()
            elif cpuMovement == 5:
                Player2.protectInferior()
            elif cpuMovement == 6:
                Player2.protectHead()

            Player1.resetProtection()
            Player2.resetProtection()

        if Player1.health > 0:
            print("Player1 wins")
        else:
            print("Player2 wins")
    elif election == 2:
        print("Game over\n")
        print("Do you wanna play again? \n 1. Yes \n 2. No")
        election = int(input())
        if election == 1:
            pass
        else:
            game = False
        