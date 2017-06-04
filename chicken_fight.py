#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 00:23:00 2017

@author: stevedeng
"""

"""This file contains code to create a virtual cockfight.  It instantiates two chicken objects and sets them to fight each other"""

#import some useful modules
import random
import time

#import the chicken classes we want to create
from JitteryChicken import *
from IntelligentChicken import *

#make two chicken objects - two JitteryChicken objects are created here for example.  
#We can create any type of chicken class, as long as it is a sub-class of FuriousChicken
#Ideally, we will create two different types of chickens to see which is superior
chick1 = JitteryChicken("Bocker")
chick2 = IntelligentChicken("SteveTheIntelligent")

#set the two chickens as opponents
chick1.set_opponent(chick2)
chick2.set_opponent(chick1)

#start the fight
round_num = 1
game_over = False
MAX_ROUNDS = 100

#loop until the game is over
while not game_over:
    #print out the round number
    print("\nROUND {}\n".format(round_num))
    
    #need to reset Chicken's attacking and defending to prevent BUG
    chick1.reset_attack_and_defence()
    chick2.reset_attack_and_defence()
    
    #let the underdog go first 20% of the time
    num = random.randint(1,5)
    if num == 1:
        shake_it_up = True
    else:
        shake_it_up = False

    #figure out who goes first
    if chick1.get_average_health() == chick2.get_average_health():
        #if both chickens have equal health, choose who goes first randomly
        num = random.randint(1,2)
        if num == 1:
            #chick1 goes first
            chick1.make_your_move()
            chick2.make_your_move()
        else:
            #chick2 goes first
            chick2.make_your_move()
            chick1.make_your_move()
        
    elif (chick1.get_average_health() > chick2.get_average_health()) and not shake_it_up:
        # otherwise, chick1 goes first if it has higher health, except for 20% random exceptions
        #each chicken makes a move in this order
        chick1.make_your_move()
        chick2.make_your_move()
    else:
        # otherwise, chick2 goes first if it has higher health or this is a random 
        #each chicken makes a move in reverse order
        #make their moves
        chick2.make_your_move()
        chick1.make_your_move()

    #check for a win scenario
    if len(chick1.get_body_parts()) <= 0:
        #chick1 has expired... output who won
        print("\n{} the {} WINS!!!".format(chick2.name.upper(), type(chick2).__name__))
        print("\n{} the {} WINS!!!".format(chick2.name.upper(), type(chick2).__name__))
        game_over = True
    elif len(chick2.get_body_parts()) <= 0:
        #chick2 has expired... output who won
        print("\n{} the {} WINS!!!".format(chick1.name.upper(), type(chick1).__name__))
        print("\n{} the {} WINS!!!".format(chick1.name.upper(), type(chick1).__name__))
        game_over = True
    elif round_num >= MAX_ROUNDS:
        print("\nOUT OF TIME!!!")
        #check who wins in a timeout scenario
        if chick1.get_average_health() > chick2.get_average_health():
            #chick1 has won... output who won
            print("\n{} the {} WINS!!!".format(chick1.name.upper(), type(chick1).__name__))
            print("\n{} the {} WINS!!!".format(chick1.name.upper(), type(chick1).__name__))
        elif chick2.get_average_health() > chick1.get_average_health():
            #chick1 has won... output who won
            print("\n{} the {} WINS!!!".format(chick2.name.upper(), type(chick2).__name__))
            print("\n{} the {} WINS!!!".format(chick2.name.upper(), type(chick2).__name__))
        else:
            #tie game
            print("\nTIE!!!")
            print("\nTIE!!!")
        game_over = True        

    #if there is a win, output the remaining body parts on each chicken
    if game_over:
        print("\n{}'s ({}%) remaining body parts: {}\n".format(chick1.name, chick1.get_average_health(), ", ".join(chick1.get_body_parts())))
        print("\n{}'s ({}%) remaining body parts: {}\n".format(chick2.name, chick2.get_average_health(), ", ".join(chick2.get_body_parts())))
                
    #increase the round number
    round_num += 1

    #pause so we can read what's happening
    #time.sleep(5)