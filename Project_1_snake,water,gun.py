import random

def gameWin(com, you):
    if comp==you:
        return None
    elif com=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif com =='w':
        if you=='g':
            return False
        elif you=='s':
          return True 
    elif comp =='g':
        if you=='s':
            return False
        elif you=='w':
            return True
print("Comp turn:Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)
if randNo ==1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp='g'

you=input("Your Turn:Snake(s) Water(w) or Gun(g)?")
a=gameWin(comp,you)

print(f"Comp chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You loose!")