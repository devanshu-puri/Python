class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay): #email can be created from first and last
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) #or self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test' , 'User', 60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)