# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   JWatts, 2/23/2025,Created Script
#   JWatts, 2/25/2025, Adding Try/Except statements
#   JWatts, 2/26/2025, Improving try/except statements
# ------------------------------------------------------------------------------------------ #

#Import Needed Modules
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = r"Output\Enrollments.json"


# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a dictionary
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

# Error handling
# Makes sure the file is open before trying to close it.
except FileNotFoundError as e:
    if file.closed == False:
        file.close()
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    if file.closed == False:
        file.close()
    print("There was a non-specific error!\n")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')


# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if student_first_name == "":
                raise Exception("Please enter a first name")
            if not student_first_name.isalpha():
                raise ValueError("Please do not include numbers in your name.")

            student_last_name = input("Enter the student's last name: ")
            if student_last_name == "":
                raise Exception("Please enter a last name")
            if not student_last_name.isalpha():
                raise ValueError("Please do not include numbers in your name.")

            course_name = input("Please enter the name of the course: ")
            if course_name == "":
                raise Exception("Please enter a course name")

            # Process input data into dictionary
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)

        except ValueError as e:
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
            continue
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            continue

        # Informs user on entered information
        print("-" * 50)
        print(f"You have registered {student_first_name} "
              f"{student_last_name} for "
              f"{course_name}.")
        print("-" * 50)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("Students In File:")
        print("-"*50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]}"
                  f" is registered for {student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=4)
            file.close()
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()
        print("The following data was saved to file!")
        print("-" * 50)
        for student in students:
            print(f"Student: {student["FirstName"]}, {student["LastName"]}"
                  f" Course: {student["CourseName"]}")
        print("-" * 50)
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
