"""
name= classRoll.py
student= samuel doyle
date= 02/05/18
desc= class roll task for lists
"""
# import random
import random
# create a list titled roll and add the names of the students
roll = ['jessica', 'emily', 'jordan', 'kayley', 'bruce', 'michael', 'everett', 'lisa', 'sam', 'noah']
# create a variable cleaner and  print the 3rd person on the list
cleaner = roll[2]
print('the cleaner is', cleaner)
# create a variable called enrolment and give it the value of the roll length
enrolment = len(roll)
# add a new student james to the roll
roll.append('james')
# remove james from the roll
del roll[2]
# change micheals name to mike
roll[5] = 'mike'
# alphabatise the roll and then reverse it
list.sort(roll)
list.reverse(roll)
# print a random name from the roll
print(random.choice(roll))
# create two rolls with 1/2 the students in one roll and 1/2 on the other
half1 = roll[0:5]
half2 = roll[6:10]
