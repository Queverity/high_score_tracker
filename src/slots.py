import random
import time as t
import os
from helper import *



def spin_grid():
    symbols = ['🍒', '🥀', '😂', '🍎', '⭐']
    return [[random.choice(symbols) for _ in range(3)] for _ in range(3)]



def print_grid(grid):
    print("*************")
    for row in grid:
        print("  ", " | ".join(row))
    print("*************")



def get_payout(grid, bet):
    payout = 0

    for row in grid:
        if row[0] == row[1] == row[2]:
            payout += symbol_multiplier(row[0]) * bet

    if grid[0][0] == grid[1][1] == grid[2][2]:
        payout += symbol_multiplier(grid[0][0]) * bet
    if grid[0][2] == grid[1][1] == grid[2][0]:
        payout += symbol_multiplier(grid[0][2]) * bet

    return payout



def symbol_multiplier(symbol):
    if symbol == '🍒':
        return 3
    elif symbol == '🥀':
        return 4
    elif symbol == '😂':
        return 5
    elif symbol == '🍎':
        return 10
    elif symbol == '⭐':
        return 20
    return 0



def not_main():
    money = 100
    print("   Welcome to slots!")
    print("   Symbols: 🍒 🥀 😂 🍎 ⭐")

    while money > 0:
        print(f"\nCurrent money: ${money}")
        
        bet = input("Place your bet amount: $")
        
        if not bet.isdigit():
            print("Please enter a valid input.")
            continue

        bet = int(bet)

        if bet > money:
            print("You don't have that much money.")
            continue
        elif bet <= 0:
            print("Bet must be greater than 0.")
            continue

        money -= bet
        print("\nSpinning...\n")
        t.sleep(1)
        grid = spin_grid()
        print_grid(grid)

        payout = get_payout(grid, bet)
        t.sleep(1)
        if payout > 0:
            print(f"You won ${payout}!")
            money += payout
            if play_again != 'Y':
                quit = input("Would you like to continue playing? Y/N:\n").strip().capitalize()
                if quit == "Y":
                    return int(money)
                else:
                    clear_screen()
                    continue
        else:
            print("You lost.")
            play_again = input("Do you want to spin again? (Y/N): ").upper()
            if play_again != 'Y':
                quit = input("Would you like to continue playing? Y/N:\n").strip().capitalize()
                if quit == "Y":
                    return int(money)
                else:
                    clear_screen()
                    continue
        if money == 0:
            print("\nNo more money!")
            break

        

    print(f"Game over!")



def slots_main():
    while True:
        money = not_main()
        choice = input("Do you want to play again? Y/N:\n").upper()
        if choice != "Y":
            return int(money)
            clear_screen()
        else:
            continue            

