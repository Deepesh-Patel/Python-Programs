# Write a python program which find out whether a given name is present in a list or not.


names =["buddy", "chris", "clara", "shiloh", "john", "tom"]
name = input("Enter the name to check in the list: ")

if(name in names):
    print("Your name is present in the list.")
else:
    print("Your name is not present in the list.")