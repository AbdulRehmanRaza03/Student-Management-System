class Student:
    def __init__(self, student_id, name, age, student_class, email, image_path=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.student_class = student_class
        self.email = email
        self.image_path = image_path


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        return self.students

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]


