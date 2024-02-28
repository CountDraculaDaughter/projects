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
        #name2 = self.name.split(', ')
        #lastName = name2[0]
        #firstName = name2[1]
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
if __name__ == '__main__':
    input('\nHit "Enter" to create several objects and print their summaries\n')

    s1 = Student('Henry Miller', major='Hist',
                 enrolled='y', credits=0, qpoints=0)
    s2 = Student('Emma Maria Vicente', major='Math',
                 enrolled='y', credits=90, qpoints=315)
    s3 = Student('A. Einstein', major='Phys',
                 enrolled='y', credits=0, qpoints=0)
    s4 = Student('W. A. Mozart', major='Mus',
                 enrolled='n', credits=29, qpoints=105)
    s5 = Student('Emma Maria Vicente', major='CSci',
                 enrolled='y', credits=60, qpoints=130)
    s5.g_num = s2.g_num
    s6 = Student('Vincent Van Gogh', major='Art',
                 enrolled='y', credits=120, qpoints=315)
    print('\nThe following Student objects were created: \n')
    print('s1 = ', s1)
    print('s2 = ', s2)
    print('s3 = ', s3)
    print('s4 = ', s4)
    print('s5 = ', s5)
    print('s6 = ', s6)
    print('\nTotal number of students: ', Student.totalEnrollment)
    input('\n\n\n Hit "Enter" to run several tests of the class methods -----------')
    print('The gpa of ', s1.name, ' is ', s1.gpa(), '\n')
    print('Class standing of ', s4.name, ' is ', s4.classLevel())
    print('Class standing of ', s2.name, ' is ', s2.classLevel(), '\n')
    if s1.equals(s2):
        print(s1.name, ' and ', s2.name, ' are the same student')
    else:
        print(s1.name, ' and ', s2.name, ' are not the same student')
    if s2.equals(s5):
        print(s2.name, ' and ', s5.name, ' are the same student')
    else:
        print(s2.name, ' and ', s5.name, ' are not the same student\n')
    if s1.isActive():
        print(s1.name, ' is currently active')
    else:
        print(s1.name, ' is not currently active')
    if s4.isActive():
        print(s4.name, ' is currently active')
    else:
        print(s4.name, ' is not currently active\n')
    print('Adding grade of "A" for ', s4.name, ', result: ', s4.addGrade('A', 3))
    print('GPA of ', s4.name, ' is now ', s4.gpa())
    print('Class standing of ', s4.name, ' is now ', s4.classLevel())
    print('\nTrying to add bogus grade of "X" to ', s1.name, ' result: ', s1.addGrade('X', 3))
    print('\nEnd of A2 Student class demo')
