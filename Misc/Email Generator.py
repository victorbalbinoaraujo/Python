import random

emails = ['gmail', 'outlook', 'yahoo', 'mail']
email = random.choice(emails)

first_name = str(input('Enter your first name: '))
middle_name = str(input('Enter your middle name: '))
last_name = str(input('Enter your last name: '))
age = str(input('Enter your age: '))

print(first_name.lower() + age + middle_name.lower() + last_name.lower() + '@' + email + '.com')