"""
Program: Match Coins Game - Player Class
Author: Pattharasittha Deevech
Purpose: Player info management
Starter code: None
Date: October 8, 2026
"""

from coin import Coin

class Player:
    def __init__(self, name):
        self.name = name
        self.coin = Coin()
        self.score = 0

    def toss_coin(self):
        self.coin.toss()

    def get_coin_side(self):
        return self.__coin.get_sideup()

    def win_coin(self):
        self.__wallet += 1

    def lose_coin(self):
        self.__wallet -= 1

    def get_wallet(self):
        return self.__wallet

    def get_name(self):
        return self.name
    