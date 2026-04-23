# Basic Python Class Example

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating object
student1 = Student("Alice", 20)

# Calling method
student1.show_details()

