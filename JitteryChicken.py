#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 00:19:40 2017

@author: stevedeng
"""

"""
This file contains the JitteryChicken class, which is a sub-class of FuriousChicken
The make_your_move() function of FuriousChicken has been overidden here
Author: Foo Barstein
Date: 31 May 2016
"""

#import the necessary modules
import random
from FuriousChicken import *

class JitteryChicken(FuriousChicken):
    """Template for a random decision-making chicken descended from the original Furious Chicken"""

    #the only function you are allowed to override is the make_your_move function

    def make_your_move(self):
        """Overriding the FuriousChicken class's function by the same name.  This function randomly decides what this chicken should do each round"""

        #EXAMPLE ONLY... YOUR CHICKEN SHOULD MAKE ITS OWN DECISIONS WHAT TO DO
        
        #this chicken randomly decides whether it should attack, defend, or rest and recuperate
        what_to_do = random.randint(1,3)

        #randomly decide what body part to attack or defend
        #add a if statement to prevent empty range for randrange() BUG
        if len(self.get_body_parts()) != 0:
            num = random.randint(0, len(self.get_body_parts())-1) #a random number from 1 to however many body parts this chicken has
            body_part = self.body_parts[num] #select the random body part from the list of this chicken's body parts
        else:
            print("{} is dead now!!!".format(self.name))
            return
            
        if what_to_do == 1:
            #attack!
            self.attack(body_part)
        elif what_to_do == 2:
            #defend!
            self.defend(body_part)
        else:
            #rest and recuperate
            self.recuperate()