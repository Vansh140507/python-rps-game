import random

def game():
      choose={1:"rock",2:"paper",3:"scissor"} 
while True:
    choose={1:"rock",2:"paper",3:"scissor"} 
    print("1. rock ")
    print("2. paper")
    print("3. scissor")
    print("4. exit ")
    user_choice=int(input("enter your choice: "))
    if(user_choice==4):
        print("thank you ")
        break
    elif user_choice not in choose :
        print("invalid ")
        continue
    
    user=choose[user_choice]
    print(f"your choice:{user}")

    computer_choice=random.randint(1,3)
    comp=choose[computer_choice]
    print(f"computer choice:{comp}")
    if user_choice==computer_choice:
        print("it's a tie !!")
    elif(user_choice==1 and computer_choice==3) or \
        (user_choice==2 and computer_choice==1) or \
         (user_choice==3 and computer_choice==2):
        print("YOU WIN !!")
    else:
        print("YOU LOSE !!")

game()
    






