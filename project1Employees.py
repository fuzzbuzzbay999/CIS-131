'''
script: cis131_lab_abstract_class_and_methods.py
action: A class hierarchy example
Author: Declan Juliano
Date:   10/14/2025
'''
from abc import ABC, abstractmethod
from IPython import embed

#embed()
# Abstract person class
class Person(ABC):
    def __init__(self, first, last, id, email,phone):
        try:
            self._first = first
            self._last = last

            if(len(str(id)) ==4 and str(id).isdigit()):
                self._id = int(id)
            else:
                raise ValueError("Id must be 4 digits")
            
            self._email = email

            if(len(str(phone))==12):
                self._phoneNumber = phone
            else:
                raise ValueError("Phone number must be 12 characters")
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

# Get name id number
    @property
    def idNumber(self):
        return self._id
    
# Get email
    @property
    def emailAddress(self):
        return self._email
    
# Get phone number
    @property
    def phoneNumber(self):
        return self._phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phone):
        if (len(str(phone))==12):
            self._phoneNumber = phone
        else:
            print("Phone number must be in the format xxx-xxx-xxxx. Nothing changed.")
    # print
    def __repr__(self):
        return f'{self._first}, reporting for duty'

#employee
class Employee(Person):
    # Variables
    from datetime import date

    roleDictionary = {'001':'Staff', '002':'Faculty'}
    classificationDictionary = {'001':'Full', '002':'Part'}

    def __init__(self, first: str, last: str, id: int|str, email: str,phone: str, month: int,day: int, year: int, salary: float,role: str, classification: str):

        super().__init__(first, last, id, email,phone)
        try:
            self._hireDate = date(year,month,day)
            print(self._hireDate)

            if(salary >=0):
                self._annualSalary = round(salary,2)
            else:
                raise ValueError("Annual salary must be >=0")
            
            isRole = [key for key, val in self.roleDictionary.items() if val == role]
            if(isRole):  
                self._role = isRole
            else:
                raise ValueError("Role must be in roleDictionary",self.roleDictionary,role)
            
            isClassification = [key for key, val in self.classificationDictionary.items() if val == classification]
            if(isClassification):
                self._classification = isClassification
            else:
                raise ValueError("Classification must be in classificationDictionary",self.classificationDictionary)
        except Exception as e:
            print("Errors have occured, reexecuting the class call is recomended. Reason:",e)
            raise
        
    # get hire date 
    @property
    def annualSalary(self):
        return self._annualSalary
    @annualSalary.setter
    def annualSalary(self,salary):
        if (salary >=0):
            self._annualSalary = round(salary,2)
        else:
            print("Salary must not be negative. Nothing changed")

    @property
    def rolePerson(self):
        return self.roleDictionary.get(str(self._role))
    @rolePerson.setter
    def rolePerson(self,role):
        if(role in self.roleDictionary):  
            self._role = self.roleDictionary[role]
        else:
            print("Role must be in roleDictionary",self.roleDictionary, "Nothing changed")

    @property
    def classificationPerson(self):
        return self.classificationDictionary.get(str(self._classification))
    @classificationPerson.setter
    def classificationPerson(self,classification):
        if(classification in self.classificationDictionary):  
            self._classification = self.classificationDictionary[classification]
        else:
            print("Role must be in roleDictionary",self.classificationDictionary, "Nothing changed")
        
    @property
    def hireDate(self):
        return self._hireDate
    


'''
processing the data

'''
from datetime import date
import re
 
employeeList = []

def getEmployees():
    global employeeList
    employees = open("employees.txt")
    for i in employees.readlines():
        employee=re.sub(r'[\t /]+',',',i).split(',')
        
        if(len(employee)==11):
            first = employee[0]
            last = employee[1]
            id = int(employee[2])
            email = employee[3]
            phone = employee[4]
            month = int(employee[5])
            day = int(employee[6])
            year = int(employee[7])
            classification= employee[8]
            role = employee[9]
            salary = float(employee[10])
            try:
                emp = Employee(first,last,id,email,phone,month,day,year,salary,role,classification)
                employeeList.append(emp)
            except Exception as e:
                print ('skipping employee')

            print(f'Added employee {first} {last} as clas {classification} and  role {role}')

            


'''
Output
'''
from datetime import date
def createMenu(num,items,):
    for i in range(0,num):
        print(f'{i+1}. {items[i]}')
    chosen(int(input()))

def chosen(index):
    match index:
        case 1:
            print("Thank you for using the system. ")
            print("Now exiting the program…")
        case 2:
            print(f'{"LastName":<20}{"FirstName":<20}{"ID":<20}{"Email":<30}{"Phone":<20}{"HireDate":<20}{"Classification":<20}{"Role":<20}{"Salary":<20}')
            for emp in employeeList:
                
                print(f'{emp.lastName:<20}{emp.firstName:<20}{emp.idNumber:<20}{emp.emailAddress:<30}{emp.phoneNumber:<20}{str(emp.hireDate):<20}{str(emp.classificationPerson):<20}{str(emp.rolePerson):<20}{emp.annualSalary:<20.2f}')        
        case 3:
            print(f'{"LastName":<20}{"FirstName":<20}{"ID":<20}{"Phone":<20}')
            for emp in employeeList:
                
                print(f'{emp.lastName:<20}{emp.firstName:<20}{emp.idNumber:<20}{emp.phoneNumber:<20}')
        
getEmployees()
createMenu(3,['quit','employee optiuons','em,ployee cobtact'])

embed()