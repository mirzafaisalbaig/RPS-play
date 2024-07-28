import random

print("Lets play Rock Paper Scissor ?")

user_wins = 0
computer_wins = 0


options = ["rock","paper","scissor"]

while True:
    user_guess = input("choose any Rock/Paper/Scissor or q for Quit: ").lower()  
    if user_guess == 'q':
        break
    elif user_guess not in options:
        continue

    random_guess = random.randint(0,2) # it includes 0,1,2 => 3

    computer_picked = options[random_guess] # options[0.rock, 1.paper, 2.scissor]
    print('computer picked '+ computer_picked +".") 
    computer_wins += 1 

    if user_guess == 'rock' and computer_picked =="scissor":
        print("You won! :)")
        user_wins += 1
        continue
    if user_guess == 'paper' and computer_picked =="rock":
        print("You won! :)")
        user_wins += 1
        continue
    if user_guess == 'scissor' and computer_picked =="paper":
        print("You won! :)")
        user_wins += 1
        continue
print("User wins: ", user_wins)
print("computer wins: ",computer_wins)
print("GOODBYE!")
  