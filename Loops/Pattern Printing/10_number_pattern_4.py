''' Write a program to print following number pattern
	6 6 6 6 6 6 
	5 5 5 5 5 
	4 4 4 4 
	3 3 3 
	2 2 
	1       '''

rows = int(input("Enter the number of rows: "))  
# Downward loop for inverse loop  
for i in range(rows, 0, -1):  
    n = i   # assign value to n of i after each iteration  
    for j in range(0, i):  
        # print reduced value in each new line  
        print(n, end=' ')  
    print("\r")  
