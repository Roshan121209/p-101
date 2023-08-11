import random

response = "y"

while response == "y":
    dice_roll = random.randint(1, 6)
    
    if dice_roll == 1:
        print(" --------- ")
        print("|         |")
        print("|    *    |")
        print("|         |")
        print(" --------- ")
    elif dice_roll == 2:
        print(" --------- ")
        print("|    *    |")
        print("|         |")
        print("|    *    |")
        print(" --------- ")
    elif dice_roll == 3:
        print(" --------- ")
        print("|    *    |")
        print("|    *    |")
        print("|    *    |")
        print(" --------- ")
    elif dice_roll == 4:
        print(" --------- ")
        print("|  *   *  |")
        print("|         |")
        print("|  *   *  |")
        print(" --------- ")
    elif dice_roll == 5:
        print(" --------- ")
        print("|  *   *  |")
        print("|    *    |")
        print("|  *   *  |")
        print(" --------- ")
    else:
        print(" --------- ")
        print("|  *   *  |")
        print("|  *   *  |")
        print("|  *   *  |")
        print(" --------- ")
    
    response = input("Roll the dice again? (y/n): ").lower()

print("Thanks for playing!")

