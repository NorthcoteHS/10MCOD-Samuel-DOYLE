"""
Prog: Game Finder
Name: Simon Lo
Date: 6/6/2018
Desc: This is to help gamers to find games they want easily
"""
#Welcoming the guest to the program
print ('Welcome, this program will help you find games you want.')
#choosing the list to find the games they might like
print ('Choose from the catalogue')
print ('Genre, Rating or Top games')
#listing of the options
options = ['Genre', 'genre','Rating','rating', 'Top games', 'top games']
#list of gernes 
genre = ['Action', 'Adventure', 'Puzzle','RPG'] or ['action', 'adventure', 'puzzle', 'rpg']
#rating from 1-10
rating = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#options depending on the choice
a = input ("")
if a == 'Genre' or a == 'genre':
    print (genre)
#These are games for the action side
    b = input ("")
    if b == 'Action' or b == 'action':
        print ("These are the game you would like:")
        print ('Overwatch, Rainbow 6 siege, pong')
#These are games for the adventure side
    elif b == 'Adventure' or b == 'adventure':
        print ('These are the games you would like:')
        print ('Minecraft, Undertale, Terraria')
    elif b == 'Puzzle' or b == 'puzzle':
        print ('These are the games you would like:')
        print ('portal 2, portal, minesweeper')
    elif b == 'RPG' or b == 'rpg':
        print ('These are the games you would like:')
        print ('world of warcraft, Undertale, borderlands 2')
#These are games for the rating side
elif a == 'Rating' or a == 'rating':
    print (rating)
    c = input ("")
    if c == '1' or c == '2' or c == '3' or c == '4' or c == '5':
        print ('These are the games you like:')
        print ('snakes')
    elif c == '6' or c == '7' or c == '8' or c == '9' or c == '10':
        print ('These are the games you like:')
        print ('portals/portals 2')
#These are the top games 
elif a == 'Top games' or a == 'top games':
    print ('These are the top games')
    print ('overwatch, fortnite, mincraft')
#farewell message to the user and saying thank you to the user
print ('Thank you and enjoy the games :)')
