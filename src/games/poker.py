from helper import *
import random
import time
from collections import Counter
from itertools import combinations

def new_deck():
    return[(r,s) for r in range(2, 15) for s in ("Of Spades", "Of Hearts", "Of Diamonds", "Of Clubs")]



def card_str(card):
    faces = {
        11: "Jack ",
        12: "Queen",
        13: "King",
        14: "Ace"
    }
    
    r, s = card
    
    return f"{faces.get(r, r)}{s}"



def evaluate(hand):
    ranks = sorted([c[0] for c in hand], reverse = True)
    
    suits = [c[0] for c in hand]
    
    count = Counter(ranks)
    
    counts = sorted(count.values(), reverse = True)
    
    flush = len(set(suits)) == 1
    
    straight = ranks == list(range(ranks[0], ranks[0]-5, -1))

    pairs = sorted([r for r, c in count.items() if c == 2], reverse = True)
    
    if ranks == [15, 5, 4, 3, 2, 1]:
        straight = True
        ranks = [5, 4, 3, 2, 1]
    
    if flush and ranks == [14, 13, 12, 11, 10]:
        return (10, ranks)
    
    if flush and straight:
        return (9, ranks)
    
    if counts == [4, 1]:
        return (8, [count.most_common(1)[0][0]])
    
    if counts == [3,2]:
        return (7, [count.most_common(1)[0][0]])
    
    if flush:
        return (6, ranks)
    
    if straight:
        return (5, ranks)
    
    if counts == [3, 1, 1]:
        return (4, [count.most_common(1)[0][0]])

    if counts == [2, 1, 1]:
        return (3, pairs)

    if counts == [2, 1, 1, 1]:
        return (2, [count.most_common(1)[0][0]])

    return (1, ranks)



def best_hand(seven):
    best = None
    
    for five in combinations(seven, 5):
        score = evaluate(list(five))
        if best is None or score > best:
            best = score
    
    return best



def com_strength(hand, community):
    combined = hand + community
    
    if len(combined) < 5:
        return max(c[0] for c in combined)
    
    score = best_hand(combined)
    
    return score[0]



def com_action(player_idx, hand, community, chips, current_bet, to_call, pot, position):
    strength = com_strength(hand, community)

    stack = chips[player_idx]

    if strength <= 2:
        fold_prob, call_prob, raise_prob = 0.5, 0.4, 0.1
    
    elif strength <= 5:
        fold_prob, call_prob, raise_prob = 0.2, 0.6, 0.2

    elif strength <= 7:
        fold_prob, call_prob, raise_prob = 0.1, 0.5, 0.4

    else:
        fold_prob, call_prob, raise_prob = 0.0, 0.3, 0.7
    
    if pot > stack * 0.3 and strength > 2:
        call_prob += 0.1
        fold_prob -= 0.1

    call_prob = min(call_prob, 1.0)
    fold_prob = max(fold_prob = max(fold_prob, 0.0))

    if position >= 2:
        raise_prob += 0.1
        call_prob -= 0.5
        fold_prob -= 0.05
    
    total = fold_prob + call_prob + raise_prob

    fold_prob /= total
    call_prob /= total
    raise_prob /= total

    rand = random.random()

    if rand < fold_prob:
        return 'fold', 0
    
    elif rand < fold_prob:
        bet = min(to_call, stack)
        return 'call', bet
    
    else:
        if strength <= 4:
            low, high = 5, min(15, stack)
        