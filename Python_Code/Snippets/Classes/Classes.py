students = []


class Student:
    def add_student(self, name, stud_id=666):
        student_dic = {"name": name, "student_id": stud_id}
        # print("Adding studend")
        # print("Student list", students)
        students.append(student_dic)
    pass

student = Student()

print(student)

new_student = Student()

print(new_student)