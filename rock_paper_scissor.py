import random

user_wins=0
computer_wins=0

options= ["Rock", "Paper", "Scissors"]


while True:
    user_input=input("Type Rock/paper/scissors or Q to quit: ").lower()
    if user_input=="q":
        break

    if user_input not in options:#making a list, if the user typed in exists in this list.
        continue

    random_number=random.radiant(0,2)
    #rock:0 papar:1 scissors:2
    computer_pick=options[random_number]
    print("comouter picked", computer_pick+ ".")

    if user_input== "rock" and computer_pick=="scissors":
        print("You won")
        user_wins+=1


    elif user_input== "Paper" and computer_pick== "rock":
        print("You won")
        user_wins+=1
        

    elif user_input=="scissors" and computer_pick=="paper":
        print("You won")
        user_wins+=1
        
    else:
        print("You Lost!!")
        computer_wins+=1


print("You won", user_wins, "times.")
print("The computer wons", computer_wins, "times.")
    
print("GoodBye!Thanks for playing")




