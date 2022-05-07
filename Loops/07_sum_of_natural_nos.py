# Write a program to find the sum of first n natural numbers using while loop.

num = int(input("Please Enter any Num: "))

total = 0
value = 1

while (value <= num):
    total = total + value
    value = value + 1

print("The Sum from 1 to {0} =  {1}".format(num, total))