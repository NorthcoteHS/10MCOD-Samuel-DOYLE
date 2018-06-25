"""
Prog: Study Helper
Date: 14/6/18
Name: Liam Cust
Desc: A Progrom to help you identify what you need to laern better
"""
#Greeting and informative text
print ("Hello and welcome to Liam's easy study program")
answer = input ('Preset Subjects/Questions (P) or custom Subjects/Questions? (C) ')
#subject selection
if answer == 'P':
    print ('Northcote High yr 10 Moving and Reacting (press M)')
    print ('Northcote High yr 10 Politics and Pop Culture (press P)')
    print ('Northcote High yr 10 Adspeak (press A)')
    print ('Northcote High yr 10 Architecture (press R)')
    print ('Northcote High yr 10 Law and Moralitiy (press L)')
    subject = input ('Subject Choice: ')
    if subject == 'M': 
            print ('You have selected Northcote High yr 10 Moving and Reacting, to go back press B otherwise press C to continue ')
            cont = input ('Exit or Continue: ')               
            if cont == 'C':
                print ('These questions will help you identify what you need to learn more about')
#inport random number
                from random import randint
                number = (randint(0, 2))
                if number == 0:
                    print ('What does the u signify in SUVAT equations?')
                    print ('a) displacement')
                    print ('b) final velocity')
                    print ('c) initial velocity')
                    print ('d) acceleration')
                    MRQ1 = input ('Answer: ')
                    if MRQ1 == 'C' or MRQ1 == 'c': 
                        print ('correct')
                    else:
                            print ('Unlucky, Answer is acually initial velocity') 
                if number == 1:
                    print ('What is the periodic symbol for Oxygen?')
                    print ('a) Na')
                    print ('b) O')
                    print ('c) H')
                    print ('d) Ox')
                    MRQ1 = input ('Answer: ')
                    if MRQ1 == 'B' or MRQ1 == 'b': 
                        print ('correct')
                    else:
                            print ('Unlucky, Answer is acually O') 
                if number == 2:
                    print ('What does the t signify in SUVAT equations')
                    print ('a) acceleraion')
                    print ('b) displacement')
                    print ('c) final velocity')
                    print ('d) time')
                    MRQ1 = input ('Answer: ')
                    if MRQ1 == 'B' or MRQ1 == 'b': 
                        print ('correct')
                    else:
                            print ('Unlucky, Answer is acually O') 
                            number = (randint(0, 2))
                if number == 0:
                    print ('What does the u signify in SUVAT equations?')
                    print ('a) displacement')
                    print ('b) final velocity')
                    print ('c) initial velocity')
                    print ('d) acceleration')
                    MRQ1 = input ('Answer: ')
                    if MRQ1 == 'C' or MRQ1 == 'c': 
                        print ('correct')
                    else:
                            print ('Unlucky, Answer is acually initial velocity') 
                if number == 1:
                    print ('What is the periodic symbol for Oxygen?')
                    print ('a) Na')
                    print ('b) O')
                    print ('c) H')
                    print ('d) Ox')
                    MRQ1 = input ('Answer: ')
                    if MRQ1 == 'B' or MRQ1 == 'b': 
                        print ('correct')
                    else:
                            print ('Unlucky, Answer is acually O') 
                if number == 2:
                    print ('What does the t signify in SUVAT equations')
                    print ('a) acceleraion')
                    print ('b) displacement')
                    print ('c) final velocity')
                    print ('d) time')
                    MRQ1 = input ('Answer: ')
                    if MRQ1 == 'B' or MRQ1 == 'b': 
                        print ('correct')
                    else:
                            print ('Unlucky, Answer is acually O') 