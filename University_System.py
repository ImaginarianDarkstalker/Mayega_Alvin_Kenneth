class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"


class Lecturer:
    def __init__(self, lecturer_id, name):
        self.lecturer_id = lecturer_id
        self.name = name
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"{self.name} (Lecturer ID: {self.lecturer_id})"


class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.lecturer = None

    def add_student(self, student):
        self.students.append(student)

    def assign_lecturer(self, lecturer):
        self.lecturer = lecturer

    def __str__(self):
        lecturer_info = self.lecturer.name if self.lecturer else "None"
        return f"{self.course_name} ({self.course_code}), Lecturer: {lecturer_info}"


class UniversityManagementSystem:
    def __init__(self):
        self.students = {}
        self.lecturers = {}
        self.courses = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student '{name}' added.")
        else:
            print("Student already exists.")

    def add_lecturer(self, lecturer_id, name):
        if lecturer_id not in self.lecturers:
            self.lecturers[lecturer_id] = Lecturer(lecturer_id, name)
            print(f"Lecturer '{name}' added.")
        else:
            print("Lecturer already exists.")

    def add_course(self, course_code, course_name):
        if course_code not in self.courses:
            self.courses[course_code] = Course(course_code, course_name)
            print(f"Course '{course_name}' added.")
        else:
            print("Course already exists.")

    def enroll_student(self, student_id, course_code):
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        if student and course:
            student.enroll(course)
            course.add_student(student)
            print(f"Student '{student.name}' enrolled in '{course.course_name}'.")
        else:
            print("Student or course not found.")

    def assign_lecturer(self, lecturer_id, course_code):
        lecturer = self.lecturers.get(lecturer_id)
        course = self.courses.get(course_code)
        if lecturer and course:
            course.assign_lecturer(lecturer)
            lecturer.assign_course(course)
            print(f"Lecturer '{lecturer.name}' assigned to course '{course.course_name}'.")
        else:
            print("Lecturer or course not found.")

    def view_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"\nStudent: {student}")
            if student.courses:
                print("Enrolled Courses:")
                for course in student.courses:
                    print(f"- {course.course_name}")
            else:
                print("No courses enrolled.")
        else:
            print("Student not found.")

    def view_lecturer(self, lecturer_id):
        lecturer = self.lecturers.get(lecturer_id)
        if lecturer:
            print(f"\nLecturer: {lecturer}")
            if lecturer.courses:
                print("Assigned Courses:")
                for course in lecturer.courses:
                    print(f"- {course.course_name}")
            else:
                print("No courses assigned.")
        else:
            print("Lecturer not found.")

    def view_course(self, course_code):
        course = self.courses.get(course_code)
        if course:
            print(f"\nCourse: {course}")
            if course.students:
                print("Students enrolled:")
                for student in course.students:
                    print(f"- {student.name}")
            else:
                print("No students enrolled.")
        else:
            print("Course not found.")


def main():
    ums = UniversityManagementSystem()

    while True:
        print("\n--- University Management System ---")
        print("1. Add Student")
        print("2. Add Lecturer")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. Assign Lecturer to Course")
        print("6. View Student Details")
        print("7. View Lecturer Details")
        print("8. View Course Details")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            sid = input("Enter student ID: ")
            name = input("Enter student name: ")
            ums.add_student(sid, name)

        elif choice == '2':
            lid = input("Enter lecturer ID: ")
            name = input("Enter lecturer name: ")
            ums.add_lecturer(lid, name)

        elif choice == '3':
            code = input("Enter course code: ")
            cname = input("Enter course name: ")
            ums.add_course(code, cname)

        elif choice == '4':
            sid = input("Enter student ID: ")
            code = input("Enter course code: ")
            ums.enroll_student(sid, code)

        elif choice == '5':
            lid = input("Enter lecturer ID: ")
            code = input("Enter course code: ")
            ums.assign_lecturer(lid, code)

        elif choice == '6':
            sid = input("Enter student ID: ")
            ums.view_student(sid)

        elif choice == '7':
            lid = input("Enter lecturer ID: ")
            ums.view_lecturer(lid)

        elif choice == '8':
            code = input("Enter course code: ")
            ums.view_course(code)

        elif choice == '9':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 9.")


if __name__ == "__main__":
    main()
