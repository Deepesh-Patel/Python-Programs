# Write a program to print multiplication table of a given number using while loop.

num = int(input("Enter a number to knows its multiplication table: "))

i = 1
while i < 11:
	 print(str(num) + "x" + str(i) + "=" + str(i*num))
	 i = i+1