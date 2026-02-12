#Blackjack code for high score tracker
import random
import time
import sys

def clear_screen(): 
    print("\033c", end = "")



def print_slow(text):

    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

    print()



def continue_screen():
    print_slow("Press Enter to continue.")
    input()



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
        print_slow(f"Dealer's hand: {dealer_hand} (Total: {calculate_total(dealer_hand)})")
    else:
        print_slow(f"Dealer's showing: {dealer_hand[0]}")
    
    print_slow(f"Your hand: {player_hand} (Total: {calculate_total(player_hand)})")



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
        print_slow("You got a Blackjack!")
        return True
    elif dealer_total == 21:
        print_hands(player_hand, dealer_hand, reveal_dealer = True)
        print_slow("Dealer got a Blackjack.")
        return True



clear_screen()

money = 100

print_slow("Blackjacking time.")



def game(money):

    while True:
        
        print_slow(f"How much do you want to bet, you have ${money}:")
        blackjack_bet = input("$")

        if not blackjack_bet.isdigit():
            print_slow("Please enter valid number.")
            continue_screen()
            clear_screen()
            continue

        blackjack_bet = int(blackjack_bet)
        
        if blackjack_bet <= 0 or blackjack_bet > money:
            print_slow("Please enter valid number.")
            continue_screen()
            clear_screen()
            continue

        money -= blackjack_bet

        current_deck = create_deck()

        player_hand = deal_hand(current_deck)

        dealer_hand = deal_hand(current_deck)

        print_hands(player_hand, dealer_hand)

        
        while True:
            
            choice = input("Hit or Stand:\n").strip().lower()

            if choice == "hit":
                hit(current_deck, player_hand)
                print_hands(player_hand, dealer_hand)

                if calculate_total(player_hand) > 21:
                    print_slow("You busted.")
                    break
            
            elif choice == "stand":
                break

            else:
                print_slow("Please enter valid input.")
                
        
        while calculate_total(dealer_hand) < 17:
            
            hit(current_deck, dealer_hand)

        continue_screen()
        clear_screen()


        print_hands(player_hand, dealer_hand, reveal_dealer = True)

        player_total = calculate_total(player_hand)
        dealer_total = calculate_total(dealer_hand)

        if player_total > 21:
            print_slow("You busted.")
            continue_screen()
            clear_screen()

        elif dealer_total > 21:
            print_slow("Dealer busted.")
            money += blackjack_bet * 2
            continue_screen()
            clear_screen()

        elif player_total > dealer_total:
            print_slow("You win.")
            money += blackjack_bet * 2
            continue_screen()
            clear_screen()

        elif player_total < dealer_total:
            print_slow("Dealer wins.")
            continue_screen()
            clear_screen()

        elif player_total == dealer_total:
            print_slow("It's a tie.")
            continue_screen()
            clear_screen()
            money += blackjack_bet

        return
    
while True:
    game(money)