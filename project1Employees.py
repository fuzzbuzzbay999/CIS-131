'''
script: project1Employees.py
action: A menu driven application, that reads a supplied text file and stores it to classes. Then uses text based navigation to view and manipulate the data. 
Author: Declan Juliano
Date:   10/29/2025
'''

# Imports
from abc import ABC, abstractmethod
from IPython import embed

#**************Abstract person class**************
class Person(ABC):
    # define the class (first, last, id, email, phone)
    def __init__(self, first, last, id, email, phone):

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
                raise ValueError("Phone number must be 12 characters")
            
            # Print errors and raise further
        except Exception as e:
            print("Errors have occured, reexecuting the class call is recomended. Reason:" , e)
            raise

# Get first name        
    @property
    def firstName(self):
        return self._first
    @firstName.setter
    def firstName(self,first):
        self._first = first

# Get last name
    @property
    def lastName(self):
        return self._last
    @lastName.setter
    def lastName(self,last):
        self._last = last

# Get id number
    @property
    def idNumber(self):
        return self._id
    
# Get email
    @property
    def emailAddress(self):
        return self._email
    
# Get phone number (if changing and its not 12 digits dont change it)
    @property
    def phoneNumber(self):
        return self._phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phone):
        if (len(str(phone)) == 12):
            self._phoneNumber = phone
        else:
            print("Phone number must be in the format xxx-xxx-xxxx. Nothing changed.")
    
    # Print
    def __repr__(self):
        return f'{self._first} {self._last} {self._email}'
    def __str__(self):
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
        return self._hireDate
    
    # Get annual Salary (if changing and the salary is negative display why and dont change it)
    @property
    def annualSalary(self):
        return self._annualSalary
    @annualSalary.setter
    def annualSalary(self,salary):
        if (salary >= 0):
            self._annualSalary = round(salary,2)
        else:
            print("Salary must not be negative. Nothing changed")
    
    # Get role (if changing it, and the role doesnt exist, display it and dont change it)
    @property
    def rolePerson(self):
        return self.roleDictionary.get(self._role[0])
    @rolePerson.setter
    def rolePerson(self,role):
        isRole = [key for key, val in self.roleDictionary.items() if val == role]
        if(isRole):  
            self._role = isRole
        else:
            print("Role must be in roleDictionary",self.roleDictionary, "Nothing changed")
    
    # Get classification (if changing it, and the classificaiton doesnt exist, display it and dont change it)
    @property
    def classificationPerson(self):
        return self.classificationDictionary.get(self._classification[0])
    @classificationPerson.setter
    def classificationPerson(self,classification):
        isClassification = [key for key, val in self.classificationDictionary.items() if val == classification]
        if(isClassification):
            self._classification = isClassification
        else:
            print("Role must be in roleDictionary",self.classificationDictionary, "Nothing changed")

    # Print
    def __repr__(self):
        return f'{self._first} {self._last} {self._email}'
    def __str__(self):
        return f'{self._first} {self._last}'



#**************student**************
class Student(Person):
    def __init__(self, first, last, id, email, phone):
        super().__init__(first, last, id, email, phone)
    


'''
Processing the data
'''

# Import
from datetime import date
import re

# Variables
employeeList = [] 
studentList = []


# Function to itterate through supplied text document and populate the list (File name to read)
def getEmployees(file): 
    global employeeList 
    employeeList = []       # Holds all employees
    employees = open(file)   # Open the text document

    # Read all lines and itterate through them
    for i in employees.readlines():

        # Remove all (\t, ,/) symbols and their duplicates, and replace them with commas. Split allong the commas into a list
        employee = re.sub(r'[\t /]+',',',i).split(',')
        
        # If the sliced line is not 11 or has atleast 1 digit discard it (doesnt have the proper data feilds. Either its missing them or its a heading)
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

            # Atempt to make a new class object and append it to the employeeList. (if any errors are thrown durring initialization, then print that and skip the employee)
            try:
                emp = Employee(first,last,id,email,phone,month,day,year,salary,role,classification)
                employeeList.append(emp)
            except:
                print ('skipping employee')
            
            # Display current progress
            print(f'Added employee {first} {last}')
def getStudents(file):
    global studentList
    studentList = []
    students = open(file)
    for i in students.readlines():
            student = re.sub(r'[\t /]+',',',i).split(',')
            if(len(student) == 5 and re.search(r'\d', i)):
                last = student[0]
                first = student[1]
                id = int(student[2])
                email = student[3]
                phone = student[4]
                try:
                    std =  Student(last,first,id,email,phone)
                    studentList.append(std)
                except:
                    print('skipping employee')
'''
Output
'''
# Import
from datetime import date

# Function for the menu, (num[amount of choices], items[list of what the items are])
# It is set up this way to allow for more modularity when presented with sub menus and what not
def createMenu(num,items):
    # Display the numeric options using the supplied amount and prompts
    def options():
        print('\n')
        print("Please select an option below\n")
        for i in range(0,num):
            print(f'{i+1}. {items[i]}')

    # Loop condition
    isRunning = True
    while(isRunning):
        # Print the options
        options()
        # Prompt the user for a number
        index = int(input())

        # Compare the number with the assosiated action
        if(index == 1):     # Option 1
            print("Thank you for using the system. ")
            print("Now exiting the program…")
            isRunning = False   # Stop the loop condition
            break               # Imediately break the loop to stop further execution

        elif(index == 2):   # Option 2
            # Header
            print(f'{"LastName":<20}{"FirstName":<20}{"ID":<20}{"Email":<30}{"Phone":<20}{"HireDate":<20}{"Classification":<20}{"Role":<20}{"Salary":<20}')
            # Body
            for emp in employeeList:
                print(f'{emp.lastName:<20}{emp.firstName:<20}{emp.idNumber:<20}{emp.emailAddress:<30}{emp.phoneNumber:<20}{str(emp.hireDate):<20}{str(emp.classificationPerson):<20}{str(emp.rolePerson):<20}{emp.annualSalary:<20.2f}')        
        
        elif(index == 3):   # Option 3
            # Header
            print(f'{"LastName":<20}{"FirstName":<20}{"ID":<20}{"Phone":<20}')
            # Body
            for emp in employeeList:
                print(f'{emp.lastName:<20}{emp.firstName:<20}{emp.idNumber:<20}{emp.phoneNumber:<20}')
        
        else:
            # No choice for that number
            print(f"I am sorry, {index} is not an option")

# Populate the employeeList
getEmployees("employees.txt")
getStudents("students.txt")
# Promp the user with the options of (quit, employment info, contact info)
createMenu(3,['Quit','Display Employee Employment Information','Display Employee Contact Information'])
