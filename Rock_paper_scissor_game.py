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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"You choose: {user}")
if user==0:
    print("Rock")
    print(rock)
elif user==1:
    print("Paper")
    print(paper)
elif user==2:
    print("Scissors")
    print(scissors)
else:
    print("enter valid number")

game = [rock,paper,scissors]
computer = random.randint(0,2)
print("computer choose: ")
print(computer)
print(game[computer])
if user == computer:
    print("match Draw!")
elif (user==0 and computer==2) or (user == 2 and computer ==1) or (user==1 and computer ==0):
    print("you won!")
else:
    print("You Lose!")