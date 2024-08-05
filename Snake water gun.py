import random
computer= random.choice([-1,0,1])
user = input("Enter your choice (s for snake, w for water, g for gun): ")
userDict ={"s":-1 , "w":0, "g":1}
you=userDict[user]
reverseDict = {-1:"snake",0:"water",1:"gun"}
print(f"You chose :{reverseDict[you]}")
print(f"Computer Chose :{reverseDict[computer]}")
if(computer==user):
    print("It is a draw")
else:
    if(computer==-1 and you==0):
        print("Computer Wins")
    elif(computer==0 and you==1):
        print("Computer Wins")
    elif(computer==1 and you==-1):
        print("Computer Wins")
    elif(computer==0 and you==-1):
        print("User Wins")
    elif(computer==1 and you==0):
        print("User Wins")
    elif(computer==-1 and you==1):
        print("User Wins")
    else:
        print("something went wrong")