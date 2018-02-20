import random
l=["rock","paper","scissor"]
i=input("press y to play")
while(i=="y"):
    a=input("choose r: for rock,p:for paper,s:for scissors")
    a.lower()
    b=random.choice(l)
    print("computer chose",b)
    print("your choice is",a)
    if a=="r":
        if b==l[0]:
            print("its a tie")
        elif b==l[1]:
            print("computer wins")
        elif b==l[2]:
            print("you win")
    if a=="r":
        if b==l[0]:
            print("its a tie")
        elif b==l[1]:
            print("computer wins")
        elif b==l[2]:
            print("you win")
    if a=="r":
        if b==l[0]:
            print("its a tie")
        elif b==l[1]:
            print("computer wins")
        elif b==l[2]:
            print("you win")
       
                 
          
