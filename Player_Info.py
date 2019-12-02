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
checkOne = False
checkTwo = False
def start():
    p1.PlayerOneName=input("What is your name? ")
    p1.PlayerOneHealth=int(input(p1.PlayerOneName + ", what is your current health? ")) 
    hexCheckOne=input("Do you have hexproof right now? (Y/N)")
    while checkOne == False
        if hexCheckOne == "Y":
            p1.PlayerOneHexproof = True
            checkOne = True
        elif hexCheckOne == "N":
            p1.PlayerOneHexproof = False
            checkOne = True
        else:
            print("This is not a valid input.")
    p1.PlayerOne=[p1.PlayerOneName,p1.PlayerOneHealth,p1.PlayerOneHexproof]
    p2.PlayerTwoName=input("What is your name? ")
    p2.PlayerTwoHealth=int(input(p2.PlayerTwoName + ", what is your current health? "))
    hexCheckTwo=input("Do you have hexproof right now? (Y/N)")
    while checkTwo == False
        if hexCheckTwo == "Y":
            p2.PlayerTwoHexproof = True
            checkTwo = True
        elif hexCheckTwo == "N":
            p2.PlayerTwoHexproof = False
            checkTwo = True
        else:
            print("This is not a valid input.")
    p2.PlayerTwo=[p2.PlayerTwoName,p2.PlayerTwoHealth,p2.PlayerTwoHexproof]
    player_list=[p1,p2]
    return player_list
