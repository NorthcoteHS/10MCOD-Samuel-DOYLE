"""
Prog: wordGeneratingApp
Name: Suzie Wang
Date: 14-6-2018
Desc: An app that can help user find the right word for their essay or persuasive or creative writing piece, by generating words from various categories.
"""

import random

#Defining mainMenu, this will make it easier to direct user back to main menu
def mainMenu():
    MMcatergories = input("""Main Menu:
    1. Essay Writing
    2. Persuasive Writing
    3. Creative Writing""")
    if MMcatergories == '1':
        EWcatergories()
    elif MMcatergories == '2':
        PWcatergories()
    else:
        CWcatergories()
#Defining EWcategories, allowing user to pick which categories of words they want
def EWcatergories():
    ewcatergories = input("""Essay Writing Catergories:
    1. Attribution
    2. Endorsement
    3. Conjunctions
    4. Modality
    5. Evaluation""")
    if ewcatergories == '1':
        print(ewattribution[random.randint(0,6)])
    if ewcatergories == '2':
        print(ewendorsement(0,7))
    if ewcatergories == '3':
        print(ewconjunctions(0,4))
    if ewcatergories == '4':
        print(ewmodality(0,7))
    elif ewcatergories == '5':
        print(ewevaluation(0,4))
#Making lists of words for each category within the essay writing section    
ewattribution = ['According to ___', '___argues(that)', '___discusses', '___states(that)', '___shows(that)', '___demonstrates', '___suggests(that)']

ewendorsement = ['reports', 'states', 'illustrates', 'shows', 'affirms', 'stresses', 'claims', 'assumes']

ewconjunctions = ['likewise', 'additionally', 'not only', 'however', 'even so']

ewmodality = ['could', 'must', 'possibly', 'clearly', 'in fact', 'generally', 'appears', 'hardly']

ewevaluation = ['important', 'significant', 'major', 'unrealistic', 'biased']
#Defining PWcategories, allowing user to pick which categories of words they want
def PWcategories():
    pwcategories = input("""Persuasive Writing
    1. To Illustrate a Point
    2. To Introduce an Example
    3. To Make Suggestions
    4. To Transition Between Information
    5. To Contrast Points
    6. For Conclusions and Summarizing
    """)
    if pwcategories == '1':
        print(pwillustrate(0,6))
    if pwcategories == '2':
        print(pwintroduce(0,5))
    if pwcategories == '3':
        print(pwsuggest(0,3))
    if pwcategories == '4':
        print(pwtransition(0,9))
    if pwcategories == '5':
        print(pwcontrast(0,7))
    if pwcategories == '6':
        print(pwconclusions(0,9))
#Making lists of words for each category within the persuasive writing section     
pwillustrate = ['for instance', 'for example', 'specifically', 'in particular', 'namely', 'such as', 'like']

pwintroduce = ['for example', 'thus', 'as an example', 'in the instance of', 'in other words', 'to illustrate']

pwsuggest = ['to this end', 'keeping this in mind', 'for this purpose', 'therefore']

pwtransition = ['also', 'furthermore', 'additionally', 'besides that', 'equally as important', 'similarly', 'likewise', 'as a result', 'otherwise', 'however']

pwcontrast = ['on the other hand', 'nevertheless', 'despite', 'in spite of', 'yet', 'conversely', 'instead', 'by the same token']

pwconclusions = ['with this in mind', 'as a result of', 'because of this', 'for this reason', 'so', 'due to', 'since', 'finally', 'in short', 'in conclusion']
#Defining CWcategories, allowing user to pick which categories of words they want
def CWcategories():
    cwcategories = input("""Creative Writing
    1. Adjectives
    2. Adverbs""")
    if cwcategories == '1':
        print(cwadjectives(0,17))
    if cwcategories == '2':
        print(cwadverbs(0,15))
#Making lists of words for each category within the creative writing section 
cwadjectives = ['acclaimed', 'accomplished', 'composed', 'concerned', 'concrete', 'conventional', 'demanding', 'focused', 'grim', 'intelligent', 'intrepid', 'jubilant', 'keen', 'mediocre', 'ornate', 'practical', 'precious', 'questionable']

cwadverbs = ['apathetically', 'assertively', 'begrudgingly', 'blissfully', 'dutifully', 'eagerly', 'faintly', 'frivolously', 'hastily', 'meagerly', 'methodically', 'neglectfully', 'normally', 'rashly', 'tactfully', 'tragically']
#Defining receiveRecommendation function
def receiveRecommendation():
    answer = input('Would you like a word recommendation? ')
    if answer == 'yes':
        mainMenu()
    else:
            print('Ok, ciao')        

receiveRecommendation()
