import os
import time
# Changes by Eliseo Magana
def menuScreen():
    print("WELCOME!")
    print("RPG Adventure 10")
    print("Copyright 2020")
def get_menu_options():
    option_title = input("Select an option: New Game, Load Game, Options, Exit: ")
    while option_title != 'New Game' and option_title != 'Load Game' and option_title != 'Options' and option_title != 'Exit':
        print ('Invalid Selection')
        option_title = input("Select an option: New Game, Load Game, Options, Exit: ")
    return option_title
def chooseClass():
    player_class = input('Choose your class: Potato, Karen, Unicorn: ' )
    while player_class != "Potato" and not player_class != "Karen" and not player_class !="Unicorn":
        print('Invalid choice. :(')
        player_class = input('Choose your class: Potato, Karen, Unicorn: ' )
    return player_class
def playerName(player_class):
    player_name = input(" please enter your  name ")
    print('Welcome, ' + player_name + ' the ' + player_class + '!')
    print("don't like your name?")
    time.sleep(1)
    print("too bad")
    return player_name

def eat_choice1():
     decision = input("Eat cold fries or ask for manager?")
    while decision != "Eat" and decision != "Ask":
        print("Invalid selection")
        decision = input("Eat cold fries or ask for manager?")
    if decision == "Eat":
        print('You have contracted the Coronavirus and have been doomed to Nacho Hell!!')
    if decision == "Ask":
        print('The manager walks up and says, "You dare complain about my Nacho Fries?!" and proceeds to choke you with cold Nacho Fries and banishes you to Nacho Hell!!')
    return decision
def redeem_swim():
    decision = input('Will you redeem yourself or dive further into the cold nacho cheese? Choose wisely: Redeem or Swim')
    while decision != "Redeem" and decision != "swim":
        print('Invalid')
        decision = input('Will you redeem yourself or dive further into the cold nacho cheese? Choose wisely: Redeem or Swim')
    if decision == "Swim":
        print('You jump into the river of nacho cheese and drown.')
        print("GAME OVER :(")
        exit(0)
    return decision
def dance_off():
    decision = input()
    while decision !="No" and decision!= "yes":
        print ('invalid')
        print('The Nacho reaper tells you to Dance ChampetaChallenge : Do you want to')
        decision = input()   
    if decision == "No":
          print('The Nacho Reaper bellows "Do you still want  to see the manager?!" and cast you into a nachoy darkness.')
          print('GAME OVER :(')
          exit(0)
    return decision
def learn_a_lesson():
    decision = input()
    while decision.lower() != "yes" and decision != "no":
        print("Invalid")
        print('The Nacho Reaper tell you to learn new lesson : Do you want to learn?')
        decision = input()
    if decision == "yes":
        print('The Nacho Reaper starts moving faster than you can see. He stops and looks to you: did you get all that?')

        decision = input()
        if decision == "No":
            print('well to bad im not doing it again')
    return decision
def goLeftOrRightDownTunnel():
    decision = input('Do you choose to walk to the left or right tunnel?')
    while decision.lower() != 'left' and decision != 'right':
        print('Invalid')
        decision = input('Do you choose to walk to the left or right tunnel?')
    if decision.lower() == 'left':
        print('You discover a tortilla chest full of nacho helmets and armor.')
        items.append("Nacho Armor")
        items[0].append(5)
        print("After collecting the Nacho Armor, you turn around and go back the way you came.")
    elif decision.lower() == 'right':
        print("You find a Cinnamon Twist Staff on a pedestal.")
        items.append("Cinnamon Staff")
        items[1].append(4)
        print("After collecting the Cinnamon Staff, you turn around and go back the way you came.")
    return decision
def helpNachoVillager():
    decision = input('Do you wish to help the villager find his coin?')
    while decision.lower() != 'yes' and decision != 'no':
        print('Invalid')
        decision = input('Do you wish to help the villager find his lost coin?')
    if decision.lower() == 'yes':
        print('The villager is appreciative for your help!')
        print('You both search eagerly for the coin.')
        print('PLEASE WAIT WHILE YOU SEARCH')
        time.sleep(15)
        print('You found it!')
        print('The villager gives you a golden Dorito necklace as a token of gratitude.')
        items.append('Dorito Necklace')
        items[2].append(6)
        print('You continure your journey.')
    elif: decision.lower() == 'no':
        print('You walk past the crying villager and continue your journey.')
        print('You find a wooden Dorito necklace on the cave floor.')
        items.append('Dorito Necklace')
        items[2].append(3)
#This is an RPG Game!
#Title Screen
items = [[],[]]
skill_points = 0
player_class = ""
player_name = ""
menuScreen()
time.sleep(1)
clear = lambda: os.system('cls')
clear()
option_title = get_menu_options()


if option_title == 'New Game':
    player_class = chooseClass()
    player_name = playerName(player_class)
    print("You're at the drive-thru at Taco Bell, when out of the blue you get cold nacho fries.")
    decision = eat_choice1()
    print('You have woken up in Nacho Hell and there are skeletons floating in a river of flaming cold nacho cheese')
    print('The Nacho Reaper presents you with the option to redeem yourself')
    decision = redeem_swim()
    print('The Nacho reaper tells you to Dance ChampetaChallenge : Do you want to')
    decision = dance_off()
    print('The Nacho Reaper tell you to learn new lesson : Do you want to learn?')
    decision = learn_a_lesson()
    print('I will teach you another way.')
    print('The Nacho Reaper points to two tunnels.')
    print('The left tunnel is glowing yellowish-orange.')
    print('The right tunnel is smells like cinnamon twists.')
    decision = goLeftOrRightDownTunnel()
    print('You are approached by a crying villager who needs help finding his lost coin.')
    decision = helpNachoVillager():
    


          
          

    

    

