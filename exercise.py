class Student():
    
    student_count = 0  #variable that keeps track of the number of students
    
    def __init__(self, name, age, serial_number):
        self.name = name
        self.age = age
        self.serial_number = serial_number
        Student.student_count += 1  #increment the student_count variable by 1
    
    def get_student_info(self):
        print(f"Name: {self.name}, age: {self.age}, serial number: {self.serial_number}")
        
    @staticmethod
    def get_student_count():
        print(f"Total number of students: {Student.student_count}")

student1 = Student("Leonardo", 18, 123)
student2 = Student("Matteo", 17, 456)
student3 = Student("Davide", 19, 789)

student1.get_student_info()
student2.get_student_info()
student3.get_student_info()

Student.get_student_count()  #call the static method