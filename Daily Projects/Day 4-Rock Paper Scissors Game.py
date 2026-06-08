import random

print("WELCOME TO ROCK PAPER SCISSORS GAME")

player_choice=input("Enter your choice.\n Rock, Paper or Scissors?:")

computer_choice=['Rock','Paper','Scissors']

a=random.randint(0,2)

computer_decision=computer_choice[a]


#Condition 1 (PLAYER WINS)

if(player_choice=="Rock" and computer_decision=="Scisscors") or (player_choice=="Paper" and computer_decision=="Rock") or (player_choice=="Scissors" and computer_decison=="Paper"):
    print("Computer chose:",computer_decision,"You win")
#Conditon 2(COMPUTER WINS)

elif(player_choice=="Rock" and computer_decision=="Paper") or (player_choice=="Paper" and computer_decision=="Scissors") or (player_choice=="Scissors" and computer_decision=="Rock"):
    print("Computer chose:",computer_decision,"You lose")
#Condition 3(DRAW)
elif player_choice==computer_decision:
    print("Computer chose:",computer_decision,"It's a Draw") 
        
       

       
    
