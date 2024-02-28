import datetime
class Employee:
    def __init__(self, employee_id, name, birth_year, birth_month, job_title, annual_salary):
        self.employee_id = employee_id
        self.name = name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.job_title = job_title
        self.annual_salary = annual_salary
    def hourly_rate(self):
        return float(self.annual_salary / 2080)
    def age(self):
        dateTime = datetime.datetime.now().__str__()
        current_year = int(dateTime[0:4])
        current_month = int(dateTime[5:7])
        if self.birth_month < current_month:
            return current_year - self.birth_year
        else:
            return current_year - self.birth_year - 1
    def can_retire(self):
        if self.age() > 70:
            return True
        else:
            return False
    def __str__(self):
        return (f'Employee ID:   {self.employee_id} \n Employee Name:   {self.name} \n Employee Birth Year:   {self.birth_year} \n Employee Birth Month:   {self.birth_month} \n Employee Job Title:   {self.job_title} \n Employee Annual Salary:   {self.annual_salary}')

if __name__ == '__main__':
    print('\nStart of Employee class demo')

    e1 = Employee('E34568', 'David Miller', 1996, 1, 'Accountant', 82000)
    e2 = Employee('E22154', 'Margarete Smith', 1972, 10, 'Vice President', 115000)
    e3 = Employee('E43344', 'Chase Snidley', 1992, 8, 'Salesman', 75000)
    e4 = Employee('E12157', 'Roone Arledge', 1979, 11, 'Lawyer', 92000)
    e5 = Employee('E00001', 'Abe Lincoln', 1940, 2, 'Former POTUS', 85000)

    print('e1 = ', e1)
    print('e2 = ', e2)
    print('e3 = ', e3)
    print('e4 = ', e4)
    print('e5 = ', e5)
    print('Hourly rate for ', e1.name, ' is ', e1.hourly_rate())
    print('Age of ', e1.name, ' is ', e1.age())
    print('Age of ', e3.name, ' is ', e3.age())
    print('Job description of ', e4.name, 'is ', e4.job_title)
    print('Retirement eligibility for ', e2.name, ' is ', e2.can_retire())
    print('Retirement eligibility for ', e5.name, ' is', e5.can_retire())

    print('\nEnd of Employee class demo')
