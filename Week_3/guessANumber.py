import random

randomNumber = random.randint(1, 101)
score = 0

difficulty = input("Enter the difficulty 'easy' or 'hard: ")

if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5


def checkScore(lives, randomNumber, score):
    # global lives,randomNumbers,score
    while (lives):  # lives= 0
        user_choice = int(input("enter the number: "))
        if (user_choice == randomNumber):
            print("Congrats u won")
            randomNumber = random.randint(1, 101)
            isWin = True
            score += 1
            checkScore(lives, randomNumber, score)
            break

        elif user_choice > randomNumber:
            print("Wrong Too high")
        else:
            print("Wrong too low")
        lives -= 1
# not True =False

    if not (lives):
        print("Your final score is: ", score)
        playAgain = input("Would u like to play again 'yes' or 'no': ")
        if playAgain == 'yes':
            playAgain = True
        else:
            playAgain = False
    return playAgain


playAgain = True
while (playAgain):
    result = checkScore(lives, randomNumber, score)

    playAgain = result
