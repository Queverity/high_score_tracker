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
    return f"{faces.get(r,r),{s}}"



def evaluate(hand):
    ranks = sorted([c[0] for c in hand], reverse = True)
    