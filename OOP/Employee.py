class Employee:

    raise_amt = 1

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.replace(" ", "").lower() + last.lower() + '@email.com'
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.025

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang



class Manager(Employee):
    raise_amt = 1.05

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name())



dev_1 = Developer('Dwayne', 'Lincoln', 3500, 'Java')
dev_2 = Developer('Gabriel Hernandes', 'Ferraz', 6700, 'Python')

mngr_1 = Manager('Rafaela', 'Souza', 15600, [dev_1])

print(mngr_1.email)
mngr_1.print_emps()

mngr_1.add_emp(dev_2)
mngr_1.remove_emp(dev_1)
mngr_1.print_emps()