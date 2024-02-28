class Department:
    univ_students = 0
    def __init__(self, d_code, d_name, capacity, minGPA):
            self.d_code = d_code.upper()
            self.d_name = d_name
            self.capacity = capacity
            self.minGPA = minGPA
            self.univ_students = 0
            self.avgGPA = 0
            self.studentRoster = []
    def __str__(self):
        return f'Name: {self.d_name}, Code: ({self.d_code}), Capacity: {self.capacity}, Number of Students, {self.univ_students}'
    def addStudent(self, student_object):
        if not isinstance(student_object, Student):
            return False, 'Object is not part of Student class'
        if len(self.studentRoster) <= self.capacity:
            if self.isQualified(student_object)[0]:
                self.studentRoster.append(student_object)
                Department.univ_students += 1
                self.avgGPA += student_object.gpa() / Department.univ_students
                student_object.setMajor(self.d_code)
                return True, 'added'
            else:
                return False, self.isQualified(student_object)[1]
        else:
            return False, 'Department at capacity'
    def isQualified(self, student_object):
        if not isinstance(student_object, Student):
            return False, 'Object is not part of the Student Class'
        if student_object.enrolled == 'y':
            if student_object.gpa() >= self.minGPA:
                i = student_object.name
                for s in self.studentRoster:
                    if student_object.equals(s):
                        return False, 'Dupe'
                return True, 'qualified'
            else:
                return False, 'Student GPA is too low to enroll in this department'
        else:
            return False, 'Student is not currently enrolled'
    def listRoster(self):
        names = '['
        for s in self.studentRoster:
            names += str(s) + '; '
        print(names + ']')
class Student:
    totalEnrollment = 0
    def __init__(self, name, major='IST', enrolled='y', credits=0, qpoints=0): #initalizes the Student Class from pregiven info
        Student.totalEnrollment += 1
        self.g_num = 'G0000' + str(Student.totalEnrollment)
        self.name = name
        self.major = major
        self.enrolled = enrolled
        self.credits = credits
        self.qpoints = qpoints

    def __str__(self):
        return f"{self.name}, {self.g_num}, {self.classLevel()}, {self.major}, active: {self.enrolled}, credits = {self.credits}, gpa = {self.gpa()}"

    def gpa(self): #calculates the gpa and returns it
        if self.credits == 0:
            return 0
        else:
            return  self.qpoints / self.credits

    def addGrade(self, letterGrade, newCredits):
        letterGrade = letterGrade.upper()
        if newCredits == 0 or newCredits == 1 or newCredits == 2 or newCredits == 3 or newCredits == 4:
            if letterGrade == 'A' or letterGrade == 'B' or letterGrade == 'C' or letterGrade == 'D' or letterGrade == 'F':
                self.credits += newCredits
                if letterGrade == 'A':
                    self.qpoints += 4 * newCredits
                elif letterGrade == 'B':
                    self.qpoints += 3 * newCredits
                elif letterGrade == 'C':
                    self.qpoints += 2 * newCredits
                elif letterGrade == 'D':
                    self.qpoints += 1 * newCredits
                else:
                    self.qpoints += 0
                return True
            else:
                return False
        else:
            return False
    def isActive(self): #Checks to see if the student is actively enrolled
        if self.enrolled == 'y':
            return True
        else:
            return False
    def classLevel(self): #returns the year the student is in
        seniority = ''
        if self.credits >= 90:
            seniority = 'Senior'
        elif self.credits >= 60:
            seniority = 'Junior'
        elif self.credits >= 30:
            seniority = 'Sophomore'
        else:
            seniority = 'Freshman'
        return seniority
    def equals(self, other):
        return (self.g_num == other.g_num and self.name == other.name)
    def setMajor(self, newMajor):
        self.major = newMajor
        return True
if __name__ == '__main__':
    # --------------------------------------------------------------------------
    # IT209_A3_S24_testscript.py - IT-209 Assignment #3 (A3) test script
    #
    # The code below runs a number of tests of your Department and Student
    # classes and methods.  Most features are exercised, but the test is
    # not comprehensive and successful completion does not guarantee your
    # code is free of defects.
    # --------------------------------------------------------------------------

    # Copy/paste the following code into yours after your class definitions.
    # There are 14 tests that are run when prompted in order

    # Global/executable code ---------------------------------------------------

    print('\nStart of Department and Student class demo **************')
    input('\nTest1. Hit "Enter" to create 16 student objects for use in the demo ')
    s1 = Student('David Miller', major='Hist',
                 enrolled='y', credits=30, qpoints=90)
    s2 = Student('Emma Maria Vicente', major='Math',
                 enrolled='y', credits=90, qpoints=315)
    s3 = Student('Chris Squire', major='Musc',
                 enrolled='y', credits=45, qpoints=160)
    s4 = Student('Tal Wilkenfeld', major='ARTS',
                 enrolled='y', credits=70, qpoints=225)
    s5 = Student('Larry Graham', major='CHHS',
                 enrolled='y', credits=105, qpoints=315)
    s6 = Student('Dave Holland', major='CSci',
                 enrolled='y', credits=15, qpoints=39)
    s7 = Student('Esperanza Spalding', major='ENGR',
                 enrolled='y', credits=65, qpoints=250)
    s8 = Student('Tim Bogert', major='Hist',
                 enrolled='y', credits=45, qpoints=126)
    s9 = Student('Gordon Sumner', major='Musc',
                 enrolled='y', credits=15, qpoints=45)
    s10 = Student('Paul McCartney', major='ARTS',
                  enrolled='y', credits=110, qpoints=330)
    s11 = Student('Tina Weymouth', major='ENGR',
                  enrolled='y', credits=85, qpoints=250)
    s12 = Student('John McVie', major='Hist',
                  enrolled='y', credits=45, qpoints=126)
    s13 = Student('Nawt enrolled', major='Hist',
                  enrolled='n', credits=45, qpoints=120)
    s14 = Student('Toolow G. Peyay', major='Undc',
                  enrolled='y', credits=20, qpoints=38)
    s15 = Student('Stanley Clark', major='Chem',
                  enrolled='y', credits=95, qpoints=295)
    s16 = Student('Geddy Lee', major='Chem',
                  enrolled='y', credits=58, qpoints=143)

    print('\nList of Students created-------------------------------:\n ')
    print('s1=  ', s1)
    print('s2=  ', s2)
    print('s3=  ', s3)
    print('s4=  ', s4)
    print('s5=  ', s5)
    print('s6=  ', s6)
    print('s7=  ', s7)
    print('s8=  ', s8)
    print('s9=  ', s9)
    print('s10= ', s10)
    print('s11= ', s11)
    print('s12= ', s12)
    print('s13= ', s13)
    print('s14= ', s14)
    print('s15= ', s15)
    print('s16= ', s16)
    d1 = Department('ENGR', 'Engineering', 5, 3.0)
    d2 = Department('ARTS', 'Art and Architecture', 5, 2.5)
    d3 = Department('CHHS', 'College of Health and Human Services', 3, 2.75)
    d4 = Department('Hist', 'History Department', 5, 2.50)

    input('\n\nTest2. Hit "Enter" to see the list of 4 Department objects created ')
    print('\n\nDepartments established---------------------------------:')
    print(d1)
    print(d2)
    print(d3)
    print(d4)

    input('\n\n\nTest3. Hit "Enter" to add s1 - s5 to ENGR Department- print student list\n')
    d1.addStudent(s1)
    d1.addStudent(s2)
    d1.addStudent(s3)
    d1.addStudent(s4)
    d1.addStudent(s5)
    d1.listRoster()

    input('\n\n\n\nTest4. Hit "Enter" to add additional students to various departments -------------------:')
    a, b = d1.addStudent(s15)
    print('\nAttempting to add ', s15.name, ' to ', d1.d_code, ' result: ')
    print('\t\t\treturn values: ', a, '  reason code: ', b)
    print('\nDepartment ', d1.d_name, ' student list is now: ')
    d1.listRoster()

    input('\n\n\n\nTest5. Hit "Enter" to add two students to the ARTS Department ')
    print('\nAttempting to add ', s6.name, ' to ', d2.d_code, ' result: ')
    a, b = d2.addStudent(s6)
    print('\t\t\treturn values: ', a, '  reason code: ', b)
    print('\nAttempting to add ', s7.name, ' to ', d2.d_code, ' result: ')
    a, b = d2.addStudent(s7)
    print('\t\t\treturn values: ', a, '  reason code: ', b)
    d2.listRoster()

    input('\n\n\n\nTest6. Hit "Enter" to add two students to the CHHS Department')
    print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
    a, b = d3.addStudent(s8)
    print('\t\t\treturn values: ', a, '  reason code: ', b)
    print('\nAttempting to add ', s9.name, ' to ', d3.d_code, ' result: ')
    a, b = d3.addStudent(s9)
    print('\t\t\treturn values: ', a, '  reason code: ', b)
    d3.listRoster()

    input('\n\n\n\nTest7. Hit "Enter" to try adding a student with low GPA to CHHS')
    a, b = d3.addStudent(s14)
    print('\nAttempting to add ', s14.name, ' to ', d3.d_code, ' result: ')
    print('\t\t\treturn values: ', a, '  reason code: ', b)

    input('\n\n\n\nTest8. Hit "Enter" to try to add a non-enrolled student to the CHHS Department')
    print('\nAttempting to add ', s13.name, ' to ', d2.d_code, ' result: ')
    a, b = d2.addStudent(s13)
    print('\t\t\treturn values: ', a, '  reason code: ', b)

    input('\n\n\n\nTest9. Hit "Enter" to try adding a duplicate student ')
    print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
    a, b = d3.addStudent(s8)
    print('\t\t\treturn values: ', a, '  reason code: ', b)

    input('\n\n\n\nTest10. Hit "Enter" to add s10 to ENGR, s11 to ARTS, s12 to CHHS.')
    print('  then print all 4 department student lists')
    print('\nAttempting to add ', s10.name, ' to ', d1.d_code, ' result: ')
    a, b = d1.addStudent(s10)
    print('\t\t\treturn values: ', a, '  reason code: ', b)
    print('\nAttempting to add ', s11.name, ' to ', d2.d_code, ' result: ')
    a, b = d2.addStudent(s11)
    print('\t\t\treturn values: ', a, '  reason code: ', b)
    print('\nAttempting to add ', s12.name, ' to ', d3.d_code, ' result: ')
    a, b = d3.addStudent(s12)
    print('\t\t\treturn values: ', a, '  reason code: ', b)

    input('\n\n\n\nTest11. Hit "Enter" to try to add s16 to ARTS, which will fail for low gpa, ')
    print('    then add a new course grade of "A"/3 credits to s15, and try the add again.')
    print('\nStudent to be added to ARTS is ', s16)
    a, b = d2.addStudent(s16)
    print('\nResult of attempt to add ', s16.name, ' gpa: ', str(s16.gpa()), ' to ', d2.d_code)
    print('\tis ', a, ', with reson code: ', b)

    input('\n\n\n\nTest12. Adding 3 credit course with grade of "A" to ' + s16.name)
    s16.addGrade("A", 3)
    print('\nStudent profile is now: ', s16)
    a, b = d2.addStudent(s16)
    print('\nResult of second attempt to add ', s16.name, ' to ', d2.d_code)
    print('\tis ', a, ', with reason code:  ', b)
    print('\nNote: ', s16.name, ' is now a ', s16.classLevel(), ' with gpa ', str(s16.gpa()))

    input('\n\n\n\nTest13. Hit "Enter" to add s15 to ARTS.')
    print('\nAttempting to add ', s15.name, ' to ', d2.d_code, ' result: ')
    a, b = d2.addStudent(s15)
    print('\t\t\treturn values: ', a, '  reason code: ', b)

    input('\n\n\n\nT14Hit "Enter" to see the final student list for all departments')
    print('\nNumber of students in ', d1.d_code, ' is ', len(d1.studentRoster))
    d1.listRoster()
    print('\nNumber of students in ', d2.d_code, ' is ', len(d2.studentRoster))
    d2.listRoster()
    print('\nNumber of students in ', d3.d_code, ' is ', len(d3.studentRoster))
    d3.listRoster()
    print('\nNumber of students in ', d4.d_code, ' is ', len(d4.studentRoster))
    d4.listRoster()

    print('\n\n\n***** End of A3 F23 Output **********')
