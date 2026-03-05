# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.
file = None  # Holds a reference to an opened file.

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
    ChangeLog: (Who, When, What)
    SRowse,3.4.26,Created Class
    """
    # Read File Info - When the program starts, read the file data into a list of lists (table)
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):

        """ This function reads the .json file into memory
            ChangeLog: (Who, When, What)
            SRowse,3.4.26,Created function
            :return: Student data
        """
        file = None
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except Exception as e:
            print("Error: There was a problem with reading the file.")
            print("Please check that the file exists and that it is in a json format.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data in memory to the .json file
            ChangeLog: (Who, When, What)
            SRowse,3.4.26,Created function
            :return: none
        """
        file = None
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem writing to the file.", error=e)
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()


#----------------------------------------------------------------------------------------------------

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output
    ChangeLog: (Who, When, What)
    SRowse,3.4.26,Created Class
    SRowse,3.4.26,Added menu output and input functions
    SRowse,3.4.26,Added a function to display the data
    SRowse,3.4.26,Added a function to display custom error messages
    """
    @staticmethod
    def printMenu(menu: str):
        """
        A function that prints the menu option
        ChangeLog: (Who, When, What)
        SRowse,3.4.26,Created Class
        output: MENU
        """
    # Present the menu of choices
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        A function that prints the menu option
        ChangeLog: (Who, When, What)
        SRowse,3.4.26,Created Class
        output: menu choice
        """
        menuchoice = input("What would you like to do? ")
        return menuchoice

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        A function that outputs an error message
        ChangeLog: (Who, When, What)
        SRowse,3.4.26,Created Class
        output: error message
        """
        print(e)  # Prints the custom message
        print("-- Technical Error Message -- ")
        print(e.__doc__)
        print(e.__str__())

    @staticmethod #chioce1
    def input_student_data(student_data: list):
        """
        A function that takes user input to write to memory
        ChangeLog: (Who, When, What)
        SRowse,3.4.26,Created Class
        output: student data to memory
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            new_student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(new_student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages
        except Exception as e:
            IO.output_error_messages
        return student_data

    @staticmethod # choice2
    def output_student_courses(student_data: list):
        """
        A function that prints data in memory
        ChangeLog: (Who, When, What)
        SRowse,3.4.26,Created Class
        output: student data to memory
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)


# -----------Present and Process the data--------------------------------------------------
# ----------End of function definitions------------------------------------------------------

# Beginning of the main body of this script
# "FileProcessor" class defined above - read_data_from_file is function from above

#             class               function        Arg                         Arg
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)


while (True):

    #menu print here
    # Present the menu
    IO.printMenu(menu=MENU)
    # Present prompt for choices
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue


    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
