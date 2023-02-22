#!/usr/bin/python3
import random

wordbank= ["indentation", "spaces"] 
wordbank.append(4)

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
num =int(input("for a number between 0 and 20. "))
student_name = tlgstudents[num]
print(student_name)
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent")

name = random.choice(tlgstudents)
print(f"{name}")

