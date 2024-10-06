class Student():
    def __init__(self, name, age, serial_number):
        self.name = name
        self.age = age
        self.serial_number = serial_number
        student_count = student_count + 1
    
    def get_student_info(self):
        print(f"Name: {self.name}, age: {self.age}, serial number: {self.serial_number}")

    @staticmethod
    def get_student_count():
        print(f"student_count")

student1 = Student("John", 21, 12345)
student2 = Student("Alice", 22, 12346)
student3 = Student("Bob", 23, 12347)

student1.get_student_info()
student2.get_student_info()
student3.get_student_info()

Student.get_student_count()