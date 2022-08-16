#Build a Snake_Water_Gun_Game using a python program.  

import random

# Snake Water Gun 
def gameWin(comp, b):
    # If two values are equal, declare a tie!
    if comp == b:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if b =='w':
            return False
        elif b =='g':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if b =='g':
            return False
        elif b =='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if b =='s':
            return False
        elif b =='w':
            return True

print("Computerg Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

b = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, b)

print(f"Computer chose {comp}")
print(f"You chose {b}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")