import random
playerspoints=0
computerspoints=0

def the_rules():
    computerPoints= computerspoints
    userPoint=playerspoints
    if player == computer:
        print('you tie')
    elif player == 'r':
        if computer == 's':
            print('you win ')
            userPoint+=1
        else:
            print('you lose')
            computerPoints+=1
    elif player == 'p':
        if computer == 'r':
            print('you win')
            userPoint+=1
        else:
            print('you lose')
            computerPoints+=1
    elif player == 's':
        if computer == 'p':
            print("you win ")
            userPoint+=1
        else:
            print("you lose")
            computerPoints+=1

    print(f'the computer has{computerPoints},while u have {userPoint}')


gameCount = int(input("how many times do u wanna play"))
end = 0

while gameCount != end:
    player = input("enter your choice ")
    player.lower()
    choices = ["r", 'p', 's']
    computer = random.choice(choices)
    print(f'you chose {player}, computer chose {computer}')
    the_rules()
    gameCount -=1

