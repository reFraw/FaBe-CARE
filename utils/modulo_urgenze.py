from .functional import getEmergencies
from .functional import getFullEmergenciesData

from .frontend import Bcolors
from .frontend import createMainScreen, createEmergenciesScreen

from tabulate import tabulate

import os

def urgenze(ruolo, engine):

    if ruolo == 0:

        createEmergenciesScreen()

        res = getEmergencies(engine)
        print("EMERGENCIES\n")
        print(tabulate(res, headers='keys', tablefmt='psql'))
        print("\n")

        choice = '?'
        while choice not in ['y', 'n', '']:
            choice = input("\n[INFO] Get more info? [Y/n] >>> ")
            if choice.lower() == 'n':
                break
            elif choice.lower() == 'y' or choice.lower() == '':
                UID = input("[INFO] Insert patient UID >>> ")
                res2 = getFullEmergenciesData(engine, UID)
                print("\n")
                print(tabulate(res2, headers='keys', tablefmt='psql'))
                print("\n")

            else:
                print(Bcolors.FAIL + f"\n[ERROR] Invalid input..." + Bcolors.ENDC)

        waiter = input("\n[INFO] Press ENTER to continue...")
        os.system("cls")
        createMainScreen()

    else:
        print(Bcolors.FAIL + "\n[ERROR] Sorry, you don't have permissions...\n" + Bcolors.ENDC)