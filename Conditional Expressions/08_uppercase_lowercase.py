# Write a program to check whether entered character is in uppercase or lowercase.


ch = input("Enter any character : ")[0]

# Check for uppercase &  lowercase
if ch.isupper() :
    print("\n" + ch, "is UPPERCASE alphabet.")

elif ch.islower() :
    print("\n" + ch, "is LOWERCASE alphabet.")

else :
    print("\n" + ch, "is not an alphabet.")