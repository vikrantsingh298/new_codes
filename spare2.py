import random
list1=['s','p','c']
plr=0
comp=0
for i in range(5):
 print(f"\n Chance {i+1}")   
 print(''' s: stone
 p: paper
 c: scissor''')
 

 while True:
     guess=input("Enter:")

     if (guess!="s") and (guess!="p") and (guess!="c"):
           print("INVALID ENTRY.......")
           continue
     else:
         break

 n= random.choice(list1)



 if guess==n:
    print("TIED....")

 elif guess=="s":
       
       if n=="p":
           print("You  LOSE..")
           comp+=1

       elif n=="c":
           print("You  WON..")
           plr+=1

 elif guess=="p":
       
       if n=="c":
           print("You  LOSE..")
           comp+=1

       elif n=="s":
           print("You  WON..")
           plr+=1

 elif guess=="c":
       
       if n=="s":
           print("You  LOSE..")
           comp+=1

       elif n=="p":
           print("You  WON..")
           plr+=1

if plr>comp:
    print(f"\n You Won...Your Score is {plr} and computer's Score is {comp}")

elif plr<comp:
    print(f"\n You Lose...Your Score is {plr} and computer's Score is {comp}")

else:
    print("\n Match Tied...")    

    

        
      