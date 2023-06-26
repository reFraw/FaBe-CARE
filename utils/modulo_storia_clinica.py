from .frontend import Bcolors
from .frontend import createStoriaClinicaScreen
from .frontend import createMainScreen

from.functional import getStoriaClinica

import pandas as pd

from tabulate import tabulate

import os

def storia_clinica(ruolo, engine):

    if ruolo == 4 or ruolo == 3:
        print(Bcolors.FAIL + "\n[ERROR] Sorry, you don't have permissions...\n" + Bcolors.ENDC)

    else:

        createStoriaClinicaScreen()

        res = getStoriaClinica(engine, ruolo)
        print("\n")
        print(tabulate(res, headers='keys', tablefmt='psql'))
        print("\n")
        waiter = input("\n[INFO] Press ENTER to continue...")
        os.system("cls")
        createMainScreen()