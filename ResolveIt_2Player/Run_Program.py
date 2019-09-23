'''
Created on Sep 8, 2019

@author: Carrie
'''
import Player_Info
from Damage_Spells import Shock, Lightning_Bolt
import Creature_Info
c=Creature_Info
x=c.Creature("Doomed Dissenter", 1, 1)
y=c.Creature("Carrion Feeder", 1, 1)
print (c.Creature.creatureList)
player_list=Player_Info.start()

stack=[]
stack.append("LightningBolt")
stack.append("LightningBolt")
stack.append("Shock")
stack.append("Counterspell")
i=0
while i<=len(stack):
    for x in stack:
        print(stack)
        MTG=stack.pop()
        print(stack)
        if MTG == "Shock":
            i +=1
            target=input("What is Shock targeting?(" + Player_Info.p1.PlayerOneName + "," + Player_Info.p2.PlayerTwoName + ", or creature)")
            if target == Player_Info.p1.PlayerOneName:
                Player_Info.p1.PlayerOneHealth=Shock(Player_Info.p1.PlayerOneHealth)
                print(Player_Info.p1.PlayerOneHealth)
            elif target == Player_Info.p2.PlayerTwoName:
                Player_Info.p2.PlayerTwoHealth=Shock(Player_Info.p2.PlayerTwoHealth)
                print(Player_Info.p2.PlayerTwoHealth)
            elif target == "creature":
                print (Creature_Info.Creature.creatureList)
                target=input("Which creature is this targetting?")
                if target == "Doomed Dissenter":
                    Creature_Info.Creature.name=doomedDissenter
                    doomedDissenter.creatureToughness=Shock(doomedDissenter.creatureToughness)
                    Creature_Info.Creature.creatureTriggeredAbility(doomedDissenter)      
                    print(Creature_Info.Creature.creatureList)
            else:
                print("This is not a valid target")
        elif MTG == "LightningBolt":
            target=input("Who is Lightning Bolt targeting?")
            if target == Player_Info.p1.PlayerOneName:
                Player_Info.p1.PlayerOneHealth=Lightning_Bolt(Player_Info.p1.PlayerOneHealth)
                print(Player_Info.p1.PlayerOneHealth)
            elif target == Player_Info.p2.PlayerTwoName:
                Player_Info.p2.PlayerTwoHealth=Lightning_Bolt(Player_Info.p2.PlayerTwoHealth)
                print(Player_Info.p2.PlayerTwoHealth)
            else:
                print("This is not a valid player")
        elif MTG == "Counterspell":
            print(stack)
            target=len(stack)-int(input("Which spell is this targetting? (Starting with 1 as the newest cast spell remaining on the stack.)"))
            del stack[target]