import numpy as np
import time

balance = 100
won = False

while True:
    won = False
    print("Your balance is", balance)
    bet = int(input("Enter your bet amount:"))
    multiplier = float(input("Enter your multiplier (starting from 1.1)"))

    winamounts = [1.1,
                  1.2,
                  1.3,
                  1.4,
                  1.5,
                  1.6,
                  1.7,
                  1.8,
                  1.9,
                  2,
                  2.2,
                  2.4,
                  2.6,
                  2.8,
                  3,
                  3.5,
                  4,
                  4.5,
                  5,
                  6,
                  7,
                  8,
                  9,
                  10,
                  20,
                  30,
                  50,
                  100,
                  250,
                  500,
                  1000
                  ]
    gamemult = winamounts[round(len(winamounts) - np.random.power(3, 1)[0] * len(winamounts))]
    # print(gamemult)

    for i in winamounts:
        print(".", end='')
        time.sleep(0.5)

        if i >= multiplier and not won:
            print("!", end='')
            won = True
            balance = balance + bet * multiplier
        if i >= gamemult:
            print('\n' + str(gamemult))
            break
    if not won:
        print("You lost :(!")
        balance = balance - bet

    print("Your balance is", balance)

    choice = input("Would you like to play again? (y/n)")
    if choice == "n":
        break
