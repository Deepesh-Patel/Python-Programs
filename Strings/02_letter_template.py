''' Write a python program to fill in a letter template given below with name and date.

letter =  "'Dear <|NAME|> ,
                You are Selected !!
                <|DATE|>''' 
                

letter = '''Dear <|NAME|> ,
You are Selected !!
<|DATE|>
'''
                
name = input("Enter your name: \n")
date = input("Enter Date: \n")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)

