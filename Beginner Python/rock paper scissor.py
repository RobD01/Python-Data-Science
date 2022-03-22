# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:45:08 2022

@author: medbz
"""

import random

def play():
    user = input("""Let\'s play Rock Paper Scissors! \n
Choose either: \n
R for rock, P for paper, S for scissor: """).lower()
    computer = random.choice(['r', 'p', 's'])
    print (f'You chose {user}! I chose {computer}!')
    if input not in ['r','p','s']:
        print('That is not a real move. Only choose P R or S')
    elif user == computer :
        print ('Tie')
    elif iswin(user,computer):
        print ('You won!')
    else:
        print('You lose!')

def iswin(player,opponent):
    if player == 'r' and opponent == 's' or \
    player == 'p' and opponent == 'r' or \
    player == 's' and opponent == 'p':
        return True

play()
