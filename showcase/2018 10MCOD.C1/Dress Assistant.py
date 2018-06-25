
"""
Prog: Dress Assistant
Name: Isabella Holloway
Date: 06/05/18
Desc: Helps those with a colour deficiency to pick out the best outfit based on colour and accessories.
"""
import time
t = 3
import random
loop = ("yes")

#Introduce the program and ask first prompt. Create while loop to restart program at the end. 
print("Welcome to the dress assistant, created to help those who are colourblind pick out the best outfit!")
print( ) 
time.sleep(t)
print("To use this programme I highly recommend having all clothes, shoes and accessories labeled with what colour they are. This ensures you will get the most use and understanding out of this programme ")
print( )
time.sleep(t)
while loop == "yes":
    top = input("I am going to calculate your perfect outfit for the day! Please enter the colour shirt or blouse you feel like wearing today... ")
    top = top.lower()
    print( )
#List of possible simple responces to first prompt. All are designed to work together in terms of colour combinations. By answering the first prompt about the top, it will generate coloured pants/skirt and shoes.
#Shoes are only very basic colours.
    if top == "red":
        print("Sounds great! According to my calculations you could wear BLUE, BROWN, GREEN or WHITE pants or skirt to match. Choose one of the suggestions and input that into the next question ")
        print( )
        time.sleep(t)
        pants = input("What colour pants or skirt did you choose? ")
        pants = pants.lower()
        print( )
        if pants == "blue":
            print("Looking good! I've thought about your choices and decided that the best coloured shoes to wear with this combination would be WHITE or BROWN. ")
        if pants == "brown":
            print("Stunning! Finish the look off with a pair of either BLACK or WHITE shoes. ")
        if pants == "green":
            print("Nice. Can't leave without shoes! I suggest you wear a pair of either BROWN, BLACK or WHITE shoes. ")
        if pants == "white":
            print("Looking very festive! Don't forget some shoes. You should wear a pair of either BLACK, BROWN or WHITE shoes to complete. ")
        print( )
        time.sleep(t)
        accessory = input("Would you like to add some accessories? Please type 'yes' or 'no' ")
        accessory = accessory.lower()
            
    if top == "yellow":
        print("Sounds great! According to our calcualtions you could wear BLUE, BLACK or WHITE pants or skirt. Choose one of the suggestions and input that into the next question ")
        print( )
        time.sleep(t)
        pants = input("What colour pants or skirt did you choose? ")
        pants = pants.lower()
        if pants == "blue":
            print("Looking good! I've thought about your choices and decided that the best coloured shoes to wear with this combination would be WHITE or BROWN.")
        if pants == "black":
            print("Stunning! Finish the look off with a pair of either BLACK, BROWN or WHITE shoes.")
        if pants == "white":
            print("Nice. Can't leave without shoes! I suggest you wear a pair of either BROWN, BLACK or WHITE shoes.")
        print ( )
        time.sleep(t)
        accessory = input("Would you like to add some accessories? Please type 'yes' or 'no' ")
        accessory = accessory.lower()

    if top == "green":
        print("Sounds great! According to our calcualtions you could wear BLUE, BLACK, BROWN or WHITE pants or skirt. Choose one of the suggestions and input that into the next question ")
        top = top.lower()
        print( )
        pants = input("What colour pants or skirt did you choose? ")
        pants = pants.lower()
        print( )
        time.sleep(t)
        if pants == "blue":
            print("Looking good! I've thought about your choices and decided that the best coloured shoes to wear with this combination would be WHITE or BROWN. ")
        if pants == "black":
            print("Stunning! Finish the look off with a pair of either BLACK, BROWN or WHITE shoes. ")
        if pants == "brown":
            print("Nice. Can't leave without shoes! I suggest you wear a pair of either BLACK or WHITE shoes. ")
        if pants == "white":
            print("Looking very festive! Don't forget some shoes. You should wear a pair of either BLACK, BROWN or WHITE shoes to complete.")
        print( )
        time.sleep(t)
        accessory = input("Would you like to add some accessories? Please type 'yes' or 'no' ")
        accessory = accessory.lower()
        

    if top == "blue":
        print("Sounds great! According to our calcualtions you could wear BROWN or WHITE pants or skirt. Choose one of the suggestions and input that into the next question ")
        print( )
        time.sleep(t)
        pants = input("What colour pants or skirt did you choose? ")
        pants = pants.lower()
        print( )
        if pants == "brown":
            print("Looking good! I've thought about your choices and decided that the best coloured shoes to wear with this combination would be WHITE or BLACK. ")
        if pants == "white":
            print("Stunning! Finish the look off with a pair of either BLACK, BROWN or WHITE shoes. ")
        print( )
        time.sleep(t)
        accessory = input("Would you like to add some accessories? Please type 'yes' or 'no' ")
        accessory = accessory.lower()
            
    if top == "pink":
        print("Sounds great! According to our calcualtions you could wear RED, BLUE, BROWN, BLACK or WHITE pants or skirt. Choose one of the suggestions and input that into the next question ")
        print ( )
        time.sleep(t)
        pants = input("What colour pants or skirt did you choose? ")
        pants = pants.lower()
        print( )
        if pants == "red":
            print("Looking good! I've thought about your choices and decided that the best coloured shoes to wear with this combination would be BLACK, WHITE or BROWN. ")
        if pants == "blue":
            print("Stunning! Finish the look off with a pair of either BROWN or WHITE shoes. ")
        if pants == "brown":
            print("Nice. Can't leave without shoes! We suggest you wear a pair of either BLACK or WHITE shoes. ")
        if pants == "black":
            print("That looks great! complete this look with a pair of BROWN, BLACK or WHITE shoes. ")
        if pants == "white":
            print("Looking very festive! Don't forget some shoes. You should wear a pair of either BLACK, BROWN or WHITE shoes to complete.")
        print( )
        time.sleep(t)
        accessory = input("Would you like to add some accessories? Please type 'yes' or 'no' ")
        accessory = accessory.lower()

    if top == "black":
        print("Sounds great! According to our calcualtions you could wear RED, YELLOW, GREEN, PINK, BROWN, BLACK or WHITE pants or skirt. Choose one of the suggestions and input that into the next question ")
        print( )
        time.sleep(t)
        pants = input("What colour pants or skirt did you choose? ")
        pants = pants.lower()
        print( )
        if pants == "red":
            print("Looking good! I've thought about your choices and decided that the best coloured shoes to wear with this combination would be BROWN, BLACK or WHITE. ")
        if pants == "yellow":
            print("Stunning! Finish the look off with a pair of either BROWN or BLACK shoes. ")            
        if pants == "green":
            print("Nice. Can't leave without shoes! We suggest you wear a pair of either BROWN, BLACK or WHITE shoes. ")
        if pants == "pink":
            print("That looks great! complete this look with a pair of BROWN, BLACK or WHITE shoes. ")
        if pants == "brown":
            print("Fantastic. You should wear a pair of either BLACK or WHITE shoes ")
        if pants == "black":
            print("Looking good! I've thought about your choices and decided that the best coloured shoes to wear with this combination would be BROWN, BLACK or WHITE. ")
        if pants == "white":
            print("That looks great! complete this look with a pair of BROWN, BLACK or WHITE shoes. ")
        print( )
        accessory = input("Would you like to add some accessories? Please type 'yes' or 'no' ")
        accessory = accessory.lower()

    if top == "white":
        print("Sounds great! According to our calcualtions you could wear RED, YELLOW, GREEN, BLUE, PINK, BROWN, BLACK or WHITE pants or skirt. Choose one of the suggestions and input that into the next question ")
        print( )
        time.sleep(t)
        pants = input("What colour pants or skirt did you choose? ")
        pants = pants.lower()
        print( )
        if pants == "red":
            print("Looking good! I've thought about your choices and decided that the best coloured shoes to wear with this combination would be BROWN, BLACK or WHITE. ")
        if pants == "yellow":
            print("Stunning! Finish the look off with a pair of either BROWN or BLACK shoes. ")            
        if pants == "green":
            print("Nice. Can't leave without shoes! We suggest you wear a pair of either BROWN, BLACK or WHITE shoes. ")
        if pants == "blue":
            print("Looking good! I've thought about your choices and decided that the best coloured shoes to wear with this combination would be BROWN or WHITE. ")
        if pants == "pink":
            print("That looks great! complete this look with a pair of BROWN, BLACK or WHITE shoes. ")
        if pants == "brown":
            print("Fantastic. You should wear a pair of either BLACK or WHITE shoes ")
        if pants == "black":
            print("Looking good! I've thought about your choices and decided that the best coloured shoes to wear with this combination would be BROWN, BLACK or WHITE. ")
        if pants == "white":
            print("That looks great! complete this look with a pair of BROWN, BLACK or WHITE shoes. ")
        print( )
        time.sleep(t)
        accessory = input("Would you like to add some accessories? Please type 'yes' or 'no' ")
        accessory = accessory.lower()

    if top == "brown":
        print("Sounds great! According to our calcualtions you could wear RED PINK or WHITE pants or skirt. Choose one of the suggestions and input that into the next question ")
        print( )
        time.sleep(t)
        pants = input("What colour pants or skirt did you choose? Choose one of the suggestions and input that into the next question ")
        pants = pants.lower()
        print( )
        if pants == "red":
            print("Looking good! I've thought about your choices and decided that the best coloured shoes to wear with this combination would be BROWN, BLACK or WHITE. ")    
        if pants == "pink":
            print("That looks great! complete this look with a pair of BROWN, BLACK or WHITE shoes. ")
        if pants == "white":
            print("That looks great! complete this look with a pair of BROWN, BLACK or WHITE shoes. ")
        print( )
        time.sleep(t)
        accessory = input("Would you like to add some accessories? Please type 'yes' or 'no' ")
        accessory = accessory.lower()

#The program will now create a suggestion of accessories based on the colour of the users top. This uses all the colour combinations previously creted to match accessories to the coloured outfits.
#Accessories are fror males and females. 
    if accessory == "yes":

        print( )
        print("You look amazing, lets finish this look off and give it a bit more 'WOW!' ")
        print( )
        time.sleep(t)
        accessory = input("Just remind me what color your shirt or blouse is and i'll give you some accessories to choose from... ")
        accessory = accessory.lower()
        print( )
        if accessory == "red":
            print("Good choice! You could wear a WHITE necklace, a PINK bracelet, a BROWN belt or a BLACK bag")
        if accessory == "yellow":
            print("Your going to look great. You could wear a BROWN hat, WHITE clutch or bag, GREEN earrings or a BLACK belt")
        if accessory == "green":
            print(" Oh fancy! You could wear a BROWN bag, PINK earrings, BLUE necklace or a BLACK bag") 
        if accessory == "blue":
            print("Nice! You could wear a PINK clutch or bag, RED belt or a WHITE tie")
        if accessory == "pink":
            print("Pretty in pink! You could wear a BROWN clutch or bag, WHITE necklace, BLACK sunnies or a BLUE tie")
        if accessory == "black":
            print("Looking good, You could wear a PINK necklace, a BLACK tie, BROWN bag or a RED bracelet")
        if accessory == "brown":
            print("Sounds great! You could wear a WHITE necklace, a PINK bag or clutch or a BLACK belt")
        if accessory == "white":
            print("Looking sharp! You could wear a BLACK necklace, a BROWN belt, a YELLOW tie or a PINK bracelet")
        print( )

    time.sleep(t)
    loop = input("Would you like to go back to the start of the programme? Please type 'yes' or 'no' ")
    loop = loop.lower()
    print( )
    
    
    if loop == "no":
        print("Thank you for using the dress assistant. I hope you love your outfit!")
              
