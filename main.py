from utils.frontend import createLogo
from utils.frontend import Bcolors
from utils.frontend import fakeBuild
from utils.frontend import createMainScreen

from utils.functional import getEngine
from utils.functional import getUserInfo
from utils.functional import getRole

from utils.modulo_anagrafica import anagrafica
from utils.modulo_storia_clinica import storia_clinica

import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(prog='FaBE-CARE', description='Future of advanced Biomedical Electronic CARE')
    group = parser.add_argument_group('Arguments')

    group.add_argument('-u', '--user', required=True, type=str, help="Username for connection")

    arguments = parser.parse_args()

    return arguments

if __name__ == "__main__":

    os.system("cls")
    args = parse_args()

    user = args.user
    pw = getUserInfo()
    role = getRole(user)

    engine = getEngine(user, pw)

    fakeBuild()

    createMainScreen()

    while True:
        choice = input("[INFO] Insert input >>> ")

        if choice == '1':
            anagrafica(role, engine)
            os.system('cls')
            createMainScreen()
        elif choice == '2':
            print("Work in progress")
        elif choice == '3':
            print("Work in progress")
        elif choice == '4':
            storia_clinica(role, engine)
            os.system('cls')
            createMainScreen()
        elif choice.lower() == '00':
            os.system("cls")
            print(Bcolors.OKGREEN + "[BYE] Thank you for using FaBE-CARE ;)\n\n" + Bcolors.ENDC)
            break
        else:
            print(Bcolors.FAIL + "\n[ERROR] Invalid entry. Please retry...\n" + Bcolors.ENDC)

    pass