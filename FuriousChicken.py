#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 17:28:35 2017

@author: stevedeng
"""

"""This file contains the code for the FuriousChicken class."""
import random

class FuriousChicken:
    """Template for a warrior chicken who fights till the end.  This class is meant to be sub-classed and have its make_your_move() function overidden."""
    
    def __init__(self, name):
        """Initial setup of each FuriousChicken object, including its name, health, and list of body parts."""
        
        #set the chicken's name
        self.name = name

        #start off with most body parts
        self.body_parts = [
                            "left leg", "right leg",
                            "left foot", "right foot",
                            "left breast", "right breast",
                            "left wing", "right wing",
                            "left eye", "right eye",
                            "beak",
                            "wattle",
                            "comb"
                            ]

        #start out with each body part being totally healthy
        self.initialize_health(100)

        #start off not attacking or protecting any body parts (note the use of the None literal keyword indicating no value)
        self.reset_attack_and_defence()

        #start off with no opponent (note the use of the None literal keyword indicating no value)
        self.opponent = None

    def initialize_health(self, max_value):
        """set up the initial health values for each body part"""
        self.health = {} #empty dictionary

        #set an initial health value for each body part
        for body_part in self.get_body_parts():
            self.health[body_part] = max_value
    
    def set_health(self, body_part, x):
        """setter for health value

        Keyword arguments:
            x - the new health value 
        """
        #health is allowed to be a value between 0 and 100
        if x >=0 and x <= 100:
            #update this body part's health
            self.health[body_part] = x

    def get_health(self, body_part):
        """getter for health property

        Returns the current health property's int value
        """
        return self.health[body_part]

    def get_average_health(self):
        sum = 0
        num_body_parts = 0
        for body_part in self.get_body_parts():
            sum += self.get_health(body_part)
            num_body_parts += 1

        if num_body_parts >= 1:
            avg = sum / num_body_parts
        else:
            avg = 0
        return avg
    
    def get_attacking(self):
        """getter for attacking property

        Returns the current attacking property's string value
        """
        return self.attacking

    def get_defending(self):
        """getter for defending property

        Returns the current defending property's string value
        """
        return self.defending
        
    def adjust_health(self, body_part, x):
        """This method adjust the chicken's health by a certain amount

        Keyword arguments:
            x - the amount to adjust the health
        """
        #calculate the new health 
        current_health = self.get_health(body_part)
        new_health = current_health + x
        
        #prevent negative health which resulting in bug
        if new_health < 0:
            new_health = 0

        #set the new health
        self.set_health(body_part, new_health)

    def set_opponent(self, opponent):
        """Sets the opponent of this chicken to be another chicken

        Keyword arguments:
            opponent - another chicken to fight
        """
        if isinstance(opponent, FuriousChicken):
            self.opponent = opponent
        else:
            print("Sorry, {} only fights other Furious Chickens or their descendents.".format(self.name))

    def get_opponent(self):
        """getter for opponent property

        Returns the current opponent property's value, which is most likely some kind of FuriousChicken object
        """
        return self.opponent

    def get_body_parts(self):
        """getter for the body_parts property

        Returns the current body_parts value, which is a list of body parts this chicken has
        """
        return self.body_parts

    def reset_attack_and_defence(self):
        """reset the attack and defence targets in preparation a round of fighting.  This sets the attacking and defending properties to non-values"""
        #set both attacking and defending to non-values... they must be explicitly set with every turn
        self.attacking = None
        self.defending = None

    def recuperate(self):
        """this method allows the chicken to regain a bit of strength by increasing its health value"""
        print("{} is resting".format(self.name))

        #give an extra point for resting
        for body_part in self.get_body_parts():
            self.adjust_health(body_part, 1)

    def defend(self, body_part):
        """defend the selected body part of the chicken against attacks by setting the defending property to the body part the chicken wants to protect

        Keyword arguments:
            body_part - a string representing the body part this chicken should protect
        """
        self.defending = body_part

        print("{} is defending its {} ({}%)".format(self.name, body_part, self.get_health(body_part)))
       
    def attack(self, body_part):
        """attack the opponent chicken at the selected body part

        Keyword arguments:
            body_part - a string representing the body part of the opponent that this chicken should attack
        """
        self.attacking = body_part #remember which body part we are attacking
        opponent = self.get_opponent() #get the opponent chicken in a simple variable

        #injure the selected body part, if it exists in the opponent's list of body parts
        if body_part in opponent.get_body_parts():
            #if the opponent has the selected body part, initiate an attack
            print("{} is attacking {}'s {} ({}%)!".format(self.name, opponent.name, body_part, opponent.get_health(body_part)))
            opponent.receive_attack(body_part)
        else:
            #if the opponent doesn't have the selected body part, the attack is futile!
            print("{} is trying to attack {}'s {}, but {} doesn't have a {}!!!".format(self.name, opponent.name, body_part, opponent.name, body_part))
            

    def receive_attack(self, body_part):
        """determine whether the attack will inflict damage

        Keyword arguments:
            body_part - a string representing the body part that this chicken is receiving an attack upon
        """
        opponent = self.get_opponent() #get the opponent chicken in a simple variable

        #as long as this chicken is not defending this body part, they will suffer an injury
        if body_part != self.defending:
            #if the chicken was not defending the attacked body part, inflict damage
            self.suffer_injury(body_part)
        else:
            #this chicken was defending the attacked body part
            print("{} defended against {}'s attack on its {} ({}%)!".format(self.name, opponent.name, body_part, self.get_health(body_part))) 

    def suffer_injury(self, body_part):
        """suffer injury on the selected body part on the chicken

        Keyword arguments:
            body_part - a string representing the body part that this chicken will suffer an injury upon
        """
        opponent = self.get_opponent() #get the opponent chicken in a simple variable

        #either injure or outright remove the selected body part, if it exists in this chicken's list of body parts
        if body_part in self.get_body_parts():

            health = self.get_health(body_part) #the health value for this body part
            self.adjust_health(body_part, -25) #subtract points for each attack
            health = self.get_health(body_part) #the health value for this body part
            
            if health <= 0:
                #if the health of this body part has dropped below zero, remove the body part
                self.remove_body_part(body_part)
                print("{}'s {} is completely out of action!!!".format(self.name, body_part))
            else:
                print("{} injured {}'s {} ({}%)".format(opponent.name, self.name, body_part, self.get_health(body_part)))

    def remove_body_part(self, body_part):
        """remove a body part from the chicken

        Keyword arguments:
            body_part - a string representing the body part that this chicken will completely lose
        """
        #remove the selected body part from this chicken's list of body parts
        self.body_parts.remove(body_part)        


    def make_your_move(self):
        """decide what move to make at any given round.  This function is intended to be customized in all sub-classes of this FuriousChicken class"""
        #you will create a sub-class of the FuriousChicken class
        #in that sub-class you will ovveride this make_your_move() function with your own customized version in order to make your chicken superior to all other chickens
        #this should be the only function you override from FuriousChicken... all other functions should be left as-is in the FuriousChicken class
        #your job is to make your chicken win by adding intelligent logic here

        #ultimately, this function must call one of the following other functions:
        # - self.attack(body_part), where body_part is a string representing the body part of the other chicken to attack
        # - self.defend(body_part), where body_part is a string representing the body part of this chicken to protect
        # - self.recuperate()

        #some ideas:
        # - use the various functions in this class to figure out what's going on with this chicken and the opponent chicken
        # - if your chicken is in bad shape, let it rest or defend itself!
        # - if the other chicken is in bad shape, perhaps attack more!
        # - don't try to attack body parts that don't exist... the body_parts list contains all body parts  that each chicken has available
        # - perhaps streamline your chicken so it doesn't have extraneous body parts that are vulnerabilities
        # - try to guess what the other chicken is about to do and pre-empt it!

        #which one of these functions you call at any given time, and which body part you protect or attack is the key to success