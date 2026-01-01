import csv
import os

# Files
STUDENT_FILE = "students.csv"
COURSE_FILE = "courses.csv"
ENROLLMENT_FILE = "enrollments.csv"

# Field Names

STUDENTS_FILED = ["id", "name", "age"]
COURSE_FILED = ["course_id", "course_name", "instructor"]
ENROLLEMENT_FILED = ["enroll_id", "student_id", "course_id", "grade"]

# Helper Functions
def load_csv(filename):
    if not os.path.exists(filename):
        with open(filename, mode="x") as file:
            print(f"{filename} has been created.")
    with open(filename, mode="r", newline="") as file:
        return list(csv.DictReader(file))    

def save_csv(filename, field_names, data):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

# Students
def view_students():
    students = load_csv(STUDENT_FILE)
    for s in students:
        print(s)

def add_students():
    students = load_csv(STUDENT_FILE)
    s_id = input("Enter Student ID: ")

    for s in students:
       if s["id"] == s_id:
        print("ID must be unique")
        return
    students.append({
        "id" : s_id,
        "name": input("Enter Students Name: "),
        "age": input("Enter Students Age: ")
    })
    save_csv(STUDENT_FILE, STUDENTS_FILED, students)

def update_students():
    students = load_csv(STUDENT_FILE)
    s_id = input("Enter Student ID: ")
    for s in students:
        if s["id"] == s_id:
            s["name"] = input("Enter New Name: ")
            s["age"] = input("Enter New Age: ")
            save_csv(STUDENT_FILE, STUDENTS_FILED, students)
            print("Students Data Has Been Updated.")
            return
    print("Student Data not found!")

def delete_students():
    students = load_csv(STUDENT_FILE)
    enrollemnts = load_csv(ENROLLMENT_FILE)

    s_id = input("Enter Student ID: ")
    students  = [s for s in students if s["id"] != s_id]
    enrollemnts = [e for e in enrollemnts if e["student_id"] != s_id]
    save_csv(STUDENT_FILE, STUDENTS_FILED, students)
    save_csv(ENROLLMENT_FILE, ENROLLEMENT_FILED, enrollemnts)
    print("Student and related enrollments has been deleted.")
    
   

# Course
def add_course():
    courses = load_csv(COURSE_FILE)
    c_id = input("Course ID: ")

    for c in courses:
        if c["course_id"] == c_id:
            print("Course id must be unique.")
            return 

    courses.append({
        "course_id" : c_id,
        "course_name": input("Enter Course Name: "),
        "instructor" : input("Enter Instructor's Name: ")
    })
    
    save_csv(COURSE_FILE, COURSE_FILED, courses)
    print("Data has been added!")

def view_course():
    courses = load_csv(COURSE_FILE)
    for c in courses:
        print(c)

def update_course():
    courses =  load_csv(COURSE_FILE)
    c_id = input("Enter Course ID: ")

    for c in courses:
        if c["course_id"] == c_id:
            c["course_name"] = input("Enter New Course Name: ")
            c["instructor"] = input("Enter New Instructor: ")
            save_csv(COURSE_FILE, COURSE_FILED, courses)
            print("Data has been Updated! ")
            return 

    print("Data has not been found!")


def delete_course():
    courses = load_csv(COURSE_FILE)
    enrollments = load_csv(ENROLLMENT_FILE)

    c_id = input["Enter Course ID: "]

    courses = [c for c in courses if c["course_id"] != c_id]
    enrollments = [e for e in enrollments if e["course_id"] != c_id]

    save_csv(COURSE_FILE, COURSE_FILED, courses)
    save_csv(ENROLLMENT_FILE, ENROLLEMENT_FILED, enrollments)

    print("Course and related enrollments has been deleted.")

# Enrollement

def enroll_student():
    students = load_csv(STUDENT_FILE)
    courses = load_csv(COURSE_FILE)
    enrollements = load_csv(ENROLLMENT_FILE)

    e_id = input("Enter Enrollement ID: ")
    for e in enrollements:
        if e["enroll_id"] == e_id:
            print("Enrollement ID must be unique!")
            return 

    s_id = input("Enter Student ID: ")
    if not any(s["id"] == s_id for s in students):
        print("Students ID must be present!")
        return 
    c_id = input("Enter Course ID: ")
    if not any(c["course_id"] == c_id for c in courses):
        print("Cours ID must be present!")
        return

    if any(e["student_id"] == s_id and e["course_id"] == c_id for e in enrollements):
        print("Relationship already exist.")
        return 
    
    enrollements.append({
        "enroll_id" : e_id,
        "student_id" : s_id,
        "course_id": c_id,
        "grade" : ""
    })
    save_csv(ENROLLMENT_FILE, ENROLLEMENT_FILED, enrollements)
    print("File Saved.")


def update_grade():
    enrollements = load_csv(ENROLLMENT_FILE)
    s_id = input("Student ID: ")
    c_id = input("Course ID: ")

    for e in enrollements:
        if e["student_id"] == s_id and e["course_id"] == c_id:
            e["grade"] = input("Enter Grade: ")
            save_csv(ENROLLMENT_FILE, ENROLLEMENT_FILED, enrollements)
            print("Grade updated!")
            return

    print("File not found!")

def unenroll_student():
    enrollements = load_csv(ENROLLMENT_FILE)
    s_id = input("Student ID: ")
    c_id = input("Course ID: ")

    new_enrollements = [e for e in enrollements 
    if not (e["student_id"] == s_id and e["course_id"] == c_id) ]

    save_csv(ENROLLMENT_FILE, ENROLLEMENT_FILED, new_enrollements)
    print("Student Unenrolled")

def student_transcript():
    s_id = input("Enter Students ID: ")
    students =  load_csv(STUDENT_FILE)
    courses =  load_csv(COURSE_FILE)
    enrollements =  load_csv(ENROLLMENT_FILE)

    student = []
    for s in students:
        if s["id"] == s_id:
            student.append(s)

    if not student:
        print("Student not found!")
        return

    print(f"Transcript for {student[0]["name"]}")

    course = []
    for e in enrollements:
        if e["student_id"] == s_id:
            for c in courses:
                if c["course_id"] == e["course_id"]:
                    course.append(c)

        print(course[0]["course_name"], " -> ", e["grade"] )
            



# Menu 

def student_menu():
    while True:
        print("\n Student Menu")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back")

        c = input("Select Operation: ")
        match c:
            case "1":
                add_students()
            case "2":
                view_students()
            case "3":
                update_students()
            case "4":
                delete_students()
            case "5":
                break

def course_menu():
    while True:
        print("\n Course Menu")
        print("1. Add Course")
        print("2. View Course")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Back")

        c = input("Select Operation: ")
        match c:
            case "1":
                add_course()
            case "2":
                view_course()
            case "3":
                update_course()
            case "4":
                delete_course()
            case "5":
                break

def enrollement_menu():
    while True:
        print("\n Enrollement Menu")
        print("1. Enroll")
        print("2. Update Grade")
        print("3. Unenroll")
        print("4. Transcript")
        print("5. Back")

        c = input("Select Operation: ")
        match c:
            case "1":
                enroll_student()
            case "2":
                update_grade()
            case "3":
                unenroll_student()
            case "4":
                student_transcript()
            case "5":
                break
    
def main_menu():
    while True:
        print("**************** Enrollement System **************")

        print("1. Students")
        print("2. Course")
        print("3. Enrollement")
        print("4. Exit")

        c = input("Select Operation: ")
        match c:
            case "1":
                student_menu()
            case "2":
                course_menu()
            case "3":
                enrollement_menu()
            case "4":
                break

main_menu()