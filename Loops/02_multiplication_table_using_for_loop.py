# Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter a number to knows its multiplication table: "))

for i in range(1, 11):
	print(str(num) + "x" + str(i) + "=" + str(i*num))