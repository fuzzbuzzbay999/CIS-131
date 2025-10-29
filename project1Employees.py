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
                raise ValueError("id must be 4 digits")
            
            self._email = email

            if(len(str(phone))==12):
                self._phoneNumber = phone
            else:
                raise ValueError("phone number must be 12 characters")
        except Exception as e:
            print("Errors have occured, reexecuting the class call is recomended" , e)

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
            raise  ValueError("phone number must be 12 characters")
    # print
    def __repr__(self):
        return "hi"

#employee
class Employee(Person):
    # Variables
    from datetime import date

    roleDictionary = {'staff':'001', 'Faculty':'002'}
    classificationDictionary = {'Full-Time':'001', 'Part-Time':'002'}
    def __init__(self, first: str, last: str, id: int|str, email: str,phone: int|str,hireDate: date, annualSalary: float,role: str, classification: str):
        super().__init__(first, last, id, email,phone)
        try:
            self._hireDate = hireDate 

            if(annualSalary >=0):
                self._annualSalary = annualSalary
            else:
                raise ValueError("annual salary must be >=0")
            
            if(role in self.roleDictionary):  
                self._role = self.roleDictionary[role]
            else:
                raise ValueError("role must be in roleDictionary")
            
            if(classification in self.classificationDictionary):
                self._classification = self.classificationDictionary[classification]
            else:
                raise ValueError("classification must be in classificationDictionary")
        except Exception as e:
            print("Errors have occured, reexecuting the class call is recomended",e)
# get hire date 
    def hireDate(self):
        return self._hireDate
    def rolePerson(self):
        return self._role
    def classificationPerson(self):
        return self._classification
    

    #get annual salary
    @property
    def annual_salary(self):
        return self._annualSalary

from datetime import date
from cis131_project1 import Person
bob = Employee('bob','jon',1223,'sdfsdff','520-490-7681',date(2002,3,20),12321,'staff','Full-Time')
print(bob.hireDate())
'''
# Create employees
print('')
Octavia = SalariedEmployee("Octavia","Melody",734235274,1832.62)
Aurry = HourlyEmployee("Aurelia","Celune",412575349,45,21.72)
Aura = HourlyEmployee("Lunar","Aura",745783123,42,1523.01)
Lyra = SalariedEmployee("Lyra","Heartstrings",47329250,2475.23)

# Print employees and their earnings sepreately
print(Octavia)
print(Octavia.earnings())
print(Aurry)
print(Aurry.earnings())
print(Aura)
print(Aura.earnings())
print(Lyra)
print(Lyra.earnings())
print('')

# List of employees
employees = [Octavia,Aurry,Aura,Lyra]

# Itterate through the list and print the employees and their earnings
for i in employees:
    print(i)
    print(i.earnings())

'''