
class StudentManager:

    def __init__(self):
        self.students = {}

    # Function to add a student
    def add_student(self, student_id, name, marks):

        if student_id == "" or name.strip() == "":
            raise ValueError("Student ID and name are required")

        if student_id in self.students:
            raise ValueError("Student already exists")

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        self.students[student_id] = {
            "name": name,
            "marks": marks
        }

        return "Student added successfully"

    # Function to view student details
    def view_student(self, student_id):

        if student_id in self.students:
            return self.students[student_id]

        raise ValueError("Student not found")

    # Function to update student marks
    def update_marks(self, student_id, marks):

        if student_id not in self.students:
            raise ValueError("Student not found")

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        self.students[student_id]["marks"] = marks

        return "Marks updated successfully"

    # Function to delete a student
    def delete_student(self, student_id):

        if student_id not in self.students:
            raise ValueError("Student not found")

        del self.students[student_id]

        return "Student deleted successfully"

    # Function to calculate average marks
    def calculate_average(self):

        if len(self.students) == 0:
            return 0

        total = 0

        for student in self.students.values():
            total = total + student["marks"]

        average = total / len(self.students)

        return average


# Main function
def main():

    manager = StudentManager()

    while True:

        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Calculate Average")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                marks = float(input("Enter Student Marks: "))

                print(manager.add_student(student_id, name, marks))

            elif choice == "2":

                student_id = input("Enter Student ID: ")
                student = manager.view_student(student_id)

                print("Student Name:", student["name"])
                print("Student Marks:", student["marks"])

            elif choice == "3":

                student_id = input("Enter Student ID: ")
                marks = float(input("Enter New Marks: "))

                print(manager.update_marks(student_id, marks))

            elif choice == "4":

                student_id = input("Enter Student ID: ")

                print(manager.delete_student(student_id))

            elif choice == "5":

                print("Average Marks:", manager.calculate_average())

            elif choice == "6":

                print("Thank you!")
                break

            else:

                print("Invalid choice. Please try again.")

        except ValueError as error:

            print("Error:", error)


if __name__ == "__main__":
    main()
