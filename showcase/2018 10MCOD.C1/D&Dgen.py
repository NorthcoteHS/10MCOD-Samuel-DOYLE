"""
Prog: D&Dgen.py
name: Vincent
Date of start: 6/6
Desc: generates a D&D character
"""
def character(): #this is the function that creates the characters name
    namecap = random.randint(65, 90) #this generates the first capital letter of the name using ACII
    combine = [] #a blank list for the combination
    first = chr(namecap) #turns the number into a letter
    for i in range (5, random.randint(7, 11)): #picks a random length of the name
        name = random.randint(97, 122)
        second = chr(name)
        combine.append(second)
    letters = (''.join(combine)) #joins the name
    global finalname #makes the final name a global variable so it can be refernced later on
    finalname = (first + letters)
    print (finalname)
#break
def repeat(): #this is here so that if you dont like the name you can run it again
    yn = input ("do you like this name? ")
    if yn == 'no':
        character()
        repeat()
    elif yn == 'yes':
        return
    else:
        print ("something was wrong with your input") #in case you mistype
        repeat()
        return
#break
import random
choice = ['barbarian', 'bard', 'fighter', 'wizard', 'N'] #these are your class choices, I should really move them
yourcantrips = [] #another blank list that sould be moved, this is used later on for the classes
#break
namechoose = input("Do you want to generate a name? type 'yes' or 'no' ") #asks if you want to generate the name
if namechoose == 'yes':
    character() #runs the function character()
    print ("this name is subject to change, you can consider it like an anagram and rearrange letters") #since you get alot of stupid names.
    repeat(); #runs the repeat() function
elif namechoose == 'no':
    finalname = input("What is your name? ") #user inputs name and saves it to finalname
else:
    print ("something was wrong with your input")
    def blah(): #I couldn't think of a name
        #This was annoying, for some reason I couldn't assign 'finalname' as a global just in general, I had to to do it in each function, which is annoying.
        global finalname
        ooft = input ("do you want to generate the name ")
        if ooft == 'yes':
         character()
         repeat()
        elif ooft == 'no':
            finalname = input("What is your name? ")
        else:
            blah() #repeats the process
    blah()
        
#break
race = ['halfling', 'human', 'tiefling', 'N'] #possible races
print ("these are your race choices ")
print (race)
def racing():
    global racechoice #making these variables global so they can be used later
    racechoice = input("now Pick a race, type [N] for random ")
    global size
    global attribute
    global speed
    global skills
    while racechoice in race: #makes sure its a viable choice
            if racechoice == 'tiefling': #these are all just quirks of a race, dont really affect anything accept at the very end
                size = ('medium')
                attribute = ['10str', '10con','10dex', '11int', '10wis', '12cha']
                speed = ('30ft')
                skills = ['Darkvision', 'Fire Resistance', 'Thaumaturgy']
                return
            elif racechoice == 'human':
                size = ('medium')
                attribute = ['11str', '11con', '11dex', '11int', '11wis', '11cha']
                speed = ('30ft')
                skills = []
                return
            elif racechoice == 'halfling':
                size = ('small')
                attribute = ['10str', '10con','12dex', '10int', '10wis', '10cha']
                speed = ('25ft')
                skills = ['Lucky', 'Brave', 'Halfling Nimbleness']
                return
            elif racechoice == 'N':
                nyooh = random.randint(0, 3) #picks a random race
                racechoice = race[nyooh]
    if racechoice not in race:
        print ("something went wrong with your input")
        racing() #repeats the process if the input doesn't match
racing()
#break
print ("these are your class choices")
print (choice)
#The function that picks your class
def classees():
    classes = input ("now pick a class, type [N] for a random one ")
    #make sure the input is a viable class
    while classes in choice:
        if classes == 'barbarian':
            #list all possible weapons, abilities and spells (whenn you need to)
            weapon = ['spear', 'sickle', 'mace', 'light hammer', 'javelin', 'handaxe', 'great club', 'dagger', 'club', 'quarterstaff', 'Flail', 'Glaive', 'Greataxe', 'Greatsword', 'Halberd', 'Lance', 'Longsword', 'Maul', 'Morningstar', 'Pike', 'Rapier', 'Scimitar', 'Shortsword', 'Trident', 'War Pick', 'Warhammer','Whip',]	
            abilities = ['Rage', 'Unarmoured defense']
            health =  str(12 + 10) #health
            styles = []
            break
        elif classes == 'bard':
            weapon = ['spear', 'sickle', 'mace', 'light hammer', 'javelin', 'handaxe', 'great club', 'dagger', 'club', 'quarterstaff', 'light crossbow']
            abilities = ['bardic inspiration']
            health = str(8 + 10)
            #these are your spells
            cantrip = ['Dancing Lights', 'Light', 'Mage Hand', 'Mending', 'Message', 'Minor Illusion', 'Prestidigitation', 'True Strike', 'Vicious Mockery']
            onelv = ['Animal Friendship', 'Bane' , 'Charm Person', 'Comprehend Languages', 'Cure Wounds', 'Detect Magic' ,'Disguise Self', 'Faerie Fire', 'Feather Fall', 'Healing Word', 'Heroism' , 'Hideous Laughter' , 'Identify', 'Illusory Script', 'Longstrider', 'Silent Image', 'Sleep', 'Speak with Animals', 'Thunderwave', 'Unseen Servant']
            styles = []
            for item in range(2): #how many spells you have
                spell = random.randint (0, len(cantrip)) #picks a random number from within the length of the possible cantrips
                spell = (spell - 1) #makes sure the index isnt out of range
                cantrips = cantrip[spell] #uses the random number to generate a random spell
                yourcantrips.append (cantrips)
            for item in range(2):
                spell = random.randint (0, len(onelv))
                spell = spell - 1
                spells = onelv[spell]
                yourcantrips.clear
                yourcantrips.append(spells)
            break
        elif classes == 'fighter':
                weapon = ['spear', 'sickle', 'mace', 'light hammer', 'javelin', 'handaxe', 'great club', 'dagger', 'club', 'quarterstaff', 'Flail', 'Glaive', 'Greataxe', 'Greatsword', 'Halberd', 'Lance', 'Longsword', 'Maul', 'Morningstar', 'Pike', 'Rapier', 'Scimitar', 'Shortsword', 'Trident', 'War Pick', 'Warhammer','Whip',] 
                abilities = ['Fighting Style', 'Second Wind']
                health = str(12 + 10)
                styles = ['Archery', 'Defense', 'Deueling', 'Great weapon fighting', 'Protection', 'Two-Weapon Fighting']
                style = random.randint (0, len(styles))
                style = (style - 1)
                yourstyle = styles[style]
                yourcantrips.append(yourstyle) # used the same variable for spells since it saves space and works since fighters dont have spells at lv1
                break
        elif classes == 'wizard':
            weapon = ['daggers, darts, slings, quarterstaffs, light crossbow']
            abilities = ['Spellcasting', 'Arcane Recovery']
            cantrip = ['Acid splash', 'Chill touch','Dancing Lights', 'Light', 'Mage Hand', 'Mending', 'Message', 'Minor Illusion', 'Prestidigitation', 'True Strike', 'Fire Bolt', 'Poison spray', 'Ray of Frost', 'Shocking Grasp']
            onelv = ['Alarm', 'Burning hands', 'charm person', 'colour spray', 'comprehend questions', 'detect magic', 'disguise self', 'expeditious retreat', 'false life', 'feather fall', 'find familiar', 'floating disk', 'fog cloud', 'grease', 'hideous laughter', 'identify', 'illusory script', 'jump', 'longstrider', 'mage armor', 'magic missile', 'protection from evil and good', 'shield', 'silent image', 'sleep', 'thunderwave', 'unseen servant']
            health = str(6 + 10)
            styles = []
            for item in range(3):
                spell = random.randint (0, len(cantrip))
                spell = (spell - 1)
                cantrips = cantrip[spell]
                yourcantrips.append (cantrips)
            for item in range(2):
                spell = random.randint (0, len(onelv))
                spell = spell -1 
                spells = onelv[spell]
                yourcantrips.clear
                yourcantrips.append(spells)
            break
        elif classes == 'N':
            epicnyooh = random.randint (0, 4) #picks a random class
            classes = choice[epicnyooh]
    if classes not in choice:
        print ('something went wrong with your input')
        classees() #repeats process if something goes wrong
    print ("")
    print ("")
    print ("") # this is the character sheet, lists all the info
    print ("")
    print ("")
    print ("")
    print ("")
    global finalname
    print ("your character is ")
    print ("name: " + finalname) #character name
    print ("")
    print ('Your race is: ' + racechoice) #all the race info
    print ("you are " + size + " size")
    print ( speed + " walking speed")
    print ('your stats are')
    print (attribute)
    print ('your skills are')
    print (skills)
    print ("")
    print ('you are a') #class info
    print (classes)
    print ('Your weapon choices are')
    print (weapon)
    print ("")
    print ("your abilities are")
    print (abilities)
    print ('your spells/fighting style are')
    print (yourcantrips)
#break
classees()
"""
problems i had:
When choosing cantrips, It would constantly say my index was out range. I got unlucky and never picked a number within the range
My repeat function didnt work, so if you said yes to genrating a name, you would never be able to leave
It would ask you twice if what class to pick.
those most of the major ones. So major that my two beta tests simply didnt work. Most of the other problems were just basic things that I could fix with a indent here and a extra letter there.

"""
