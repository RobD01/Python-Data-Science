import random

# =============================================================================
# def guess(x):
#     random_number= random.randint(1,x)
#     guess = 0
#     while (guess != random_number): 
#         guess = int(input(f'Guess a number between 1 and {x}:'))
#         if guess < random_number:
#             print('Guess is too low')
#         elif guess > random_number:
#             print('Guess is too high')
#     print(f'Jack pot! You guessed the number {random_number}')
# 
# 
# guess(5)
# =============================================================================

def computerguess(x):
    low = 1
    high = x
    feedback = ''
    while (feedback != 'c'):
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} too high (H), or too low (L), or correct (C) ?').lower()
        if feedback == 'h':
          high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'I have guessed your number, {guess}!')
    
computerguess(10)
