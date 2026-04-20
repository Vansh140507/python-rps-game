
def winner(user_choice,computer_choice):
    if user_choice==computer_choice:
            print("it's a tie !!")
    elif(user_choice==1 and computer_choice==3) or \
        (user_choice==2 and computer_choice==1) or \
         (user_choice==3 and computer_choice==2):
        print("YOU WIN !!")
    else:
        print("YOU LOSE !!")


