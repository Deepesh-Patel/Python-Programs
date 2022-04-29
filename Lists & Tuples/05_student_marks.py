#Write a python program to accept marks of 6 students display them in a sorted manner.

m1 = input("Enter the marks of student no 1: ")
m2 = input("Enter the marks of student no 2: ")
m3 = input("Enter the marks of student no 3: ")
m4 = input("Enter the marks of student no 4: ")
m5 = input("Enter the marks of student no 5: ")
m6 = input("Enter the marks of student no 6: ")

student_list = [m1, m2, m3, m4, m5, m6]
student_list.sort()

print("\n****** ENTERED STUDENTS MARKS******")
print(student_list)