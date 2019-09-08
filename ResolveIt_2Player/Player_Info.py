'''
Created on Sep 8, 2019

@author: Carrie
''' 
class PlayerOne:
    PlayerOneHealth=1
    PlayerOneName=""
    def _init_ (self, PlayerOneName, PlayerOneHealth):
        self.PlayerOneName=PlayerOneName
        self.PlayerOneHealth=PlayerOneHealth
class PlayerTwo:
    PlayerTwoHealth=1
    PlayerTwoName=""
    def _init_ (self, PlayerTwoName, PlayerTwoHealth):
        self.PlayerTwoName=PlayerTwoName
        self.PlayerTwoHealth=PlayerTwoHealth
p1=PlayerOne()
p2=PlayerTwo()
def start():
    p1.PlayerOneName=input("What is your name? ")
    p1.PlayerOneHealth=int(input(p1.PlayerOneName + ", what is your current health? "))
    p1.PlayerOne=[p1.PlayerOneName,p1.PlayerOneHealth]
    p2.PlayerTwoName=input("What is your name? ")
    p2.PlayerTwoHealth=int(input(p2.PlayerTwoName + ", what is your current health? "))
    p2.PlayerTwo=[p2.PlayerTwoName,p2.PlayerTwoHealth]
    player_list=[p1,p2]
    return player_list
