# Здесь был Гоша
import random
print ('Hello,Gosha!')
round = 0
while round < 3:
  print(f'Round {round + 1}')
  value = random.choice(['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' ,'9' , '10', 'J', 'Q' , 'K' , 'A'])
  suit = random.choice(['H' , 'D' , 'S' , 'C'])
  answer = input()
  if answer == 'R' and suit in ['H' , 'D']:
    print(f'Correct . Card was {value}{suit}')
  elif answer == 'B' and suit in ['S' , 'C']:
    print (f'Correct . Card was {value}{suit}')
  else:
    print (f'Incorrect . Card was {value}{suit}')
  round += 1
print('Congratulations, Gosha!')