hungry = 'no'

hungry = input('Do you know what to eat?')

while hungry == 'no':


    from random import randint
    number = (randint(0, 11))

    if number == 1:
        print('Do you feel like pizza? ')

    if number == 2:
        print('Do you feel like burger? ')

    if number == 3:
        print('Do you feel like soup? ')

    if number == 4:
        print('Do you feel like dumplings? ')

    if number == 5:
        print('Do you feel like nachos? ')

    if number == 6:
        print('Do you feel like souvlaki? ')

    if number == 7:
        print('Do you feel like indian? ')

    if number == 8:
        print('Do you feel like sushi?')

    if number == 9:
        print('Do you feel like pasta?')

    if number == 10:
        print('Do you feel like steak?')

    if number == 11:
        print('Do you feel like toast?')

    hungry = input('Yes or no?')

if hungry == 'yes':
    print('Enjoy your meal!')
    
else:
    print('Invalid message')
