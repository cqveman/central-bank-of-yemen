import datetime

def validate(value, check, errorMessage):
    while True:
        if check(value):
            return value
        value = input('\n' + str(errorMessage) + '\n')

def nameValidator(name):
    if name.replace(' ', '').replace('-', '').isalpha():
        return True
    return False

def dofValidator(date):
    if len(date) == 10 and date[2] == '-' and date[5] == '-':
        noDashesDate = date.replace('-', '')
        if noDashesDate.isdigit():
            # Assume all months have 31 days
            if (
                    1 <= int(noDashesDate[:2]) <= 31
                    and 1 <= int(noDashesDate[2:4]) <= 12
                    and 1900 <= int(noDashesDate[4:]) < datetime.datetime.now().year
            ):
                return True
    return False

def genderValidator(gender):
    if gender == 'Male' or gender == 'Female':
        return True
    return False

def jobValidator(job):
    if job.replace(' ', '').isalpha():
        return True
    return False

def addressValidator(address):
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
                return True
    return False

def phoneValidator(phNum):
    if phNum.isdigit() and len(phNum) == 9 and int(phNum[0]) == 7:
        return True
    return False

def emailValidator(email):
    if email.count('@') == 1:
        if email.rfind('.') > email.find('@'):
            # Assume min length is "a@b.c"
            if len(email) >= 5:
                return True
    return False

def usernameValidator(username, users):
    for user in users:
        if user.get("username") == username:
            return False

    return True

def passwordValidator(password):
    if ' ' not in password:
        if any(char.isdigit() for char in password):
            if len(password) >= 8:
                return True
    return False

def loginValidator(username, password, users):
    for user in users:
        if user.get('username') == username:
            if user.get('password') == password:
                return user
    return -1