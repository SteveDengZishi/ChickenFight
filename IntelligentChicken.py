#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 01:15:52 2017

@author: stevedeng
"""

from FuriousChicken import *

class IntelligentChicken(FuriousChicken):
    
    def count_injuries(self):
        cnt = 0
        for bodyPart in self.get_body_parts():
            if self.get_health(bodyPart) < 100:
                cnt+=1
        return cnt
    
    def make_your_move(self):

        #if your average health is below 85 percent, recuperate
        if self.get_average_health() <= 85 and self.count_injuries() >= 6:
            self.recuperate()
         
        #if opponent is defending a body part, do not attack that part
        else:
            opponent = self.get_opponent()
            opponent_defending = opponent.get_defending()
            
            #analyze opponent and find the weakest part to attack
            weakest_part = 'comb'
            second_weakest = 'wattle'
            for bodyPart in opponent.get_body_parts():
                if opponent.get_health(bodyPart) < opponent.get_health(weakest_part):
                    second_weakest = weakest_part
                    weakest_part = bodyPart
            
            if weakest_part != opponent_defending:
                self.attack(weakest_part)
            else:
                self.attack(second_weakest)
        #never defend as it is purely based on luck 