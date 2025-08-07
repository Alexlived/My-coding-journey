Rock = 1
Paper = 2
Scissors = 3
import random
replay = 'yes'
while replay.lower() == 'yes':
    


    print('')
    print("Rock = 1")
    print("Paper = 2")
    print("Scissors = 3")

    print('')
    user = int(input('What do you pick?: '))
    if user not in [1,2,3]:
        print("Invalid action,try again")
        exit()
    print('')
    print("You picked ")
    if user == 1:
        print("Rock")
    if user == 2:
        print("Paper")
    if user == 3:
        print("Scissors")
 

    computer = random.randint(1,3)
    print("Computer picked")
    if computer == 1:
        print("Rock")
    if computer == 2:
        print("Paper")
    if computer == 3:
        print("Scissors")



    if computer == 1 and user == 2: #Computer is rock and user is paper
        print("You won,paper beats rock") 
    if computer == 2 and user == 1: #Computer is paper and user is rock
        print("You lost,paper beats rock")
    if computer == 2 and user == 3: #Computer is scissors and user is paper
        print("You lost,scissors beats paper")
    if computer == 3 and user == 2: #Computer is paper and user is rock
         print("You won,scissors beats paper")
    if computer == 3 and user == 1: #Computer is scissors and user is rock
        print("You won,rock beats scissors")
    if computer == 1 and user == 3: #Computer is rock and user is scissors
        print("You lost,rock beats scissors")
    if computer == 1 and user == 1:
        print("Nobody won,its a tie")
    if computer == 2 and user == 2:
        print("Nobody won,its a tie")
    if computer == 3 and user == 3:
        print("Nobody won,its a tie")

    replay = input("Would you like to play again?(Yes/No)").lower()
    if replay == 'no':
        exit()
  


