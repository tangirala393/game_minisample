n = int(input("no of attempts:"))
import random
li1 = ["snake","gun","water"]
G,S,W,T,U = 0,0,0,0,0
def choice_snake(n):        ######### Userinput ****  snake
    global G,S,T,W,U
    k = random.choice(li1)
    print("random value:",k)
    if k == "gun":
        G = G+1
    elif k == "water":
        U = U+1
    else:
        T = T+1
def choice_gun(n):              ########## Userinput **** Gun
    k = random.choice(li1)
    global G,S,T,W,U
    print("random value:",k)
    if k == "snake":
        U = U+1        
    elif k == "water":
        W = W+1
    else:
        T = T+1
def choice_water(n):                ######### Userinput ****water
    k = random.choice(li1)
    global G,S,T,W,U
    print("random value:",k)
    if k == "gun":
        U = U+1
    elif k == "snake":
        S = S+1
    else:
        T = T+1
for i in range(n):
    user_input = input("\n*****Enter the value:")    #### Enter user choice
    if  user_input == "snake":
        choice_snake(n)
    elif user_input == "gun":
        choice_gun(n)
    elif user_input == "water":
        choice_water(n)
print(U,G,S,W,T)
if U > max(S,G,W,T):
    print("\nCongratulations User won the game")
elif S > max(U,G,W,T):
    print("\nSnake won the game")
elif G > max(S,U,W,T):
    print("\nGun won the game")
elif T > max(U,S,W,G):
    print("\ngame was Tie")










