import itertools
import random


def player(prev_play, opponent_history=[], previous_plays={}, length=5):
    best_plays = {'R': 'P', 'S': 'R', 'P': 'S'}

    if not prev_play:
        for v in itertools.product('RSP', repeat=length):
            key = ''.join(v)
            previous_plays[key] = 0
    else:
        opponent_history.append(prev_play)

    last_plays = opponent_history[-length:]

    if len(last_plays) == length:
        previous_plays[''.join(last_plays)] += 1

        next_play_keys = [''.join(last_plays)[-(length - 1):] + v for v in 'RSP']
        choices = {k: previous_plays[k] for k in next_play_keys}
        next_play = max(choices, key=choices.get)
        if choices[next_play] == 0:
            guess = random.choice('RPS')
        else:
            guess = best_plays[next_play[-1]]
    else:
        # Default strategy, random choice
        guess = random.choice('RPS')

    return guess
