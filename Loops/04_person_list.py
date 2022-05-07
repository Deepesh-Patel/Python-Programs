''' Write a program to greet all person names stored in a list l1 and which starts with S.
     l1 = ["Buddy", "Soham", "Sachin", "Rahul", "Shubham", "Vikas"] '''
     
l1 = ["Buddy", "Soham", "Sachin", "Rahul", "Shubham", "Vikas"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)
     