import json
import os

users = []

while True:
    print('*──────────────────Central Bank of Yemen──────────────────*')
    print('If you already have an account please enter login')
    print('If you do not have an account enter register')

    choice = input('>> ').strip().lower()

    # REGISTER
    if choice == 'register':
        ...
    elif choice == 'login':
        ...
    else:
        print('Invalid Input. Please try again.\n')