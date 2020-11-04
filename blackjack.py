import copy
import time
import random

player_money = 100
player_credits = 0
bet = 0

standard_deck = ['a_hea', 'a_dim', 'a_spa', 'a_clu',
                '2hea', '2dim', '2spa', '2clu',
                '3hea', '3dim', '3spa', '3clu',
                '4hea', '4dim', '4spa', '4clu',
                '5hea', '5dim', '5spa', '5clu',
                '6hea', '6dim', '6spa', '6clu',
                '7hea', '7dim', '7spa', '7clu',
                '8hea', '8dim', '8spa', '8clu',
                '9hea', '9dim', '9spa', '9clu',
                '10hea', '10dim', '10spa', '10clu',
                'j_hea', 'j_dim', 'j_spa', 'j_clu',
                'q_hea', 'q_dim', 'q_spa', 'q_clu',
                'k_hea', 'k_dim', 'k_spa', 'k_clu']


def gameplay():
    global player_credits
    global bet
#Variable used to exit main loop of player's turn   
    lp_break = False
    bet = 0
    
    shuffle_deck()
    
    print()
    time.sleep(1.5)
    print('The dealer deals your cards:')
    print()
    time.sleep(1.5)
    print(shuffled_deck[-1])
    player_hand.append(shuffled_deck[-1])
    shuffled_deck.remove(shuffled_deck[-1])
    time.sleep(1.5)
    print(shuffled_deck[-1])
    player_hand.append(shuffled_deck[-1])
    shuffled_deck.remove(shuffled_deck[-1])
    print()
    time.sleep(1.5)
    
    print('The dealer deals to herself:')
    print()
    time.sleep(1.5)
    print(shuffled_deck[-1])
    dealer_hand.append(shuffled_deck[-1])
    dealer_first_hand.append(shuffled_deck[-1])
    shuffled_deck.remove(shuffled_deck[-1])
    time.sleep(1.5)
    print('xxxx')
    dealer_hand.append(shuffled_deck[-1])
    dealer_first_hand.append('xxxx')
    shuffled_deck.remove(shuffled_deck[-1])
    time.sleep(1.5)
    print()
    print("Dealer's hand:")
    print(dealer_first_hand)
    print()
    print('Your Hand:')
    print(player_hand)
    print()
    print('Total:', calculate_hand(player_hand))
    print('Credits:',player_credits)
    print()
    time.sleep(1.5)
    print('Place Your Bet:')
    
    while True:
        player_bet = input('>')
        player_bet = int(player_bet)
        if player_bet > player_credits:
            print('You wager more than the credits you have. Please choose a lower amount')
        else:
            bet += player_bet
            player_credits -= player_bet
            break
            
#Loop for player's turn
    while True:
        if lp_break == True:
            break
        time.sleep(1.5)
        print()
        print('Wager:', bet)
        print()
        print("Dealer's hand:")
        print(dealer_first_hand)
        print()
        print('Your Hand:')
        print(player_hand)
        
        check_bust = calculate_hand(player_hand)
        if check_bust.lower() == 'bust':
            print('You Go Bust')
            print('Credits:', player_credits)
            time.sleep(1.5)
            break
        print()
        print('Total:', check_bust)
        print()
        time.sleep(1.5)
        print('Would You Like To (s)tand or (h)it?')
        
    
        while True:
            choice = input('>')
            if choice.lower() == 'h':
                time.sleep(1.5)
                print('The Dealer Deals You a Card:')
                time.sleep(1.5)
                print(shuffled_deck[-1])
                time.sleep(1.5)
                player_hand.append(shuffled_deck[-1])
                shuffled_deck.remove(shuffled_deck[-1])
                break
            if choice.lower() == 's':
                dealer_round()
                player = calculate_hand(player_hand)
                dealer = calculate_hand(dealer_hand)
                calculate_win(player, dealer)
                lp_break = True
                break
            else:
                print('Incorrect Input. Please enter "s" or "h".')

def shuffle_deck():
    deck_to_shuffle = copy.deepcopy(standard_deck)
    for i in range(len(standard_deck)):
        card = random.choice(deck_to_shuffle)
        shuffled_deck.append(card)
        deck_to_shuffle.remove(card)
        
def credits_get():
    global player_money
    global player_credits
    
    while True:
        credit_choice = int(input('>'))
        if credit_choice > player_money:
            print('You only have', player_money, 'money. Please choose a lower amount')
        else:
            player_credits += credit_choice
            player_money -= credit_choice
            return credit_choice
            
def calculate_hand(hand):
    ace_high = True
    ace = False
    count = 0
    check = False
    
    while True:
        for i in hand:
            if i[0] == 'a':
                ace = True
                if ace_high == True:
                    count += 11
                else:
                    count += 1
            if i[0] == '2':
                count += 2
            if i[0] == '3':
                count += 3
            if i[0] == '4':
                count += 4
            if i[0] == '5':
                count += 5
            if i[0] == '6':
                count += 6
            if i[0] == '7':
                count += 7
            if i[0] == '8':
                count += 8
            if i[0] == '9':
                count += 9
            if i[0] == '1':
                count += 10
            if i[0] in ['j', 'q', 'k']:
                count += 10
                
        if count < 22:
            return str(count)
        elif count > 21 and ace == True and check == False:
            ace_high = False
            count = 0
            check = True
        else:
            return 'Bust'
            
def calculate_win(player_tot, dealer_tot):
    global player_credits
    global bet
    if dealer_tot == 'Bust':
        print('You Win')
        player_credits += bet*2
        print('Credits:', player_credits)
    elif player_tot == dealer_tot:
        print("It's a Draw")
        player_credits += bet
        print('Credits:', player_credits)
    elif int(player_tot) > int(dealer_tot):
        print('You Win')
        player_credits += bet*2
        print('Credits:', player_credits)
    else:
        print("Dealer Wins")
        print('Credits:', player_credits)
    time.sleep(1.5)    
        
def dealer_round():
    print('Dealer reveales turned over card:')
    time.sleep(1.5)
    print(dealer_hand)
    while True:
        dealer_total = calculate_hand(dealer_hand)
        if dealer_total == 'Bust':
            time.sleep(1.5)
            print(dealer_hand)
            print('Dealer Goes Bust')
            time.sleep(1.5)
            break
        elif int(dealer_total) > 15:
            time.sleep(1.5)
            print(dealer_hand)
            print('Dealer Stands On',dealer_total)
            time.sleep(1.5)
            break
        else:
            time.sleep(1.5)
            print('Dealer Deals Herself a Card:')
            print(shuffled_deck[-1])
            dealer_hand.append(shuffled_deck[-1])
            shuffled_deck.remove(shuffled_deck[-1])
            





#Main game loop
while True:
    player_hand = []
    dealer_hand = []
    dealer_first_hand = []
    shuffled_deck = []
    
    time.sleep(1.5)
#Way to escape main game loop    
    print("Press enter to continue playing blackjack or 'q' to leave the table")
    leave = input('>')
    if leave.lower() == 'q':
        break
    
    print('Your Money:', player_money)
    print('Player Credits:', player_credits)
    print('Dealer asks how many credits you would like')
    
    credits_get()
    gameplay()
