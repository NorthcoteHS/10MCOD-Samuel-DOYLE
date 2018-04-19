"""
prog: calculator.py
date:14/03/18
name: calculator
desc: calculator
"""
# user inputs the first number
print('input number')
x = int(input(''))
# user picks second number
print('input number')
y = int(input(''))
# the user selects the sum they desire
print('select, * + - / ')
t = input('')
if t == '+':
    print(x+y)
elif t == '-':
      print(x-y)
elif t == '*':
      print(x*y)
elif t == '/':
      print(x/y)
