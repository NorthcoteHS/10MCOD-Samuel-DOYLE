"""
Prog:   3DPrinterMenu.py
Name:   Tom Poletti
Date:   2018/06/10
Desc:   An intuitive and easy to use 3D Printer menu
"""

import time
import random

printer = 1

num = list(range(1, 5))
idleTemp = list(range(20, 30))

extSet = 0
bedSet = 0

while printer == 1:
    extTemp = (random.choice(idleTemp))
    bedTemp = (random.choice(idleTemp))

    print('1. Print From SD')
    print('2. Printer Adjust')
    print()
    print('Extruder:', extTemp, '/', extSet)
    print('Bed:', bedTemp, '/', bedSet)
    print()
    user1 = input()

    if user1 == '1':
        print('Select File...')
        print('1. Calibration Cube')
        print('2. 3D Benchy')
        print('3. Marvin')
        print()
        user2 = input() 
        
        print('Printing ')
    elif user1 == '2':
        print('1. Position')
        print('2. Temperature') 
        print('3. Filament Loading')
        print('4. Fan Speed')
        print('5. Jerk & Acceleration')
        print('6. Printer Statistics')
        print('7. EEPROM')
        print()
        user3 = input()
    else:
        print('Invalid Input')
        print()
