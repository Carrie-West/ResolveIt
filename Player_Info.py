'''
Created on Sep 8, 2019

@author: Carrie
''' 
class PlayerOne:
    PlayerOneHealth=1
    PlayerOneName=""
    def _init_ (self, PlayerOneName, PlayerOneHealth, PlayerOneHexproof):
        self.PlayerOneName=PlayerOneName
        self.PlayerOneHealth=PlayerOneHealth
        self.PlayerOneHexproof=PlayerOneHexproof
class PlayerTwo:
    PlayerTwoHealth=1
    PlayerTwoName=""
    def _init_ (self, PlayerTwoName, PlayerTwoHealth, PlayerTwoHexproof):
        self.PlayerTwoName=PlayerTwoName
        self.PlayerTwoHealth=PlayerTwoHealth
        self.PlayerTwoHexproof=PlayerTwoHexproof
p1=PlayerOne()
p2=PlayerTwo()
def start():
    p1.PlayerOneName=input("What is your name? ")
    p1.PlayerOneHealth=int(input(p1.PlayerOneName + ", what is your current health? ")) 
    hexCheckOne=input("Do you have hexproof right now? (Y/N)")
    if hexCheckOne == "Y":
        p1.PlayerOneHexproof = True
    else:
        p1.PlayerOneHexproof = False
    p1.PlayerOne=[p1.PlayerOneName,p1.PlayerOneHealth,p1.PlayerOneHexproof]
    p2.PlayerTwoName=input("What is your name? ")
    p2.PlayerTwoHealth=int(input(p2.PlayerTwoName + ", what is your current health? "))
    hexCheckTwo=input("Do you have hexproof right now? (Y/N)")
    if hexCheckTwo == "Y":
        p2.PlayerTwoHexproof = True
    else:
        p2.PlayerTwoHexproof = False
    p2.PlayerTwo=[p2.PlayerTwoName,p2.PlayerTwoHealth,p2.PlayerTwoHexproof]
    player_list=[p1,p2]
    return player_list
