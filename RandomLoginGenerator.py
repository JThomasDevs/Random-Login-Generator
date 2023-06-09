import random
import string


def rand_email():
    domains_list = ["gmail.com", "outlook.com", "hotmail.com"]   # Change this to whatever domain(s) you want
    first_name = first_names[random.randint(0, len(first_names) - 1)]   # Grab a first and last name from the lists
    last_name = last_names[random.randint(0, len(last_names) - 1)]      # each at a random index
    nums = str(random.randint(0, 9999))
    domain = random.choice(domains_list)
    if nums == 0:
        nums = ''
    email = f'{first_name}{last_name}{nums}@{domain}'
    return email


def rand_pass(length: int):
    characters = string.ascii_letters + string.digits + string.hexdigits
    password = ''.join(random.choices(characters, k=length))
    return password


first_names = []
last_names = []

with open('firstnames.txt', 'r') as firstnames:   # Read both files and append each line(name) to a list
    for line in firstnames:
        name = line.strip()
        first_names.append(name)
with open('lastnames.txt', 'r') as lastnames:
    for line in lastnames:
        name = line.strip()
        last_names.append(name)


valid_input = ['emails', 'passwords', 'both']
what_to_make = input("Would you like to generate emails, passwords, or both? ")

while what_to_make not in valid_input:   # Input validation
    print("Invalid input, please try again.")
    what_to_make = input("Would you like to generate emails, passwords, or both? ")


if what_to_make == 'emails':
    num_emails = int(input("How many emails would you like to generate? "))
    with open('emails.txt', 'a') as emails:
        for i in range(num_emails):
            emails.write(rand_email())
            if i != num_emails - 1:
                emails.write('\n')

elif what_to_make == 'passwords':
    num_passwords = int(input("How many passwords would you like to generate? "))
    pass_length = int(input("How many characters long would you like the passwords to be? "))
    with open('passwords.txt', 'a') as passwords:
        for i in range(num_passwords):
            passwords.write(rand_pass(pass_length))
            if i != num_passwords - 1:
                passwords.write('\n')

elif what_to_make == 'both':
    num_logins = int(input("How many logins would you like to generate? "))
    pass_length = int(input("How many characters long would you like the passwords to be? "))
    with open('logins.txt', 'a') as logins:
        for i in range(num_logins):
            logins.write(rand_email() + ':' + rand_pass(pass_length))
            if i != num_logins - 1:
                logins.write('\n')
