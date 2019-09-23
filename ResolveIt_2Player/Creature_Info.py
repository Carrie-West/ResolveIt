'''
Created on Sep 17, 2019

@author: Carrie
'''
from Run_Program import doomedDissenter
class Creature():
    creatureToughness = 1
    creaturePower = 1
    creatureName=""
    creatureList=[]
    powerList=[]
    sacrifice=""
    def __init__ (self, creatureName, creaturePower, creatureToughness):
        self.creaturePower=creaturePower
        self.creatureToughness=creatureToughness
        self.creatureName=creatureName
        Creature.creatureList.append(creatureName)
        if creatureToughness == 0:
            print("This creature has died.")
            del Creature.creatureList[creatureName]
        print(Creature.creatureList)
    def creatureCreate(self, creatureName, creaturePower, creatureToughness):
        self.creaturePower=creaturePower
        self.creatureToughness=creatureToughness
        self.creatureName=creatureName
    def creatureActivatedAbility(self, name):
        if Creature.creatureName == "Carrion Feeder":
            sacrifice=input("What creature is being sacrificed?")
            if sacrifice == "Doomed Dissenter":
                zombie=Creature("Zombie", 2, 2)
    def creatureTriggeredAbility(self, name):
        if name == doomedDissenter:
            if Creature.creatureToughness == 0:
                del Creature.creatureList[Creature.creatureName]
                Creature.creatureCreate("Zombie",2,2)         

