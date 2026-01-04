import os

from util.validators import *
from util.helpers import *

users = []

fileName = 'data/users.json'
if os.path.exists(fileName) and os.path.getsize(fileName) > 2:
    with open(fileName, 'r') as f:
        users = json.load(f)

currentUser = -1

while True:
    print('*──────────────────Central Bank of Yemen──────────────────*')
    print('If you already have an account please enter login')
    print('If you do not have an account enter register')

    choice = input('>> ').strip().lower()

    # REGISTER
    if choice == 'register':
        print('\n#────────Sign-up────────#')
        print('Please fill in your personal information: ')

        # User Input
        fullName = input('Full Name: ').strip().title()
        dateOfBirth = input('Date of Birth (dd-mm-yyyy): ').strip()
        gender = input('Gender: ').strip().capitalize()
        job = input('Job: ').strip().title()
        address = input('Address (building #, Street Name, Neighbourhood, City-Postal Code): ').strip()
        phoneNum = input('Phone number (+967): ').strip()
        email = input('Email (example@gmail.com): ').strip()

        waitingAnimation('Validating Information', 1)

        # Validations
        fullName = validate(fullName, nameValidator, 'Invalid Full Name. Only alphabetic characters allowed, try again:')
        dateOfBirth = validate(dateOfBirth, dofValidator, 'Invalid Date of Birth. Only integer values allowed in the formatB of "dd-mm-yyyy", try again:')
        gender = validate(gender, genderValidator, 'Invalid Gender. Enter either male or female:')
        job = validate(job, jobValidator, 'Invalid Job. Only alphabetic characters allowed, try again:')
        address = validate(address, addressValidator, 'Invalid Address. Please use this format "building #, Street Name, Neighbourhood, City-Postal Code":')
        phoneNum = validate(phoneNum, phoneValidator, 'Invalid Phone Number. Omit +967 and enter 9 digits counting from "7":')
        email = validate(email, emailValidator, 'Invalid Email. Please use this format "example@gmail.com":')

        username = input('Username: ').strip()
        waitingAnimation('Checking Availability', 1, 3)
        username = validate(
            username,
            lambda x: usernameValidator(x, users),
            '✘ Username is taken. Please try again:'
        )

        password = input('Password: ')
        waitingAnimation('Validating Password', 1, 3)
        password = validate(
            password,
            passwordValidator,
            'Invalid Password. must be at least 8 characters long, contain at least one number, and include no spaces. Try again:'
        )

        users.append(
            {
                'username': username,
                'full name': fullName,
                'date of birth': dateOfBirth,
                'gender': gender,
                'job': job,
                'address': address,
                'phone number': phoneNum,
                'email': email,
                'password': password,
                'balance': 0.0
            }
        )

        saveToJson(fileName, users)
        waitingAnimation('Registering User', 1, 2)
        print('Sign-up successful, your id is ' + str(len(users)))

    elif choice == 'login':
        print('\n#────────Log-in────────#')

        username = input('Username: ').strip()
        password = input('Password: ')

        currentUser = loginValidator(username, password, users)
        try:
            if currentUser.get('username') == username:
                break
        except (ValueError, AttributeError):
            print('\nInvalid Username or Password. Please try again.\n')
            continue
    else:
        print('Invalid Input. Please try again.\n')

while True:
    print(f'\n*──────────────────{currentUser.get('full name')}\'s Dashboard──────────────────*')
    print("[1] Deposit")
    print("[2] Withdraw")
    print("[3] Transfer")
    print("[4] Check balance & personal info")
    print("[5] Exit")

    try:
        choice = int(input('>> '))
    except ValueError:
        print('\nInvalid Choice. Please enter 1 to 5.')
        continue

    # DEPOSIT
    if choice == 1:
        print('\n#────────Deposit────────#')

    # WITHDRAW
    elif choice == 2:
        print('\n#────────Withdraw────────#')

    # TRANSFER
    elif choice == 3:
        print('\n#────────Transfer────────#')

    # ACCOUNT
    elif choice == 4:
        print('\n#────────Account Details────────#')
        print(f'Username: {currentUser.get('username')}')
        print(f'Full Name: {currentUser.get('full name')}')
        print(f'Date of Birth: {currentUser.get('date of birth')}')
        print(f'Job: {currentUser.get('job')}')
        print(f'Address: {currentUser.get('address')}')
        print(f'Phone Number: +967 {currentUser.get('phone number')}')
        print(f'Email: {currentUser.get('email')}')
        print(f'Password: {currentUser.get('password')}')
        print(f'Balance: {currentUser.get('balance')}')

    # EXIT
    elif choice == 5:
        print('Buh Bye :)')
        break