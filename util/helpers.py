import json
import time


def saveToJson(fName, users):
    with open(fName, 'w') as f:
        json.dump(users, f, indent=2)

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