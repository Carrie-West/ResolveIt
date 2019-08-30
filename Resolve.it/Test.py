'''
Created on Aug 29, 2019

@author: Carrie
'''
from _ctypes import Array
class Player:  #defining the basic characteristics of a player
    health=0
    name=""
    
    def __init__ (self,name,health): 
        self.name=name
        self.health=health
        return
    def health (self):
        if self.health <=0:
            print("You are already dead.")
            return
    
def start(): 
    no_players=int(input("How many players are there? "))
    
    playerList=[]
    for x in range(no_players):
        name=input("What is your name? ")
        health=input(name + ", what is your current health? ")
        
        p=Player (name,health)
        playerList.append(p)

start()