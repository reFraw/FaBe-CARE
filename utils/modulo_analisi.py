from .frontend import Bcolors
from .frontend import createParametriScreen
from .frontend import createMainScreen

from .functional import getParametri

from tabulate import tabulate

import matplotlib.pyplot as plt
from matplotlib import style

import os

def analisi(ruolo, engine):

    if ruolo == 0:

        createParametriScreen()

        res, tip = getParametri(engine)

        if tip != 'EEG':
            print("\n")
            print(tabulate(res, headers='keys', tablefmt='psql'))
            print("\n")

            print("ANALYTICS\n")
            print(res['VALORE'].describe())

            n_warn = len(res[res['WARNING'] == 'Y'])

            if n_warn >= 5:
                print(Bcolors.WARNING + f"\n[WARNING] Pay attention to the patient! No. of Warnings : {n_warn}" + Bcolors.ENDC)

        visual_choice = '?'
        while visual_choice not in ['y', 'n', '']:
            visual_choice = input("\n[INFO] Display parameters trend? [Y/n] >>> ")
            if visual_choice.lower() == 'n':
                break
            elif visual_choice.lower() == '' or visual_choice.lower() == 'y':
                if tip == 'EEG':
                    start_date = input("\n[INFO] Enter start date in the following format AAAA-MM-GG >>> ")
                    start_hour = input("[INFO] Enter start time in the following format HH:MM:SS >>> ")
                    stop_date = input("[INFO] Enter end date in the following format AAAA-MM-GG >>> ")
                    stop_hour = input("[INFO] Enter end time in the following format HH:MM:SS >>> ")

                    waiter = input("\n\n[INFO] Press ENTER to visualize...")

                    start_time = start_date + ' ' + start_hour
                    end_time = stop_date + ' ' + stop_hour

                    partial_eeg = res[(res['TIMESTAMP'] >= start_time) & (res['TIMESTAMP'] <= end_time)]

                    plt.figure()
                    figManager = plt.get_current_fig_manager()
                    figManager.window.showMaximized()
                    style.use('ggplot')
                    plt.plot(partial_eeg['TIMESTAMP'], partial_eeg['VALORE'])
                    plt.xlabel('Orario')
                    plt.show()

                else:
                    waiter = input("\n\n[INFO] Press ENTER to visualize...")
                    plt.figure()
                    figManager = plt.get_current_fig_manager()
                    figManager.window.showMaximized()
                    style.use('ggplot')
                    plt.plot(res['TIMESTAMP'], res['VALORE'])
                    plt.scatter(res['TIMESTAMP'], res['VALORE'], c='black')
                    plt.xlabel('Orario')
                    plt.show()


        else:
            pass

        waiter = input("\n[INFO] Press ENTER to continue...")
        os.system("cls")
        createMainScreen()

    else:
        print(Bcolors.FAIL + "\n[ERROR] Sorry, you don't have permissions...\n" + Bcolors.ENDC)