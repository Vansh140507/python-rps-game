import utilis
import logic
def game():
 while True:
   
    print("1. rock ")
    print("2. paper")
    print("3. scissor")
    print("4. exit ")
    user_choice=int(input("enter your choice: "))
    if(user_choice==4):
        print("thank you ")
        break
    elif user_choice not in utilis.choose:
        print("invalid ")
        continue
    print(f"your choice:{utilis.choose[user_choice]}")
    computer_choice=utilis.computer_move()
    print(f"computer choice:{utilis.choose[computer_choice]}")
    logic.winner(user_choice,computer_choice)


game()
   

    






