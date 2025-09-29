import random

print("Winning Rules of the game ROCK PAPER SCISSORs are:\n"
+ "ROCK vs PAPER ----> Paper Wins\n"
+ "ROCK vs SCISSOR ----> Rock Wins\n"
+ "PAPER vs SCISSOR ----> Scissor Wins\n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissor \n")

# Take the input from user
    choice = int(input("Enter your choice: "))

        # Looping until user enters valid input:
    while choice > 3 and choice <1:
        choice = int(input('Enter a valid choice: '))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

        # Print user choice
        print('User choice is:', choice_name)
        print("Now it's Computer's Turn...")

        comp_choice = random.randint(1, 3)

        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'


        print("Computer choice is:", comp_choice_name)
        print(choice_name, 'vs', comp_choice_name)


            # Determine the winner
        if choice == comp_choice:
            result = "DRAW"
        elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
            result = 'Paper'
        elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
            result = 'Rock'
        elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
            result = 'Scissors'


            # Print the result
        if result == "DRAW":
            print("<== It's a tie! ==>")
        elif result == choice_name:
            print("<== User wins! ==>")
        else:
            print("<== Computer wins! ==>")

        # Ask if the user wants to play again
        print("Do you want to play again? (Y/N)")
        ans = input().lower()
        if ans == 'n':
            break

    # After coming out of the while loop, print thanks for playing
    print("Thanks for playing!")