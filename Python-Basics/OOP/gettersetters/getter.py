class Student:
    def __init__(self, first_name):
        self.first_name = first_name

    # define getter method
    @property
    def getter(self):
        return self.first_name
        
# create a new Student object
student = Student("Mwaura")

# access the first name using data property
print(student.first_name)  # Mwaura

# access the first name using getter property
print(student.getter)  # Mwaura
