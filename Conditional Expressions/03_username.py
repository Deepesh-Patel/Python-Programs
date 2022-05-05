# Write a python program to find whether a given username contains less than 10 characters or not.

user = input("Enter your username: ")

if(len(user)<10):
    print("The maximum number of character should be 10")
else:
    print("You can now login succesfully")