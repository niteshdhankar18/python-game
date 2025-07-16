import random
'''
1= snake 
2= water
3 = gun
'''
computer = random.choice([1,2,3])
you= int(input("enter your choice(1 for snake , 2 for water, 3 for gun):"))
# dict={"snake": 1, "water": 2, "gun": 3}
reversedict= {1: "snake", 2: "water", 3: "gun"}
# you = dict[youstr]
print(f"you choose{reversedict[you]} ")
print(f"computer choose{reversedict[computer]}")
if(computer==you):
    print("match draw ")
else:
    if(computer==1 and you==2):
        print("you loose!")
    elif(computer==1 and you==3):
        print("you win!")
    elif(computer==2 and you==1):
        print("you win!")
    elif(computer==2 and you==3):
        print("you loose !")
    elif(computer==3 and you==1):
        print("you loose !")
    elif(computer==3 and you==2):
        print("you win!")
    else:
     print("something went wrong")    