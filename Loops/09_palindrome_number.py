# Write a program to check whether a given no. is palindrome or not.

n = int(input("Enter any number: "))

temp=n
rev=0

while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
    
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")