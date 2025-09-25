# Write a program to create a class with the name Student and perform the following tasks - 
# 1. Declare a variable grade 
# 2. Print a sentence inside the class 
# 3. Create an object of class student and see the output

class Student:
    def __init__(self, grade):
        self.grade= grade
    def display(self):
        print(f"You are from {self.grade} grade.")
student=Student("9")      
student.display()  

