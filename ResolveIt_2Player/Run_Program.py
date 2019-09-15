'''
Created on Sep 8, 2019

@author: Carrie
'''
import Player_Info
from Damage_Spells import Shock, Lightning_Bolt
from pip._vendor.requests.api import delete
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
            target=input("Who is Shock targeting?")
            if target == Player_Info.p1.PlayerOneName:
                Player_Info.p1.PlayerOneHealth=Shock(Player_Info.p1.PlayerOneHealth)
                print(Player_Info.p1.PlayerOneHealth)
            elif target == Player_Info.p2.PlayerTwoName:
                Player_Info.p2.PlayerTwoHealth=Shock(Player_Info.p2.PlayerTwoHealth)
                print(Player_Info.p2.PlayerTwoHealth)
            else:
                print("This is not a valid player")
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