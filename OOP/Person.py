from datetime import date

class Person:

    num_of_persons = 0
    raise_amt = 1

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.replace(" ", "").lower() + last.lower() + '@email.com'

        Person.num_of_persons += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod #Adicionando uma pessoa baseado numa string
    def from_string(cls, per_str):
        first, last, pay = per_str.split('-')
        pay = float(pay)
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


Person.set_raise_amt(1.04)

per_1 = Person('Anna Livia', 'Prado', 50000)
per_2 = Person('Clara Maria', 'Cardoso', 50000)
per_3 = Person('Victor Balbino', 'Araujo', 50000)

#Criando pessoa baseado em string
per_str_1 = 'Leticia-Nobrega-50000'
per_4 = Person.from_string(per_str_1)

people = [per_1, per_2, per_3, per_4]


for i in range(len(people)):
    people[i].apply_raise()
    print(f'Name : {people[i].full_name()}\nEmail : {people[i].email}\nSalary : R$ {people[i].pay}')
    print()
    print('-' * 10)
    print()   

my_date = date.today()
print(f'Today is {my_date}. Today is a workday? {Person.is_workday(my_date)}')

print()
