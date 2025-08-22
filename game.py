import random

computer = random.choice([-1,0,1])

youstr = input("Enter your choice :- ")
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1 : "Snake", -1: "Water", 0: "Gun"}

you = youdict[youstr]

print(f"You chose {reversedict[you]}\n computer choice {reversedict[computer]}")

if(computer == you):
    print("Its's a Draw")
else:
    if(computer == 1 and you == 0):
        print("YOU WIN!")
    elif(computer == 1 and you == -1):
        print("YOU LOSE!")
    elif(computer == -1 and you == 1):
        print("YOU WIN!")
    elif(computer == -1 and you == 0):
        print("YOU LOSE!")
    elif(computer == 0 and you == 1):
        print("YOU LOSE!")
    elif(computer == 0 and you == -1):
        print("YOU WIN!")
    else:
        print("Something Went Wrong")