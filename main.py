import json
import os
import time
import datetime

users = [ ]

def waitingAnimation(message, seconds, option=1):
    symbols = []
    if option == 1:
        symbols = [
            '▒▒▒▒▒▒▒▒▒▒ 0%', '██▒▒▒▒▒▒▒▒ 20%', '████▒▒▒▒▒▒ 40%',
            '██████▒▒▒▒ 60%', '████████▒▒ 80%', '██████████ 100%'
        ]
    elif option == 2:
        symbols = ['○', '◔', '◑', '◕', '●']
    elif option == 3:
        symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    print()
    for i in symbols:
        print(f'\r{message} {i}', end='')
        time.sleep(seconds)
    print('\n')

while True:
    print('*──────────────────Central Bank of Yemen──────────────────*')
    print('If you already have an account please enter login')
    print('If you do not have an account enter register')

    choice = input('>> ').strip().lower()

    # REGISTER
    if choice == 'register':
        print('\n#────────Sign-up────────#')
        print('Please fill in your personal information: ')

        fullName = input('Full Name: ').strip().capitalize()
        dateOfBirth = input('Date of Birth (dd-mm-yyyy): ').strip()
        gender = input('Gender: ').strip().capitalize()
        job = input('Job: ').strip().capitalize()
        address = input('Address (building #, Street Name, Neighbourhood, City-Postal Code): ').strip().capitalize()
        phoneNum = input('Phone number (+967): ').strip()
        email = input('Email (example@gmail.com): ').strip()

        waitingAnimation('Validating Information', 1)

        while True:
            if fullName.replace(' ', '').replace('-','').isalpha():
                break
            fullName = input('\nInvalid Full Name. Only alphabetic characters allowed, try again:\n')

        while True:
            if len(dateOfBirth) == 10 and dateOfBirth[2] == '-' and dateOfBirth[5] == '-':
                noDashesDate = dateOfBirth.replace('-', '')
                if noDashesDate.isdigit():
                    # Assume all months have 31 days
                    if (
                            1 <= int(noDashesDate[:2]) <= 31
                            and 1 <= int(noDashesDate[2:4]) <= 12
                            and 1900 <= int(noDashesDate[4:]) < datetime.datetime.now().year
                    ):
                        break
            dateOfBirth = input('\nInvalid Date of Birth. Only integer values allowed in the format of "dd-mm-yyyy", try again:\n')

        while True:
            if gender == 'Male' or gender == 'Female':
                break
            gender = input('\nInvalid Gender. Enter either male or female:\n')

        while True:
            if job.replace(' ', '').isalpha():
                break
            job = input('\nInvalid Job. Only alphabetic characters allowed, try again:\n')

        while True:
            parts = address.split(', ')
            if len(parts) == 4:
                building = parts[0]
                street = parts[1]
                neighbourhood = parts[2]
                city = parts[3]
                if (
                        building.isdigit()
                        and street.replace(' ', '').replace('.', '').isalpha()
                        and neighbourhood.replace(' ', '').isalpha()
                ):
                    cityParts = city.split('-')
                    if len(cityParts) == 2 and cityParts[1].isdigit():
                        break
            address = input('\nInvalid Address. Please use this format "building #, Street Name, Neighbourhood, City-Postal Code":\n')

        while True:
            if phoneNum.isdigit() and len(phoneNum) == 9 and int(phoneNum[0]) == 7:
                break
            phoneNum = input('\nInvalid Phone Number. Omit +967 and enter 9 digits counting from "7":\n')

        while True:
            if email.count('@') == 1:
                if email.rfind('.') > email.find('@'):
                    # Assume min length is "a@b.c"
                    if len(email) >= 5:
                        break
            email = input('\nInvalid Email. Please use this format "example@gmail.com":\n')

        username = input('Username: ').strip()

        waitingAnimation('Checking Availability', 1, 3)

        while True:
            found = False
            for user in users:
                if user.get("username") == username:
                    found = True
                    break

            if not found:
                print('Username Available ✔')
                break

            username = input('✘ Username is taken. Please try again:\n')

        password = input('Password: ')

        while True:
            if ' ' not in password:
                if any(char.isdigit() for char in password):
                    if len(password) >= 8:
                        break
            password = input('Invalid Password. must be at least 8 characters long, '
                             'contain at least one number, and include no spaces.\nTry again: ')

    elif choice == 'login':
        ...
    else:
        print('Invalid Input. Please try again.\n')