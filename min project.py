
class Student:
    def __init__(self, name, roll_no, course):
    
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def display_details(self):
    
        print(f"Name: {self.name} | Roll No: {self.roll_no} | Course: {self.course}")

student_list = []


def add_student():
    # Adding a new student DETAILS
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    course = input("Enter Course: ")
    
    
    new_student = Student(name, roll_no, course)
    student_list.append(new_student)
    print("Student added successfully!")

def display_all_students():
    
    if not student_list:
        print("No students found.")
    else:
        print("\n--- Student Records ---")
        for s in student_list:
            s.display_details()

def search_student():
    # Searching for a specific student using  loop and conditional statements 
    query = input("Enter Roll Number to search: ")
    found = False
    for s in student_list:
        if s.roll_no == query:
            print("Student Found:")
            s.display_details()
            found = True
            break
    if not found:
        print("Student not found.")

# 4. Main Menu (Control Flow Concept)
while True:
    # Creating  interactive menu with  while loop
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program...")
        break # Exiting the loop
    else:
        print("Invalid choice, try again.")