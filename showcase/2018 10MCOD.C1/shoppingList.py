print('This is a program that helps you to build a reasonable shopping list. Answer the following questions and this program will tell you what to buy with your budget.')
a=input('What is the first thing you want to buy? ')
price1=int(input('How much is it? (You only need to input an integer) '))
b=input('What is the second thing you want to buy? ')
price2=int(input('How much is it? (You only need to input an integer) '))
c=input('What is the third thing you want to buy? ')
price3=int(input('How much is it? (You only need to input an integer) '))
print("If you don't want to buy anything more, answer '0' for the next questions")
d=input('What is the fourth thing you want to buy? ')
price4=int(input('How much is it? (You only need to input an integer )'))
e=input('What is the fifth thing you want to buy? ')
price5=int(input('How much is it? (You only need to input an integer) '))
budget=int(input('What is your budget? (You only need to input an integer) '))
one=budget-price1
two=one-price2
three=two-price3
four=three-price4
five=four-price5
if one>=0:
    if two>=0:
        if three>=0:
            if four>=0:
                if five>=0:
                    print('You can buy',a+',',b+',',c+',',d+',','and',e+'.','Your budget left is',str(five)+".")
                else:
                    print('You can buy',a+',',b+',',c,'and',d+'.','Your budget left is',str(four)+".")
            else:
                print('You can buy',a+',',b,'and',c+'.','Your budget left is',str(three)+".")
        else:
            print('You can buy',a,'and',b+'.','Your budget left is',str(two)+".")
    else:
        print('You can buy',a+'.','Your budget left is',str(one)+".")
else:
    print('What you want to buy is beyond your budget.')
print('Follow the instructions and spend your money wisely. You are doing great!')
