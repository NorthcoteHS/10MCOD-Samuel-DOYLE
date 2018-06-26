"""
Name: CAT 3.py
Student: Samuel Doyle
Date: 06/06/18
Desc: This is my coding program for the third CAT of coding. This will help people revise for their tests/exams and offer websites to help them revise like mathspace or code academy etc.
"""
# import datetime and calendar and print welcome prompt to the user
import calendar, time, datetime
print("welcome to your personal calender and revision program")
print("today is", datetime.date.today().strftime("%A"))
print('the date is', datetime.date.today())
# get the user to input their tests
year = ["2018"]
month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
day = ['1', '2', '3', '4', '6', '7', '8', '9', '10', '11', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
tests = []
test = input('input your upcoming tests')
tests.append(test)
# ask the user if they would like to print out thier tests
print('you have', len(tests), 'tests coming up')
q = input('would you like to print these events out y/n?')
# create an if statement to respond to the users answer
if q == 'n':
    print('ok')
# create a second statment for a different response
elif q == 'y':
    print(tests)
    print('these are your upcoming tests')
    revision = ['https://mathspace.co/', 'https://bc.vitalsource.com/tenants/205753/books/LF9781488677328?bc_token=9b920a30-4f75-0136-d0ed-0a580a540026&relaunch_vbid=LF9781488677328&license_to=', 'https://bc.vitalsource.com/tenants/northcote_lti/books/LF9780190307950?bc_token=bb3875a0-4f75-0136-d0ed-0a580a540026&book_location=%2Fpage%2F324&relaunch_vbid=LF9780190307950']
revision2 = input('would you like to do revision y/n?')
if revision2 == 'y':
    print('these websites/books can help you with your revision')
    print(revision)
# if the user doesn't want to revise, print a prompt to shut thee program down if the user wishes
elif revision2 == 'n':
    print('ok')
    shutdown = input('are you sure you dont want to revise? y/n')
    if shutdown == 'y':
        print('goodbye for now')
    elif shutdown == 'n':
        print(revision)