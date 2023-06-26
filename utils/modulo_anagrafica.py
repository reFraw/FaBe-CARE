from .frontend import Bcolors
from .frontend import createAnagraficaScreen
from .frontend import createMainScreen

from.functional import getAnagrafica

import pandas as pd

from tabulate import tabulate

import os

def anagrafica(ruolo, engine):

    if ruolo == 4 or ruolo == 3:
        print(Bcolors.FAIL + "\n[ERROR] Sorry, you don't have permissions...\n" + Bcolors.ENDC)

    else:

        createAnagraficaScreen()

        res = getAnagrafica(engine, ruolo)
        print("\n")
        print(tabulate(res, headers='keys', tablefmt='psql'))
        print("\n")
        waiter = input("\n[INFO] Press ENTER to continue...")
        os.system("cls")
        createMainScreen()
