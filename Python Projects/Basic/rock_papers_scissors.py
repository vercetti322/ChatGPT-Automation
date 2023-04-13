import random as rd

def play():
    user = input("What's your choice? 'r' is for rock, 'p' is for paper and 's' is for scissors\n")
    computer = rd.choice(['r', 'p', 's']) 

    if user == computer:
        return 'tie'
    if win(user, computer):
        return 'You won'
    
    return 'You lost!'
    
# to check if player defeats opponent
def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

play()
