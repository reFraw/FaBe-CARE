from utils.frontend import createLogo
from utils.frontend import Bcolors
from utils.frontend import fakeBuild
from utils.frontend import createMainScreen

from utils.functional import getEngine
from utils.functional import getUserInfo
from utils.functional import getRole
from utils.functional import checkUser

from utils.modulo_anagrafica import anagrafica
from utils.modulo_storia_clinica import storia_clinica
from utils.modulo_analisi import analisi
from utils.modulo_urgenze import urgenze

import os
import argparse

from time import sleep


def parse_args():
    parser = argparse.ArgumentParser(prog='FaBE-CARE', description='Future of advanced Biomedical Electronic CARE')
    group = parser.add_argument_group('Arguments')

    group.add_argument('-u', '--user', required=False, type=str, help="Username for connection")
    group.add_argument('-r', '--root', required=False, type=str, help="Root mode")

    arguments = parser.parse_args()

    return arguments

if __name__ == "__main__":

    os.system("cls")
    args = parse_args()

    if args.root == 'y' and args.user is None:
        os.system("cls")
        os.chdir("C:/Program Files/MySQL/MySQL Server 8.0/bin") # INSERIRE PERCORSO MYSQL
        os.system("mysql -u root -p -D fabecare_db")

    else:
        user = args.user
        checkuser = checkUser(user)

        if checkuser == 0:
            print(Bcolors.FAIL + "\n\n[ERROR] This user doesn't exists...\n\n" + Bcolors.ENDC)
            quit()

        if args.user == 'p.romano':
            fakeBuild()
            print("\n")
            os.chdir("C:/Program Files/MySQL/MySQL Server 8.0/bin")  # INSERIRE PERCORSO MYSQL
            os.system("mysql -u p.romano -p -D fabecare_db")

        else:

            pw = getUserInfo()
            role = getRole(user)

            engine = getEngine(user, pw)

            fakeBuild()

            createMainScreen()

            while True:
                choice = input("[INFO] Insert input >>> ")

                if choice == '1':
                    anagrafica(role, engine)
                elif choice == '2':
                    analisi(role, engine)
                elif choice == '3':
                    storia_clinica(role, engine)
                elif choice.lower() == '00':
                    os.system("cls")
                    print(Bcolors.OKGREEN + "\n\n[BYE] Thank you for using FaBE-CARE ;)\n\n" + Bcolors.ENDC)
                    sleep(2)
                    os.system("cls")
                    quit()
                elif choice == '4':
                    urgenze(role, engine)
                else:
                    print(Bcolors.FAIL + "\n[ERROR] Invalid entry. Please retry...\n" + Bcolors.ENDC)

            pass