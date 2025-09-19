def nearestMultiple(num):
    if num >= 4:
        return num + (4 - (num % 4))
    else:
        return 4

def lose1():
    print("\n\nYou Lose")
    print("Better Luck Next Time")
    exit()

def check(xyz):
    for i in range(1, len(xyz)):
        if xyz[i] - xyz[i-1] != 1:
            return False
    return True

def start1():
    xyz = []
    last = 0

    print("Enter 'F' to take the first chance")
    print("Enter 'S' to take the second chance")
    chance = input("> ").upper()

    if chance == 'F':
        while True:
            if last == 21:
                lose1()

            print("\nYour Turn")
            print("How many numbers do you wish to enter (1-3)?")
            inp = int(input("> "))

            if inp < 1 or inp > 3:
                print('Wrong Input. You are disqualified from the game')
                lose1()

            print('Now enter the values')
            for i in range(inp):
                a = int(input('> '))
                xyz.append(a)

            if not check(xyz):
                print("\nYou did not input consecutive integers.")
                lose1()

            last = xyz[-1]
            if last == 21:
                print("Congratulations!!! You Won!")
                exit()

            # Computer's turn
            comp = 4 - inp
            for j in range(comp):
                xyz.append(last + j + 1)
            last = xyz[-1]
            print("Order of inputs after computer's turn is: ", xyz)

            if last == 21:
                lose1()

    elif chance == 'S':
        comp = 1
        while True:
            # Computer plays first
            for j in range(comp):
                xyz.append(last + j + 1)
            last = xyz[-1]
            print("Order of inputs after computer's turn is: ", xyz)

            if last == 21:
                lose1()

            # Player's turn
            print("\nYour turn.")
            print("How many numbers do you wish to enter (1-3)?")
            inp = int(input('> '))

            print("Enter your values")
            for i in range(inp):
                xyz.append(int(input("> ")))

            if not check(xyz):
                print("\nYou did not input consecutive numbers.")
                lose1()

            last = xyz[-1]
            if last == 21:
                print("\n\nCongratulations !!!")
                print("You Won !")
                exit(0)

            comp = 4 - inp
    else:
        print("Wrong choice")


# Game loop
while True:
    print("Player 2 is Computer.")
    print("Do you want to play the 21 number game? (Yes / No)")
    ans = input("> ").upper()
    if ans == "YES":
        start1()
    else:
        print("Do you want to quit the game? (Yes / No)")
        nex = input("> ").upper()
        if nex == "YES":
            print("You are quitting the game...")
            exit(0)
        elif nex == "NO":
            print("Continuing...")
        else:
            print("Wrong Choice")
