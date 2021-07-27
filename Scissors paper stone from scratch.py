start_game = input('Type start to start game:').lower()
import random
def is_win(player,opponent):
    if (player == 'rock'and opponent == 'scissors') or (player == 'scissors'and opponent == 'paper') or \
            (player=='paper' and opponent == 'rock'):
        return True
    else:
        return False

def play():
    user = input("'rock' , 'paper', 'scissors' ").lower()
    if user == 'quit':
        print("Game ended :(")
        exit()
    computer = random.choice(['rock', 'paper','scissors'])
    print(computer)
    if user == computer:
        return "It's a tie!"
    elif is_win(user, computer):
        return 'You win!'
    else:
        return 'You lost!'

while True:
    if start_game != 'start':
        start_game = input('Sorry i dont understand please try again:')
    else:
        print(play())