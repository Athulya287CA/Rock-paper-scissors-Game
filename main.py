import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option=[rock,paper,scissors]
you=input('What do you choose.Type:\n "0" for Rock ,\n "1" for Paper or\n "2" for Scissors .\n')
choice=int(you)
print("you chose:")
print(option[choice])

print("computer chose:")

comp=random.randint(0,2)
print(option[comp])

if choice==0:
  if comp==0:
    print("DRAW")
  elif comp==1:
    print("YOU LOSE")
  else:
    print("YOU WIN")
elif choice==1:
  if comp==0:
    print("YOU WIN")
  elif comp==1:
    print("DRAW")
  else :
    print("YOU LOSE")
elif choice==2:
  if comp==0:
    print("YOU LOSE")
  elif comp==1:
    print("YOU WIN")
  else :
    print("DRAW")
else :
  print("Wrong Choice. Try Again.")