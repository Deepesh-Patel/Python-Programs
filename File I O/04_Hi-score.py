# The game() function in a program lets a user play a game 
# and returns a score as an integer. You need to read a file
# 'Hiscore.txt' which is either blank or contains the previous 
# Hi-score. You need to write a program to update the Hi-score
# whenever game() breaks the Hi-score. 


def game():
   return 184

score = game()
with open("E:\Deepesh\Python\File I O\Highscore.txt") as f:
    hiscoreStr = f.read()

if(hiscoreStr == ''):
    with open("E:\Deepesh\Python\File I O\Highscore.txt", "w") as f:
        f.write(str(score))

elif(int(hiscoreStr) < score):
    with open("E:\Deepesh\Python\File I O\Highscore.txt", "w") as f:
        f.write(str(score))      