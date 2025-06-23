import random
#coin_toss_debugged.py
#📄 Description:
#Fixes a buggy coin toss guessing game where the user gets two chances to guess correctly.
print("name :Monalisa.N \n usn : 1AY24AI073 \n section : O ")
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1)
toss = 'heads' if toss == 1 else 'tails'

if toss == guess:
    print('You got it!')
else:
    
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
