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
    choice_name == 'Rock'
elif choice == 2:
    choice_name == 'Paper'
else:
    choice_name = 'Scissors'