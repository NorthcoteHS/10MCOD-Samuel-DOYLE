print('This is a calculator for your hockey shooting accuracy.')
typeofshot = input('Enter type of shot:')
target =input('Enter target you are going for:')
shots = input('Enter amount of the shots you hit:')
outof = input('Enter amount of shots you took:')
shots = int(shots)
outof = int(outof)
per = shots*100/outof
print ('When going for',(target), 'Your Percentage for' ,(typeofshot),'is', str(per),'%')

 
