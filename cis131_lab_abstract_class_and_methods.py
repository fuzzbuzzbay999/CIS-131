'''
script: cis131_lab_abstract_class_and_methods.py
action: A class hierarchy example
Author: Declan Juliano
Date:   10/14/2025
'''
from abc import ABC, abstractmethod

# Abstract employee class
class Employee(ABC):
    def __init__(self, first, last, ssn):
        self._first = first
        self._last = last
        self._ssn = ssn
# Get first name        
    @property
    def first_name(self):
        return 
# Get last name
    @property
    def last_name(self):
        return self._last
# Get name (first + last)
    @property
    def name(self):
        return f"{self._first} {self._last}"
# Get ssn
    @property
    def ssn(self):
        return self._ssn
# Get earnings
    @abstractmethod
    def earnings(self):
        raise NotImplementedError("Subclasses must implement earnings method")
# Print
    def __repr__(self):
        return f"{self._first} {self._last}, SSN: {self.ssn}"


# salaried employee
class SalariedEmployee(Employee):
    def __init__(self, first, last, ssn, weekly_salary):
        super().__init__(first, last, ssn)
        self.weekly_salary = weekly_salary
# get weekly salary
    @property
    def weekly_salary(self):
        return self._weekly_salary
# Change weekly salary
    @weekly_salary.setter
    def weekly_salary(self, value):
        if value < 0:
            raise ValueError("Weekly salary must be non-negative")
        self._weekly_salary = value
# Get earnings
    def earnings(self):
        return self.weekly_salary
# Print
    def __repr__(self):
        return f"SalariedEmployee: {super().__repr__()}, Weekly Salary: ${self.weekly_salary:.2f}"

 # Hourly employee   
class HourlyEmployee(Employee):
    def __init__(self, first, last, ssn, hours, wage):
        super().__init__(first, last, ssn)
        self.hours = hours
        self.wage = wage
# Hours worked
    @property
    def hours(self):
        return self._hours
# change hours
    @hours.setter
    def hours(self, value):
        if not (0 <= value <= 168):
            raise ValueError("Hours must be between 0 and 168")
        self._hours = value
# get Wage
    @property
    def wage(self):
        return self._wage
# Change wage
    @wage.setter
    def wage(self, value):
        if value < 0:
            raise ValueError("Wage must be non-negative")
        self._wage = value
# Get earnings
    def earnings(self):
        if self.hours <= 40:
            return self.hours * self.wage
        else:
            overtime = self.hours - 40
            return 40 * self.wage + overtime * self.wage * 1.5
# Print
    def __repr__(self):
        return (f"HourlyEmployee: {super().__repr__()}, Hours: {self.hours}, "
                f"Wage: ${self.wage:.2f}")

# Try to create a class object of an abstract class
try:
    bob = Employee("Bob","Jones",123123)
    print(bob)
except Exception as e:
    print("You can't do that.",e)

# Create employees
print('')
Octavia = SalariedEmployee("Octavia","Melody",734235274,1832.62)
Aurry = HourlyEmployee("Aurelia","Celune",412575349,45,21.72)
Aura = HourlyEmployee("Lunar","Aura",7457831ew23,42,1523.01)
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
