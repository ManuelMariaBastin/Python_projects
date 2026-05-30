#importing random module 
import random as rd 

Real_player_1='' #initialization to store user input

#initialization of scores
Real_player_score=0
Com_player_score=0
play=0 #no. of rounds

print('----------------------------------------------------------------------')
print("------------- Welcome to Rock, Paper, Scissors Game! -----------------")
print('----------------------------------------------------------------------')


while Real_player_1 !='exit': #to play until user wants to exit the game

    Real_player_1=input("Enter your choice(1- Rock,2- Paper,3- Scissors or exit) : ")
    play += 1 #calculate rounds played

    if Real_player_1 == '1':
        Real_player_1 = 'Rock'
    elif Real_player_1 == '2':
        Real_player_1 = 'Paper'
    elif Real_player_1 == '3':
        Real_player_1 = 'Scissors'
    elif Real_player_1 in ['exit', 'Exit', 'EXIT']:
        print("Exiting the game. Thanks for playing!\n")
        break    
    else:
        print("Invalid input, please enter 1, 2, 3 or exit\n")
        continue

    #printing current  playing Round, Real_palyer choice and Computer choice

    print(f"\n------ Round {play} ---------")#current playing round

    print(f"Real player choice is : {Real_player_1}")#Real_player_1 choice 

    Com_player_1=rd.choice(['Rock','Paper','Scissors']) #computer random choice from options list
    
    print(f"Comp random choice is : {Com_player_1}")#Comp_player choice 
    
    
    # Game logic:
    if Real_player_1 == Com_player_1:
        print("It's a tie!\n")
       
        Real_player_score=Real_player_score
        Com_player_score=Com_player_score

    elif     (Real_player_1 ==  'Rock' and  Com_player_1 == 'Scissors') \
          or (Real_player_1 ==  'Paper' and  Com_player_1 == 'Rock') \
          or (Real_player_1 ==  'Scissors' and  Com_player_1 == 'Paper'):
        
        print("Real_player win!\n")
       
        Real_player_score += 1
    else:
        print("Computer wins!\n")
        Com_player_score += 1

# Print the final scores and declare the winner        

print('--------------- Final Scores -------------------------')
print(f"No.of rounds played : {play-1} ")
print('------------------------------------------------------')
print(f"Real_player: {Real_player_score}")
print(f"Computer   : {Com_player_score}\n")


if Real_player_score > Com_player_score:
    print("Congratulations! You won the game!\n")
elif Real_player_score < Com_player_score:
    print("Computer wins the game! Better luck next time.\n")
else:
    print("The game is a tie!\n")

print('------------------------------------------------------')    
