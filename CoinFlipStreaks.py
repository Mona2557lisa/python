print("name : monalisa.n\n usn : 1AY24AI073 \n section : O ")

import random

def flip_coins(num_flips=100):
    return [random.choice(['H', 'T']) for _ in range(num_flips)]

def count_streaks(coin_flips, streak_length=6):
    streaks = 0
    current_streak = 1

    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:
            current_streak += 1
            if current_streak == streak_length:
                streaks += 1
        else:
            current_streak = 1
    return streaks

# Run simulation
flips = flip_coins()
print('Flips:', ''.join(flips))
print('Number of 6-in-a-row streaks:', count_streaks(flips))
