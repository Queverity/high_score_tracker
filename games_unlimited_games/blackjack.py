#Blackjack code for high score tracker
import random
import time
import sys

def clear_screen(): print("\033c", end = "")



def print_slow(text):

    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)

    print()



def create_deck():

    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

    random.shuffle(deck)

    return deck



def deal_hand(deck, num_cards = 2):

    hand = []

    for _ in range(num_cards):
        card = deck.pop()
        if card == 11: 
            card = "J"
        elif card == 12: 
            card = "Q"
        elif card == 13: 
            card = "K"
        elif card == 14: 
            card = "A"
        
        hand.append(card)

    return hand



def calculate_total(hand):
    total = 0
    aces = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            total += 11
            aces += 1
        else:
            total += card
    
    while total > 21 and aces:
        total -= 10
        aces -= 1
    
    return total



def print_hands(player_hand, dealer_hand, reveal_dealer = False):
    
    if reveal_dealer:
        slow_print(f"Dealer's hand: {dealer_hand} (Total: {calculate_total(dealer_hand)})")
    else:
        slow_print(f"Dealer's showing: {dealer_hand[0]}")
    
    slow_print(f"Your hand: {player_hand} (Total: {calculate_total(player_hand)})")



def hit(deck, hand):
    
    card = deck.pop()
    
    if card == 11:
        card = "J"
    elif card == 12: 
        card = "Q"
    elif card == 13: 
        card = "K"
    elif card == 14: 
        card = "A"
    
    hand.append(card)



def check_blackjack(player_hand, dealer_hand):

    player_total = calculate_total(player_hand)

    dealer_total = calculate_total(dealer_hand)

    if player_total == 21:
        print_hands(player_hand, dealer_hand, reveal_dealer = True)
        slow_print("You got a Blackjack!")
        return True
    elif dealer_total == 21:
        print_hands(player_hand, dealer_hand, reveal_dealer = True)
        slow_print("Dealer got a Blackjack.")
        return True



def game():

    clear_screen()

    print_slow("It's Blackjacking time.")

    money = 100

    while True:

        blackjack_bet = input(f"How much do you want to bet, you have ${money}")

        if not blackjack_bet.isdigit():
            print_slow("Please enter valid number.")
            clear_screen()
            continue

        blackjack_bet = int(blackjack_bet)\
        
        if blackjack_bet <= 0 or blackjack_bet > money:
            print_slow("Please enter valid number.")
            clear_screen()
            continue

        current_deck = create_deck()

        player_hand = deal_hand(current_deck)

        dealer_hand = deal_hand(current_deck)

        print_hands(player_hand, dealer_hand)



game()