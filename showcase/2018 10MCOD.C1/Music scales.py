'''
Prog:   Music scales CAT3.py
Name:   Daniel Mandy  
Date:   6/6/2018
Desc:   shows the user the notes in a particular scale
'''
C = 1
Db = 2
D = 3
Eb = 4
E = 5
F = 6
Gb = 7
G = 8
Ab = 9
A = 10
Bb = 11
B = 12

C = int(C)
Db = int(Db)
D = int(D)
Eb = int(Eb)
E = int(E)
F = int(F)
Gb = int(Gb)
G = int(G)
Ab = int(Ab)
A = int(A)
Bb = int(Bb)
B = int(B)

note1 = 'z'
note2 = 'z'
note3 = 'z'
note4 = 'z'
note5 = 'z'
note6 = 'z'
note7 = 'z'
scaletype = 'major'

scaletype = input('Please enter a type of scale(major, minor, harmonicminor, blues): ')
startnote = input('Please enter the starting note(use flats only No sharps eg Db or Bb): ')

key = startnote


if key == 'C':
    key = 1
    
if key == 'Db':
    key = 2
    
if key == 'D':
    key = 3
    
if key == 'Eb':
    key = 4
    
if key == 'E':
    key = 5
    
if key == 'F':
    key = 6
    
if key == 'Gb':
    key = 7
    
if key == 'G':
    key = 8
    
if key == 'Ab':
    key = 9
    
if key == 'A':
    key = 10
    
if key == 'Bb':
    key = 11
    
if key == 'B':
    key = 12
    
if scaletype == 'major':
    note1 = key
    

    if note1 == 1:
        note1 = 'C'
        note2 = 'D'
        note3 = 'E'
        note4 = 'F'
        note5 = 'G'
        note6 = 'A'
        note7 = 'B'
    
    if note1 == 2:
        note1 = 'Db'
        note2 = 'Eb'
        note3 = 'F'
        note4 = 'Gb'
        note5 = 'Ab'
        note6 = 'Bb'
        note7 = 'C'
    
    if note1 == 3:
        note1 = 'D'
        note2 = 'E'
        note3 = 'Gb'
        note4 = 'G'
        note5 = 'A'
        note6 = 'B'
        note7 = 'Db'
    
    if note1 == 4:
        note1 = 'Eb'
        note2 = 'F'
        note3 = 'G'
        note4 = 'Ab'
        note5 = 'Bb'
        note6 = 'C'
        note7 = 'D'
    
    if note1 == 5:
        note1 = 'E'
        note2 = 'Gb'
        note3 = 'Ab'
        note4 = 'A'
        note5 = 'B'
        note6 = 'Db'
        note7 = 'Eb'
    
    if note1 == 6:
        note1 = 'F'
        note2 = 'G'
        note3 = 'A'
        note4 = 'Bb'
        note5 = 'C'
        note6 = 'D'
        note7 = 'E'
    
    if note1 == 7:
        note1 = 'Gb'
        note2 = 'Ab'
        note3 = 'Bb'
        note4 = 'B'
        note5 = 'Db'
        note6 = 'Eb'
        note7 = 'F'
        
    if note1 == 8:
        note1 = 'G'
        note2 = 'A'
        note3 = 'B'
        note4 = 'C'
        note5 = 'D'
        note6 = 'E'
        note7 = 'Gb'
        
    if note1 == 9:
        note1 = 'Ab'
        note2 = 'Bb'
        note3 = 'C'
        note4 = 'Db'
        note5 = 'Eb'
        note6 = 'F'
        note7 = 'G'
        
    
    if note1 == 10:
        note1 = 'A'
        note2 = 'B'
        note3 = 'Db'
        note4 = 'E'
        note5 = 'F'
        note6 = 'Gb'
        note7 = 'Ab'
        
    
    if note1 == 11:
        note1 = 'Bb'
        note2 = 'C'
        note3 = 'D'
        note4 = 'Eb'
        note5 = 'F'
        note6 = 'G'
        note7 = 'A'
    
    if note1 == 12:
        note1 = 'B'
        note2 = 'Db'
        note3 = 'Eb'
        note4 = 'E'
        note5 = 'Gb'
        note6 = 'Ab'
        note7 = 'Bb'
        
        
    print(note1, note2, note3, note4, note5, note6, note7, note1)
    
if scaletype == 'minor':
    note1 = startnote
    
    note = (key+2)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note ==9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
        
    note2 = note
    
    note = (key+3)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note3 = note
    
    note = (key+5)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note4 = note
    
    note = (key+7)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note5 = note
    
    note = (key+8)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note6 = note
    
    note = (key+10)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note7 = note
    print(note1, note2, note3, note4, note5, note6, note7, note1)
    
if scaletype == 'harmonicminor':
    note1 = startnote
    
    note = (key+2)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note ==9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
        
    note2 = note
    
    note = (key+3)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note3 = note
    
    note = (key+5)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note4 = note
    
    note = (key+7)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note5 = note
    
    note = (key+8)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note6 = note
    
    note = (key+11)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note7 = note
    print(note1, note2, note3, note4, note5, note6, note7, note1)
    
if scaletype == 'blues':
    note1 = startnote
    
    note = (key+3)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note ==9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
        
    note2 = note
    
    note = (key+5)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note3 = note
    
    note = (key+6)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note4 = note
    
    note = (key+7)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note5 = note
    
    note = (key+10)
    if note > 12:
        note = (note-12)
    if note == 1:
        note = 'C'
    if note == 2:
        note = 'Db'
    if note == 3:
        note = 'D'
    if note == 4:
        note = 'Eb'
    if note == 5:
        note = 'E'
    if note == 6:
        note = 'F'
    if note == 7:
        note = 'Gb'
    if note == 8:
        note = 'G'
    if note == 9:
        note = 'Ab'
    if note == 10:
        note = 'A'
    if note == 11:
        note = 'Bb'
    if note == 12:
        note = 'B'
    
    note6 = note

    
    print(note1, note2, note3, note4, note5, note6, note1)
    

   






























