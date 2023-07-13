from questionModel import AskQues
from data import question_data
from quiz_brain import Score, CheckAns


askQues = AskQues()
question_checker = CheckAns()

# print(askQues.get_ques(question_data[0]))


# //ask as question
# take a input
# check asnwer
# if true
#   continue till score reaches 10
# else
#   print score and ask user to play again
play_again = True
while (play_again):

    scoreCalc = Score()
    for i in range(0, 11):
        print(f"{i+1}. {askQues.get_ques(question_data[i])}\n(True/False)")

        userAnswer = input().capitalize()
        answer = askQues.get_ans(question_data[i])

        result = question_checker.check_ans(userAnswer, answer=answer)

        scoreCalc.update_score(result)

        if (result):
            print("You got it right: ")
            print(f"your current score is: {scoreCalc.get_score()}/{i}.\n\n\n")
        else:
            print("Thats Wrong: ")
            print(f"your current score is: {scoreCalc.get_score()}/{i}.\n\n\n")
            break

    play_again = input(
        "Do you want to play again:\nType 'y' for playing again else any key to exit : ")

    print("\n\n\n")
    if play_again.lower() == "y":
        is_true = True
    else:
        is_true = False
