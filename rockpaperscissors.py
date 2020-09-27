from random import randint
choice = ["rock", "paper", "scissors"]
user_input = str.lower(input("please enter rock, paper or scissors:"))
while user_input != "rock" and user_input != "paper" and user_input != "scissors":
    user_input = str.lower(input("invalid input, please enter rock or paper or scissors only:"))
computer = choice[randint(0, 2)]
print("computer has chosen", computer)
if (computer == "rock" and user_input == "scissors") or (computer == "paper" and user_input == "rock") or (computer == "scissors" and user_input == "paper"):
    print("You Lose!")
elif computer == user_input:
    print("Tie!")
else:
    print("You Win!")



