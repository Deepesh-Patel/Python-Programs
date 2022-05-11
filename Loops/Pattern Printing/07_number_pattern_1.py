''' Write a program to print following number pattern
		1
		2 2
		3 3 3
		4 4 4 4
		5 5 5 5 5
		6 6 6 6 6 6          '''

rows = int(input("Enter the number of rows: "))  

for i in range(rows+1):  
    for j in range(i):  
        print(i, end=" ")  
    print(" ")  
