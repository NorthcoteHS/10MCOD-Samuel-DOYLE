"""
Prog:   userInfo.py
Name:   Samuel doyle
Date:   18/04/18
Desc:   Asks the user for their name, address, etc.
"""

# Display welcome message.
print('Welcome to the User Information Booth! Please enter your info.')

# Get user's name.
name = input('First Name: ')
surname = input('Last Name: ')

# Get user's birth date.
yob = input('Birth Year: ')
mob = input('Birth Month: ')
dob = input('Birth Day: ')

# Get user's favourites.
red = input('Favourite colour: ')
song = input('Favourite song: ')
sport = input('Favourite sport: ')

# Display exit message.
print('Thank you, your information has been saved.')
