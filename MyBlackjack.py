from random import *
from os import system as sys

cards = [2,3,4,5,6,7,8,9,10,10,10,10, 11]
d_hand = None
p_hand = None
money = 1000
pot = 0
all_in = False

def Restart():
    global all_in
    global d_hand
    global p_hand
    global pot
    d_hand = None
    p_hand = None
    pot = 0
    all_in = False

def Start():
    global cards
    global d_hand
    global p_hand
    d_hand = [choice(cards), choice(cards)]
    p_hand = [choice(cards), choice(cards)]
#    p_hand = [,]
#    d_hand=[,]

def Print(d_turn = False):
    sys("clear")
    global d_hand
    global p_hand
    global money
    global pot
    global all_in
    print("H = Hit, S = Stand\n     Blackjack!\n")
    print("   Pot =", pot)
    if all_in:
        print("      All In.")
    if d_turn:
        print("   ",d_hand,"Total:",sum(d_hand))
    else:
        print("   ",[d_hand[0], "?"])
    print("   ",p_hand,"Total:",sum(p_hand))
    print("===============")

def Check():
    global d_hand
    global p_hand
    global money
    global pot
    global all_win
    if sum(d_hand) == 21 and sum(p_hand) == 21:
        Print(True)
        print("Mega draw... womp")
        money += pot/2
        Again()
    if sum(d_hand) == 21:
        Print(True)
        print("Dealer Wins.")
        if all_in:
            print("Don't all-in next time (:")
            exit()
        Again()
#    elif sum(p_hand) == 21:
#        Print(True)
#        print("You Win!")
#        money += pot
#        Again()
    p_total = 0
    p_ace = []
    d_total = 0
    d_ace = []
    #Checking Player hand:
    for j in range(len(p_hand)):
        if p_hand[j] == 11:
            p_ace.append(j)
    p_total = sum(p_hand)
    if p_total > 21:
        if 11 not in p_hand:
            Print(True)
            print("You busted. . . wait-")
            Again()
        else:
            p_hand[p_ace[0]] = 1
    #Checking Dealer hand:
    for j in range(len(d_hand)):
        if d_hand[j] == 11:
            d_ace.append(j)
    d_total = sum(d_hand)
    if d_total > 21:
        if 11 not in d_hand:
            Print(True)
            print("Dealer Busted! . . wait-")
            money += pot
            Again()
        else:
            d_hand[d_ace[0]] = 1

def dTurn():
    global d_hand
    global p_hand
    global money
    global pot
    global all_in
    while True:
        Print(True)
        if sum(d_hand) > sum(p_hand):
            print("Dealer Wins!")
            if all_in:
               print("U lose the all in\nGet good")
               exit()
            Again()
        elif sum(d_hand) >= 16:
            Check()
            final_Check()
        if sum(d_hand) <= 15:
            d_hand.append(choice(cards))
            Check()

def final_Check():
    global d_hand
    global p_hand
    global pot
    global money
    global all_in
    Check()
    if sum(d_hand) > sum(p_hand):
        print("Dealer Wins!")
        if all_in:
            print("Out of money so womp")
            exit()
        Again()
    elif sum(d_hand) < sum(p_hand):
        print("You Win!")
        money += pot
        Again()
    else:
        print("Draw")
        money += pot/2
        Again()

def Again():
    global cards
    global pot
    user = str(input("Play Again? y/n: "))[0].lower()
    if user != "y":
        exit()
    else:
        Restart()
        BlackJack(cards)

def BlackJack(cards):
    global d_hand
    global p_hand
    global money
    global pot
    global all_in
    money = int(money)
    Started = False
    Start()
    all_in = False
    Failed = False
    while Failed == False:
        if Started == False:
            print("   Money:", money)
            how_much = int(input("How much will you bet?: "))
            if how_much <= 0:
                print("You changed your mind and don't want to play blackjack.")
                exit()
            elif how_much == money:
                all_in = True
                Started = True
            else:
                Started = True
            money -= how_much
            pot += how_much*2
        Check()
        Print()
        user = str(input("   Hit or Stand?: ")).lower()
        if user == "h":
            p_hand.append(choice(cards))
            Check()
        elif user == "s":
            dTurn()
        else:
            print("'S'' or 'H' please.")
    print("Out of money so womp")
    exit()

BlackJack(cards)