'''
script: project1Employees.py
action: A menu driven application, that reads a supplied text file and stores it to classes. Then uses text based navigation to view and manipulate the data. 
Author: Declan Juliano
Date:   10/29/2025
    Ammended 10/30/2025
            Added the student class, cleaned up the createMenu() function
    Ammended 12/02/2025
            Added student scores functionality
    Ammended 12/09/2025
            Changed option 6 for grade report to show high, low, average per subject and overall high low average and letter grade
            Added lookup by ID functionality
            Added honor roll functionality
'''

# Imports
from abc import ABC, abstractmethod
from IPython import embed
from datetime import date
import re

isRunning = True    # Global state flag
#**************Abstract person class**************
class Person(ABC):
    # define the class (first, last, id, email, phone)
    def __init__(self, first, last, id, email, phone):
        """Initialize Person
            args: abstract
        """
        # If any of the checks throw an error raise it and continue
        try:
            self._first = first
            self._last = last

            # If id is not 4 digits error
            if(len(str(id)) == 4 and str(id).isdigit()):
                self._id = int(id)
            else:
                raise ValueError("Id must be 4 digits")
            
            self._email = email

            # If phone is not 12 chars error
            if(len(str(phone)) == 12):
                self._phoneNumber = phone
            else:
                print(phone)
                raise ValueError("Phone number must be 12 characters")
                
            
        # Print errors and raise further
        except Exception as e:
            print("Errors have occured, reexecuting the class call is recomended. Reason:" , e)
            raise

    # Get first name        
    @property
    def firstName(self):
        """Returns the first name
        args: none
        """
        return self._first
    @firstName.setter
    def firstName(self,first):
        """Sets the first name
        args: first (str): first name
        """
        self._first = first

    # Get last name
    @property
    def lastName(self):
        """Returns the last name
        args: none
        """
        return self._last
    @lastName.setter
    def lastName(self,last):
        """Sets the last name
        args: last (str): last name
        """
        self._last = last

    # Get id number
    @property
    def idNumber(self):
        """Returns the ID number
        args: none
        """
        return self._id
    
    # Get email
    @property
    def emailAddress(self):
        """Returns the email address
        args: none
        """
        return self._email
    
    # Get phone number (if changing and its not 12 digits dont change it)
    @property
    def phoneNumber(self):
        """Returns the phone number
        args: none
        """
        return self._phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phone):
        if (len(str(phone)) == 12):
            self._phoneNumber = phone
        else:
            print("Phone number must be in the format xxx-xxx-xxxx. Nothing changed.")
    
    # Print
    def __repr__(self):
        """Returns the representation of the person
        """
        return f'{self._first} {self._last} {self._email}'
    def __str__(self):
        """Returns the string of the person
        """
        return f'{self._first} {self._last}'

#**************employee**************
class Employee(Person):
    # Imports
    from datetime import date

    # Dictionaries for role and classification 
    roleDictionary = {'001':'Staff', '002':'Faculty'}
    classificationDictionary = {'001':'Full', '002':'Part'}

    # Define the class with people(first, last, id, email, phone) and This(month, day, year, salary, role, classification)
    def __init__(self, first: str, last: str, id: int|str, email: str,phone: str, month: int,day: int, year: int, salary: float,role: str, classification: str):
        """Initialize Employee
            args: first (str): first name
                  last (str): last name
                  id (int|str): 4 digit id number
                  email (str): email address
                  phone (str): phone number in the format xxx-xxx-xxxx
                  month (int): hire month
                  day (int): hire day
                  year (int): hire year
                  salary (float): annual salary >=0
                  role (str): role in roleDictionary
                  classification (str): classification in classificationDictionary
        """
        # Use the parent
        super().__init__(first, last, id, email,phone)

        # If any of the checks fail, throw error
        try:
            # Hire date
            self._hireDate = date(year,month,day)

            # If salary is negative then error
            if(salary >= 0):
                self._annualSalary = round(salary,2)
            else:
                raise ValueError("Annual salary must be >=0")
            
            # Convert role (str) to the respective dict key (if it doesnt exist error)
            isRole = [key for key, val in self.roleDictionary.items() if val == role]
            if(isRole):  
                self._role = isRole
            else:
                raise ValueError("Role must be in roleDictionary",self.roleDictionary,role)
            
            # Convert classification (str) to the respective dict key (if it doesnt exist error)
            isClassification = [key for key, val in self.classificationDictionary.items() if val == classification]
            if(isClassification):
                self._classification = isClassification
            else:
                raise ValueError("Classification must be in classificationDictionary",self.classificationDictionary)
        
        # Print errors and raise further
        except Exception as e:
            print("Errors have occured, reexecuting the class call is recomended. Reason:",e)
            raise
    
    # Get hire date
    @property
    def hireDate(self):
        """Returns the hire date
        args: none
        """
        return self._hireDate
    
    # Get annual Salary (if changing and the salary is negative display why and dont change it)
    @property
    def annualSalary(self):
        """Returns the annual salary
        args: none
        """
        return self._annualSalary
    @annualSalary.setter
    def annualSalary(self,salary):
        """Sets the annual salary
        args: salary (float): annual salary >=0
        """
        if (salary >= 0):
            self._annualSalary = round(salary,2)
        else:
            print("Salary must not be negative. Nothing changed")
    
    # Get role (if changing it, and the role doesnt exist, display it and dont change it)
    @property
    def rolePerson(self):
        """Returns the role
        args: none
        """
        return self.roleDictionary.get(self._role[0])
    @rolePerson.setter
    def rolePerson(self,role):
        """Sets the role
        args: role (str): role in roleDictionary
        """
        isRole = [key for key, val in self.roleDictionary.items() if val == role]
        if(isRole):  
            self._role = isRole
        else:
            print("Role must be in roleDictionary",self.roleDictionary, "Nothing changed")
    
    # Get classification (if changing it, and the classificaiton doesnt exist, display it and dont change it)
    @property
    def classificationPerson(self):
        """Returns the classification
        args: none
        """
        return self.classificationDictionary.get(self._classification[0])
    @classificationPerson.setter
    def classificationPerson(self,classification):
        """Sets the classification
        args: classification (str): classification in classificationDictionary
        """
        isClassification = [key for key, val in self.classificationDictionary.items() if val == classification]
        if(isClassification):
            self._classification = isClassification
        else:
            print("Role must be in roleDictionary",self.classificationDictionary, "Nothing changed")

    # Print
    def __repr__(self):
        """Returns the representation of the employee
        """
        return f'{self._first} {self._last} {self._email}'
    def __str__(self):
        """Returns the string of the employee
        """
        return f'{self._first} {self._last}'

#**************student**************
class Student(Person):
    # List of valid courses
    courseNameList = ['Art', 'Latin', 'Greek', 'Mathematics', 'Science', 'Painting', 'Sculpting']
    
    # Define the class with people(first, last, id, email, phone)
    def __init__(self, first, last, id, email, phone):
        """Initialize Student
            args: first (str): first name
                  last (str): last name
                  id (int|str): 4 digit id number
                  email (str): email address
                  phone (str): phone number in the format xxx-xxx-xxxx
        """        # Use the parent
        super().__init__(first, last, id, email, phone)

        # instance dictionary for storing student scores
        self.courseStudentDict = {}

    # Set student scores (subjects[list of subjects], scores[list of scores])
    def setStudentScores(self,subjects,scores):
        """setStudentScores
            args: subjects (list): list of subjects
                  scores (list): list of scores
        """ 

        # Itterate through the subjects and scores using the subjects length
        for i in range(len(subjects)):
            try:
                # Get the current subject
                subject = subjects[i]
                # If the subject is valid and the score is between 0 and 100 add it to the dict, else add INVALID and raise error
                if(subject in self.courseNameList):
                    if(0<=int(scores[i])<=100):
                        self.courseStudentDict[subject] = scores[i]
                    else:
                        # Mark score as INVALID if out of range
                        self.courseStudentDict[subject] = 'NaN'
                        raise ValueError(f'{scores[i]} is an invalid score')
                else:
                    # Mark score as INVALID if the subject is not in allowed courses
                    self.courseStudentDict[subject] = 'NaN'
                    raise ValueError(f'{subject} was not found in allowed courses')
            except Exception as e:
                print("Errors have occured, reexecuting the function call is recomended. Reason:" , e)
    
    # Get student academics (returns list of scores from the dict)
    def getStudentAcedemicReport(self):
        """getStudentAcedemics
            args: none
            returns: list of scores
        """ 
        scores = list(map(float,self.courseStudentDict.values())) 
        high = round(max(scores))
        low = round(min(scores))
        avg = sum(scores)/(len(scores))
        if(avg>=90):
            grade = 'A'
        elif(avg>=80):
            grade = 'B'
        elif(avg>=70):
            grade = 'C'
        elif(avg>=60):
            grade = 'D'
        else:
            grade = 'F'
        scores = list(self.courseStudentDict.values())
        return scores+[high,low,avg,grade]



'''
Processing the data
'''

# Function to itterate through supplied text document and populate the list (File name to read)
def getEmployees(file): 
    """Populate the employeeList from a text document
        args: file (str): text document to read
    """

    global employeeList     # Ensure global control of employeeList
    employeeList = []       # Reset employeeList
    employees = open(file)  # Open the text document

    # Read all lines and itterate through them
    for i in employees.readlines():

        # Remove all (\t, ,/) symbols and their duplicates, and replace them with commas. Strip any new lines. Split allong the commas into a list
        employee = re.sub(r'[\t /]+',',',i).strip().split(',')
        
        # If the sliced line is not 11 or have atleast 1 digit discard it (doesnt have the proper data feilds. Either its missing them or its a heading)
        if(len(employee) == 11 and re.search(r'\d', i)):
            # Assign the list indecies to their variables (convert those that need to be int and float to such)
            last = employee[0]
            first = employee[1]
            id = int(employee[2])
            email = employee[3]
            phone = employee[4]
            month = int(employee[5])
            day = int(employee[6])
            year = int(employee[7])
            classification= employee[8]
            role = employee[9]
            salary = float(employee[10])

            # Atempt to make a new class object and append it to the employeeList. (if any errors are thrown durring initialization, then print them and skip the employee)
            try:
                emp = Employee(first,last,id,email,phone,month,day,year,salary,role,classification)
                employeeList.append(emp)
                print(f'Added employee {first} {last}')     # Display current progress
            except:
                print ('skipping employee')

            
# Function to itterate through supplied text document and populate the list (File name to read)
def getStudents(file):
    """Populate the studentList from a text document
        args: file (str): text document to read
    """
    global studentList      # Ensure global control of studentList
    studentList = []        # Reset student list
    students = open(file)   # Open the text document
    
    #  Read all lines and itterate through them
    for i in students.readlines():
            
            # Remove all (\t, ,/) symbols and their duplicates, and replace them with commas. Strip any new lines. Split allong the commas into a list
            student = re.sub(r'[\t /]+',',',i).strip().split(',')

            # If the sliced line is not 5 or have atleast 1 digit discard it (doesnt have the proper data feilds. Either its missing them or its a heading)
            if(len(student) == 5 and re.search(r'\d', i)):
                # Assign the list indecies to their variables (convert those that need to be int and float to such)
                last = student[0]
                first = student[1]
                id = int(student[2])
                email = student[3]
                phone = student[4]

                # Atempt to make a new class object and append it to the employeeList. (if any errors are thrown durring initialization, then print them and skip the employee)
                try:
                    std =  Student(last,first,id,email,phone)
                    studentList.append(std)
                    print(f'Added student {first} {last}')      # Display current progress
                except:
                    print('skipping student')

# Function to itterate through supplied text document and set student scores (File name to read)
def getStudentScores(file):
    """getStudentScores
        args: file (str): text document to read
        returns: none
    """
    # Open the text document
    gradeBook = open(file)
    heading = []
    # Read all lines and itterate through them
    for i in gradeBook.readlines():
        #  Remove all (\t, ,/) symbols and their duplicates, and replace them with commas. Strip any new lines. Split allong the commas into a list
        line = re.sub(r'[\t /]+',',',i).strip().split(',')
        # If the line has a digit its a score line, else its a heading line
        if re.search(r'\d', i):
            scores = line
            # Itterate through all students to find the matching id number
            for std in studentList:
                try:
                    # If the id numbers match set the scores for that student
                    if (int(std.idNumber) == int(scores[0])):
                        print(f'Setting scores for {std.firstName}')
                        # Set the student scores (heading[1::] = subjects, scores[1::] = scores)
                        std.setStudentScores(heading[1::],scores[1::])
                except:
                    print('error')
        else:
            heading = line

# Function to get the headings from the scores file (File name to read)
def getheadings(file):
    """getheadings
        args: file (str): text document to read
        returns: list of headings
    """
    lines = open(file).readlines()\
    # Remove all (\t, ,/) symbols and their duplicates, and replace them with commas. Strip any new lines. Split allong the commas into a list
    line = re.sub(r'[\t /]+',',',lines[0]).strip().split(',')
    return line[1::]

'''
Output
'''
# Function for the menu
# It is set up this way to allow for more modularity when presented with sub menus and what not
def createMenu():
    """Create the menu for user interaction
    """
    
    # Menu items
    items = ['Quit','Display Employee Employment Information','Display Employee Contact Information','Display Student Contact Information','Display All Person Contact Information','Display Full Student Academic report','Display Academic Report for one Student','Display Honor Roll']
    # Number of menu items
    num = len(items)
    
    # Display the numeric options using the above amounts
    def options(items):
        """Display the options to the user
            args: items (list): list of menu items
        """
        
        print('\n')
        print("Please select an option below\n")
        for i in range(0,num):
            print(f'{i+1}. {items[i]}')

    # Switch case for optioins
    def choices(index):
        """Select the action based on user input
            args: index (str): user input
        """
        match index:
            # Compare the number with the assosiated action
            case '1':    # Option 1
                print("Thank you for using the system. ")
                print("Now exiting the program…")
                global isRunning    # Ensure global control
                isRunning = False   # Trip the flag
                
            case '2':   # Option 2
                # Header
                print(f'{"LastName":<20}{"FirstName":<20}{"ID":<10}{"Email":<30}{"Phone":<20}{"HireDate":<20}{"Classification":<20}{"Role":<20}{"Salary":<20}')
                # Body
                for emp in employeeList:
                    print(f'{emp.lastName:<20}{emp.firstName:<20}{emp.idNumber:<10}{emp.emailAddress:<30}{emp.phoneNumber:<20}{str(emp.hireDate):<20}{str(emp.classificationPerson):<20}{str(emp.rolePerson):<20}{emp.annualSalary:<20.2f}')        
            
            case '3':   # Option 3
                # Header
                print(f'{"LastName":<20}{"FirstName":<20}{"ID":<10}{"Email":<30}{"Phone":<20}')
                # Body
                for emp in employeeList:
                    print(f'{emp.lastName:<20}{emp.firstName:<20}{emp.idNumber:<10}{emp.emailAddress:<30}{emp.phoneNumber:<20}')

            case '4':   # Option 4
                # Header
                print(f'{"LastName":<20}{"FirstName":<20}{"ID":<10}{"Email":<30}{"Phone":<20}')
                # Body
                for std in studentList:
                    print(f'{std.lastName:<20}{std.firstName:<20}{std.idNumber:<10}{std.emailAddress:<30}{std.phoneNumber:<20}')

            case '5':   # Option 5
                # Header              
                print(f'{"LastName":<20}{"FirstName":<20}{"ID":<10}{"Email":<30}{"Phone":<20}')
                # Body
                peorsonList = employeeList+studentList
                for p in peorsonList:
                    print(f'{p.lastName:<20}{p.firstName:<20}{p.idNumber:<10}{p.emailAddress:<30}{p.phoneNumber:<20}')

            case '6':   # option 6
                # Header              
                classes = list(getheadings('scores.txt')) # get the class headings
                courseGrades = [0.0]*len(classes)   # base list for number of classes used as a constant for the amount of class grades
                high = [0.0]*len(classes)       # initialize high list
                low = [101.0]*len(classes)      # set low to 101 so any score will be lower
                avg = [0.0]*len(classes)        # initialize average list

                classes = [f'{i:<15}' for i in classes]  # convert to fstring with proper spacing
                classes = ''.join(classes)

                print(f'{"LastName":<20}{"FirstName":<20}{"ID":<10}{classes}{"High":15}{"Low":15}{"Average":<15}{"Grade":<15}')
                # Body
                for std in studentList:
                    grades = [ f'{i:<15}' for i in std.getStudentAcedemicReport()]  # get the entire report and convert it to a fstring
                    grades = ''.join(grades)
                    courses = std.getStudentAcedemicReport()[0:len(courseGrades)]   # get the individual course grades

                    print(f'{std.lastName:<20}{std.firstName:<20}{std.idNumber:<10}{grades}')   # print the student info and grades

                    # iterate through courses and find the highest and lowest for each subject
                    for i in range(len(courses)):
                        # compare and set high and low
                        if(float(courses[i]) >= float(high[i])):
                            high[i] = courses[i]
                        if(float(courses[i]) <= float(low[i])):
                            low[i] = courses[i]
                    # accumulate the scores for each course into avg
                    avg = [float(x) + float(y) for x, y in zip(avg, courses)]

                # Calculate avg
                avg = [avg[i]/len(studentList) for i in range(len(avg))]
                high = [ f'{i:<15}' for i in high]  # convert high to fstring with proper spacing
                high = ''.join(high)

                low = [ f'{i:<15}' for i in low]  # convert low to fstring with proper spacing
                low = ''.join(low)
                
                avg = [ f'{i:<15}' for i in avg]  # convert avg to fstring with proper spacing
                avg = ''.join(avg)

                # print the individual course high low and avg
                print('')
                print(f'{"High":<50}{high}')
                print(f'{"Low":<50}{low}')
                print(f'{"Average":<50}{avg}')

            case '7': # option 7
                idFound = False   # flag for if the id was found
                while(not idFound):
                    # Prompt for student ID
                    print("Please enter the ID of the student or -1 to quit:")
                    id = input()
                    print('') # New line before the output
                    
                    # Itterate through all students to find the matching id number if found print the academic report
                    for std in studentList:
                        # If the id numbers match set the scores for that student
                        if (int(std.idNumber) == int(id)):
                            classes = list(getheadings('scores.txt')) # get the class headings
                            classes = [f'{i:<15}' for i in classes]   # convert to fstring with proper spacing
                            classes = ''.join(classes)
                            print(f'{"LastName":<20}{"FirstName":<20}{"ID":<10}{classes}{"High":15}{"Low":15}{"Average":<15}{"Grade":<15}')
                            grades = [ f'{i:<15}' for i in std.getStudentAcedemicReport()]  # get the entire report and convert it to a fstring
                            grades = ''.join(grades)
                            print(f'{std.lastName:<20}{std.firstName:<20}{std.idNumber:<10}{grades}')   # print the student info and grades
                            idFound = True # mark that we found the id to exit the loop

                    # If the id is -1 set idFound to exit the loop
                    if(int(id) == -1):
                        idFound = True
                    # If the id was not found prompt again
                    if(not idFound):
                        print('That is not an ID we have on record. Please try again or enter -1 to quit.')

            case '8': # option 8
                print(f'{"Honor Roll Report":>80}')
                print('') # New line before the output
                classes = list(getheadings('scores.txt')) # get the class headings
                classes = [f'{i:<15}' for i in classes]   # convert to fstring with proper spacing
                classes = ''.join(classes)
                print(f'{"LastName":<20}{"FirstName":<20}{"ID":<10}{classes}{"High":15}{"Low":15}{"Average":<15}{"Grade":<15}')
                for std in studentList:
                # If the id numbers match set the scores for that student
                    if (std.getStudentAcedemicReport()[-1] == 'A'):
                        
                        grades = [ f'{i:<15}' for i in std.getStudentAcedemicReport()]  # get the entire report and convert it to a fstring
                        grades = ''.join(grades)
                        print(f'{std.lastName:<20}{std.firstName:<20}{std.idNumber:<10}{grades}')   # print the student info and grades

            case _: # No choice for that input
                print(f"I am sorry, {index} is not an option")
    
    # display the options and prompt for input
    def getChoice():
        """Get the user choice
            args: none
        """
        options(items)
        return input()

    # While running call getChoice() and select the input
    while(isRunning):
        choice = getChoice()
        print('') # New line before the output
        choices(choice)


def main():
    # Variables
    employeeList = []   # List for all employees
    studentList = []    # List for all students



    # Populate employeeList and studentList and student scores
    getEmployees("employees.txt")
    getStudents("students.txt")
    getStudentScores("scores.txt")

    # Prompt the user with the options of (quit, employment info, contact info, student contact info, all contact info, student scores)
    createMenu()

main()