class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def update_age(self, new_age):
        self.age = new_age
        print("Age updated successfully!")

    def change_course(self, new_course):
        self.course = new_course
        print("Course changed successfully!")

    def is_adult(self):
        if self.age >= 18:
            print(self.name, "is an adult.")
        else:
            print(self.name, "is not an adult.")


# Creating object
student1 = Student("Alice", 20, "Computer Science")

# Calling methods
student1.show_details()
student1.update_age(21)
student1.change_course("Data Science")
student1.is_adult()
student1.show_details()