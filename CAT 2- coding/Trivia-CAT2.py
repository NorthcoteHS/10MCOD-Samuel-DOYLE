"""
Name: Trivia-CAT2.py
Student: Samuel Doyle
Date: 09/05/18
Desc: This is a trivia game for the 2nd CAT in coding
"""
# greet the user
print('welcome to the trivia game')
# create a list of all the questions you wish to ask
questions = ['what is the capital of israel?', 'who is the prime minister of england?', 'what animal has the scientific name Dromaius novaehollandiae?', 'mossad is the intelligence agency for which country?', 'who is the current captain of the australian cricket team?']
# create a list of all the correct answers for your questions
answers = ['jerusalem', 'teresa may', 'the emu', 'israel', 'tim paine']
# create a for loop to pick a qustion for the user to answer and state wether the answer is correct or not
for i, question in enumerate(questions):
    print(question)
    input('answer?')
    print(answers[i])
    