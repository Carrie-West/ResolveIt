'''
Created on Sep 8, 2019

@author: Carrie
'''
import Player_Info
from Damage_Spells import Shock, Lightning_Bolt
import Creature_Info
c=Creature_Info
doomed=c.creatureCreate("Doomed Dissenter", 1, 1, False, False, False)
carrion=c.creatureCreate("Carrion Feeder", 1, 1, False, False, False)
rhonas=c.creatureCreate("Rhonas the Indomitable", 5, 5, True, False, False)
print(c.Creature.creatureList)
print(carrion.indestructible)
player_list=Player_Info.start()

rhythmCheck = input("Is Rhythm of the Wild active right now? (Y/N)")
if rhythmCheck == "Y":
    for x in c.Creature.creatureList:
        print(x)
        riot=input("Should this creature gain haste or a +1/+1 counter? (HASTE OR COUNTER)")
        if riot == "COUNTER":
            if x == "Doomed Dissenter":
                doomed.creaturePower +=1
                doomed.creatureToughness +=1
            elif x == "Carrion Feeder":
                carrion.creaturePower +=1
                carrion.creatureToughness +=1
            elif x == "Rhonas the Indomitable":
                rhonas.creaturePower +=1
                rhonas.creatureToughness +=1
        elif riot == "HASTE":
            if x == "Doomed Dissenter":
                doomed.haste = True
            elif x == "Carrion Feeder":
                carrion.haste = True
            elif x == "Rhonas the Indomitable":
                rhonas.haste = True
stack=[]
stack.append("LightningBolt")
stack.append("LightningBolt")
stack.append("Wrath of God")
stack.append("Shock")
stack.append("Counterspell")
fizzle= "N"
i=0
while i<=len(stack):
    for x in stack:
        print(stack)
        MTG=stack.pop()
        print(stack)
        if MTG == "Shock":
            i +=1
            fizzle= "Y"
            while fizzle == "Y":
                target=input("What is Shock targeting?(" + Player_Info.p1.PlayerOneName + "," + Player_Info.p2.PlayerTwoName + ", or creature)")
                if target == Player_Info.p1.PlayerOneName and Player_Info.p1.PlayerOneHexproof == False:
                    Player_Info.p1.PlayerOneHealth=Shock(Player_Info.p1.PlayerOneHealth)
                    print(Player_Info.p1.PlayerOneHealth)
                    fizzle="N"
                elif target == Player_Info.p2.PlayerTwoName and Player_Info.p2.PlayerTwoHexproof == False:
                    Player_Info.p2.PlayerTwoHealth=Shock(Player_Info.p2.PlayerTwoHealth)
                    print(Player_Info.p2.PlayerTwoHealth)
                    fizzle = "N"
                elif target == "creature":
                    print (Creature_Info.Creature.creatureList)
                    target=input("Which creature is this targetting?")
                    if target == "Doomed Dissenter":
                        print(doomed.creatureToughness)
                        doomed.creatureToughness=Shock(doomed.creatureToughness)
                        if doomed.creatureToughness <= 0:
                            c.Creature.creatureList.remove("Doomed Dissenter")
                            c.dissenterTrigger()
                        fizzle = "N"
                    if target == "Carrion Feeder":
                        print(carrion.creatureToughness)
                        sac=input("Would you like to sacrifice a creature you control to put a +1/+1 counter on Carrion Feeder? (Y/N)")
                        while sac == "Y":
                            c.feederActivated()
                            sac=input("Would you like to do this again?(Y/N)")
                            print(carrion.creatureToughness)
                            carrion.creatureToughness=Shock(carrion.creatureToughness)
                        fizzle = "N"
                else:
                    print("This is not a valid target, choose again.")
        elif MTG == "LightningBolt":
            fizzle= "Y"
            while fizzle == "Y":
                target=input("What is Lightning Bolt targeting?(" + Player_Info.p1.PlayerOneName + "," + Player_Info.p2.PlayerTwoName + ", or creature)")
                if target == Player_Info.p1.PlayerOneName and Player_Info.p1.PlayerOneHexproof == False:
                    Player_Info.p1.PlayerOneHealth=Lightning_Bolt(Player_Info.p1.PlayerOneHealth)
                    print(Player_Info.p1.PlayerOneHealth)
                    fizzle="N"
                elif target == Player_Info.p2.PlayerTwoName and Player_Info.p2.PlayerTwoHexproof == False:
                    Player_Info.p2.PlayerTwoHealth=Lightning_Bolt(Player_Info.p2.PlayerTwoHealth)
                    print(Player_Info.p2.PlayerTwoHealth)
                    fizzle="N"
                elif target == "creature":
                    print (Creature_Info.Creature.creatureList)
                    target=input("Which creature is this targetting?")
                    if target == "Doomed Dissenter":
                        print(doomed.creatureToughness)
                        doomed.creatureToughness=Lightning_Bolt(doomed.creatureToughness)
                        if doomed.creatureToughness <= 0:
                            c.Creature.creatureList.remove("Doomed Dissenter")
                            c.dissenterTrigger()
                            fizzle+"N"
                    if target == "Carrion Feeder":
                        print(carrion.creatureToughness)
                        sac=input("Would you like to sacrifice a creature you control to put a +1/+1 counter on Carrion Feeder? (Y/N)")
                        while sac == "Y":
                            c.feederActivated()
                            sac=input("Would you like to do this again?(Y/N)")
                            print(carrion.creatureToughness)
                            carrion.creatureToughness=Lightning_Bolt(carrion.creatureToughness)
                            fizzle="N"
                    else:
                        print("This is not a valid target, choose again.")
        elif MTG == "Counterspell":
            print(stack)
            target=len(stack)-int(input("Which spell is this targetting? (Starting with 1 as the newest cast spell remaining on the stack.)"))
            del stack[target]
        elif MTG == "Wrath of God":
            doomedTriggers=0
            count=0
            dying=[]
            for x in (c.Creature.creatureList):
                count +=1
                print(c.Creature.creatureList)
                print(x)
                if x == "Doomed Dissenter" and doomed.indestructible != True:
                    dying.append(x)
                    doomedTriggers =+ 1
                    print(doomedTriggers)
                if x == "Carrion Feeder" and carrion.indestructible != True:
                    dying.append(x)
                if x == "Rhonas the Indomitable" and rhonas.indestructible != True:
                    dying.append(x)
                if x == "Zombie" and z.indestructible != True:
                    dying.append(x)
            for y in list(dying):
                if y in c.Creature.creatureList:
                    c.Creature.creatureList.remove(y)
                    dying.remove(y)
            spawnTrigger = True
            while spawnTrigger == True:
                c.dissenterTrigger()
                doomedTriggers =- 1
                if doomedTriggers == 0:
                    spawnTrigger = False
            print(c.Creature.creatureList)
