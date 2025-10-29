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

    roleDictionary = {'Staff':'001', 'Faculty':'002'}
    classificationDictionary = {'Full':'001', 'Part':'002'}

    def __init__(self, first: str, last: str, id: int|str, email: str,phone: str, month: int,day: int, year: int, salary: float,role: str, classification: str):

        super().__init__(first, last, id, email,phone)
        try:
            self._hireDate = date(year,month,day)

            if(salary >=0):
                self._annualSalary = round(salary,2)
            else:
                raise ValueError("Annual salary must be >=0")
            
            if(role in self.roleDictionary):  
                self._role = self.roleDictionary[role]
            else:
                raise ValueError("Role must be in roleDictionary",self.roleDictionary)
            
            if(classification in self.classificationDictionary):
                self._classification = self.classificationDictionary[classification]
            else:
                raise ValueError("Classification must be in classificationDictionary",self.classificationDictionary)
        except Exception as e:
            print("Errors have occured, reexecuting the class call is recomended. Reason:",e)
        
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
        return self._role
    @rolePerson.setter
    def rolePerson(self,role):
        if(role in self.roleDictionary):  
            self._role = self.roleDictionary[role]
        else:
            print("Role must be in roleDictionary",self.roleDictionary, "Nothing changed")

    @property
    def classificationPerson(self):
        return self._classification
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

            emp = Employee(first,last,id,email,phone,month,day,year,salary,role,classification)
            employeeList.append(emp)



getEmployees()

print(employeeList)
