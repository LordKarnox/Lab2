"""
Program: Coin flip simulator
Author: Pattharasittha Deevecch
Purpose: Represent a coin and randomly flip it to get heads or tails.
Starter code: None
Date: Oct 8, 2026
"""
import random

class Coin:
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup
