import random


def the_rules():
    if player == computer:
        print('you tie')
    elif player == 'r':
        if computer == 's':
            print('you win ')
        else:
            print('you lose')
    elif player == 'p':
        if computer == 'r':
            print('you win')
        else:
            print('you lose')
    elif player == 's':
        if computer == 'p':
            print("you win ")
        else:
            print("you lose")


timesYouWannaPlay =int(input("how many times do u wanna play"))
gameCount = timesYouWannaPlay
end = 0
while gameCount != end:
    player = input("enter your choice ")
    player.lower()
    choices = ["r", 'p', 's']
    computer = random.choice(choices)
    print(f'you chose {player}, computer chose {computer}')
    the_rules()
    gameCount -=1