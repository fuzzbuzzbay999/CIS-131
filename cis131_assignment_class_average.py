'''
script: cis131_lab_guess_the_number.py CIS 131 - lab 2
action: Class average program with sentinel-controlled iteration. once the sentinel is entered it will dump data to a text file.
Author: Declan Juliano
Date:   9/23/2025
'''

 # initialization phase
total = 0  # sum of grades
grades = [] # list to hold grades
grade_counter = 0 # number of grades entered
 # processing phase
grade = int(input('Enter grade, -1 to end: '))  # get one grade
while grade != -1:
    total += grade
    grades.append(str(grade)+'\n') # Add grade entered to the list
    grade_counter += 1
    grade = int(input('Enter grade, -1 to end: '))
    
    # termination phase
    if grade_counter != 0:
        average = total / grade_counter
        print(f'Class average is {average:.2f}')
        print(grades)

    else:
        print('No grades were entered')
    
#write the list of grades to grades.txt
writer = open("grades.txt",'w')
writer.writelines(grades)
writer.close