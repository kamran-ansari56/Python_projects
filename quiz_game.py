print('Welcome to the Tutorial!')

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :)")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect!!')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect!!')

answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print('Correct!')
    score +=1
else:
    print('Incorrect')

answer = input("What does PSU stand for? ")
if answer.lower() == 'power supply unit':
    print('Correct!')
    score +=1
else:
    print('Incorrect')

print(f"You got {score} questions correct!")
print(f"You got {(score/4) * 100} %")