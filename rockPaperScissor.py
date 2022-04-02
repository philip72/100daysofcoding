# import random
# playerspoints=0
# computerspoints=0
#
# def the_rules():
#     computerPoints= computerspoints
#     userPoint=playerspoints
#     if player == computer:
#         print('you tie')
#     elif player == 'r':
#         if computer == 's':
#             print('you win ')
#             userPoint+=1
#         else:
#             print('you lose')
#             computerPoints+=1
#     elif player == 'p':
#         if computer == 'r':
#             print('you win')
#             userPoint+=1
#         else:
#             print('you lose')
#             computerPoints+=1
#     elif player == 's':
#         if computer == 'p':
#             print("you win ")
#             userPoint+=1
#         else:
#             print("you lose")
#             computerPoints+=1
#
#     print(f'the computer has{computerPoints},while u have {userPoint}')
#
#
# gameCount = int(input("how many times do u wanna play"))
# end = 0
#
# while gameCount != end:
#     player = input("enter your choice ")
#     player.lower()
#     choices = ["r", 'p', 's']
#     computer = random.choice(choices)
#     print(f'you chose {player}, computer chose {computer}')
#     the_rules()
#     gameCount -=1
#
import random

game=['rock','paper','scissor']
gameTimes=int(input('how many times'))
computerPoints=0
userPoints=0
while gameTimes!=0:
    userinput=input("enter you choice")
    userinput.lower()
    computer=random.choice(game)
    if userinput==computer:
        print('you tie')
        print(f'these are your points user{userPoints}, computer points{computerPoints}')
    elif userinput=='rock':
        if computer=='scissor':
            userPoints+=1
            print('you win')
        else:
            computerPoints+=1
            print("computer wins")
    elif userinput=='scissor':
        if computer== 'paper':
            userPoints+=1
            print("you win")
        else:
            computerPoints+=1
    elif userinput == 'paper':
        if computer=='rock':
            userPoints+=1
            print('you win')
        else:
            computerPoints+=1

    gameTimes-=1
print(f'u have {userPoints}, computer has{computerPoints}')
