'''
Created on Sep 17, 2019

@author: Carrie
'''
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
        if Creature.creatureToughness == 0:
            print("This creature has died.")
            del Creature.creatureList[Creature.creatureName]
        print(Creature.creatureList)
def creatureActivatedAbility(creatureName):
    if Creature.creatureName == "Carrion Feeder":
        sacrifice=input("What creature is being sacrificed?")
        if sacrifice == "Doomed Dissenter" and "Doomed Dissenter" in Creature.creatureList:
            z=Creature("Zombie", 2, 2)
        elif sacrifice in Creature.creatureList:
            Creature.creaturePower =+ 1
            Creature.creaturePower =+ 1
def creatureTriggeredAbility(creatureName):
    print(Creature.creatureName)
    if Creature.creatureName == "Doomed Dissenter":
        if Creature.creatureToughness == 0:
            del Creature.creatureList[Creature.creatureName]
            z=Creature.creatureCreate("Zombie",2,2)         
def creatureCreate(creatureName, creaturePower, creatureToughness):
        creature=Creature(creatureName,creaturePower,creatureToughness)
        return creature