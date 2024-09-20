import random
computer_choice = random.choice(['rock','paper','scissor'])
user_choice = input("Enter Your Choice?\n")
print("Computer Choice:",computer_choice)
if computer_choice == user_choice :
    print("TIE")
elif computer_choice == 'paper' and user_choice == 'scissor':
    print("You win")
elif computer_choice == 'rock' and user_choice == 'paper':
    print("You win")
elif computer_choice == 'scissor' and user_choice == 'rock':
    print("You win")
else:
    print("Computer Wins,You lost")