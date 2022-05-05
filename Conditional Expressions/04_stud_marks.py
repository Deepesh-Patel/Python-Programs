''' Write a program to find out whether a student is
pass or fail, if it requires total no. 40% and atleast
35% in each subject to pass. Assume 3 subjects & 
take marks as an input from the user. '''


s1 = int(input("Enter the marks of 1st subject: "))
s2 = int(input("Enter the marks of 2nd subject: "))
s3 = int(input("Enter the marks of 3rd subject: "))

if(s1<35 or s2<35 or s3<35):
    print("You are fail because you have less than 35% in one of the subjects")
elif((s1+s2+s3)/3 < 40):
    print("You are failed due to total percentage is less than 40")
else:
    print("Congratulations ! You are passed")