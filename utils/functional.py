import sqlalchemy
import stdiomask

from sqlalchemy import text

import pandas as pd

from .roles import roles
from .roles import users

from tabulate import tabulate

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getEngine(user, pw):
    eng_str = f"mysql+mysqlconnector://{user}:{pw}@localhost:3306/fabecare_db"
    engine = sqlalchemy.create_engine(eng_str)

    return engine

def getUserInfo():
    check = 0

    while not check:
        pw = stdiomask.getpass("[INFO] Insert password >>> ", '*')
        if pw == 'ciao':
            check = 1
        else:
            print(Bcolors.FAIL + "\n[ERROR] Please check username and/or password..\n" + Bcolors.ENDC)

    return pw

def getRole(user):
    global roles

    for key in roles:
        if user in roles[key]:
            return key


def getAnagrafica(engine, ruolo):

    choice = ''

    print(Bcolors.OKCYAN + """
        SELECT AN OPTION
    
        [1] Complete patients registry
        [2] Search patient
            """ + Bcolors.ENDC)

    while choice != '1' and choice != '2':

        if ruolo == 2:

            while True:

                choice = input("\n[INFO] Select an option >>> ")

                if choice == '1':
                    query = text("SELECT IDP, NOME, COGNOME, DATA_NASCITA FROM pazienti")
                    with engine.connect() as conn:
                        res = pd.read_sql_query(query, conn)
                        return res
                elif choice == '2':
                    patient_id = input("\n[INFO] Input patient UID >>> ")
                    try:
                        query = text(f"SELECT IDP, NOME, COGNOME, DATA_NASCITA FROM pazienti WHERE IDP = '{patient_id}'")
                        with engine.connect() as conn:
                            res = pd.read_sql_query(query, conn)
                            return res
                    except Exception as e:
                        print(Bcolors.FAIL +  f"\n[ERROR] Something goes wrong. Error message : {e}\n" + Bcolors.ENDC)
                else:
                    print(Bcolors.FAIL + f"\n[ERROR] Invalid input...\n" + Bcolors.ENDC)

        else:
            choice = input("\n[INFO] Select an option >>> ")

            if choice == '1':
                query = text("SELECT * FROM pazienti")
                with engine.connect() as conn:
                    res = pd.read_sql_query(query, conn)
                    return res
            elif choice == '2':
                patient_id = input("\n[INFO] Input patient UID >>> ")
                try:
                    query = text(f"SELECT * FROM pazienti WHERE IDP = '{patient_id}'")
                    with engine.connect() as conn:
                        res = pd.read_sql_query(query, conn)
                        return res
                except Exception as e:
                    print(Bcolors.FAIL + f"\n[ERROR] Something goes wrong. Error message : {e}\n" + Bcolors.ENDC)
            else:
                print(Bcolors.FAIL + f"\n[ERROR] Invalid input..." + Bcolors.ENDC)


def getStoriaClinica(engine, ruolo):

    choice = ''

    print(Bcolors.OKCYAN + """
        SELECT AN OPTION
    
        [1] Clinical history of all patients
        [2] Search patient
            """ + Bcolors.ENDC)

    while choice != '1' and choice != '2':

        if ruolo == 2:

            while True:

                choice = input("\n[INFO] Select an option >>> ")

                if choice == '1':
                    query = text("SELECT ID_PAZIENTE, ID_PERSONALE, PATOLOGIA, PRESCRIZIONI FROM cure")
                    with engine.connect() as conn:
                        res = pd.read_sql_query(query, conn)
                        return res
                elif choice == '2':
                    patient_id = input("\n[INFO] Input patient UID >>> ")
                    try:
                        query = text(f"SELECT ID_PAZIENTE, ID_PERSONALE, PATOLOGIA, PRESCRIZIONI FROM cure WHERE ID_PAZIENTE = '{patient_id}'")
                        with engine.connect() as conn:
                            res = pd.read_sql_query(query, conn)
                            return res
                    except Exception as e:
                        print(Bcolors.FAIL +  f"\n[ERROR] Something goes wrong. Error message : {e}\n" + Bcolors.ENDC)
                else:
                    print(Bcolors.FAIL + f"\n[ERROR] Invalid input...\n" + Bcolors.ENDC)

        else:
            choice = input("\n[INFO] Select an option >>> ")

            if choice == '1':
                query = text("SELECT * FROM cure")
                with engine.connect() as conn:
                    res = pd.read_sql_query(query, conn)
                    return res
            elif choice == '2':
                patient_id = input("\n[INFO] Input patient UID >>> ")
                try:
                    query = text(f"SELECT * FROM cure WHERE ID_PAZIENTE = '{patient_id}'")
                    with engine.connect() as conn:
                        res = pd.read_sql_query(query, conn)
                        return res
                except Exception as e:
                    print(Bcolors.FAIL + f"\n[ERROR] Something goes wrong. Error message : {e}\n" + Bcolors.ENDC)
            else:
                print(Bcolors.FAIL + f"\n[ERROR] Invalid input..." + Bcolors.ENDC)


def getDataframeParametri(engine, tipo, UID):
    with engine.connect() as conn:
        query = text(f"SELECT TIMESTAMP, VALORE, TIPO, WARNING FROM parametri_vitali WHERE ID = '{UID}' AND TIPO = '{tipo}'")
        res = pd.read_sql_query(query, conn)

    return res


def getParametri(engine):

    print(Bcolors.OKCYAN + """
        SELECT AN OPTION
                        
        [1] Temperature
        [2] Systolic pressure
        [3] Diastolic pressure
        [4] Pulse
        [5] Respiratory rate
        [6] EEG
                        """ + Bcolors.ENDC)

    choice = ''

    while choice not in ['1', '2', '3', '4', '5', '6']:

        while True:

            choice = input("\n[INFO] Select an option >>> ")

            if choice not in ['1', '2', '3', '4', '5', '6']:
                print(Bcolors.FAIL + f"\n[ERROR] Invalid input..." + Bcolors.ENDC)
                continue

            UID = input("\n[INFO] Insert patient UID >>> ")

            if choice == '1':
                type = 'T'
                res = getDataframeParametri(engine, type, UID)


            elif choice == '2':
                type = 'PS'
                res = getDataframeParametri(engine, type, UID)


            elif choice == '3':
                type = 'PD'
                res = getDataframeParametri(engine, type, UID)

            elif choice == '4':
                type = 'POL'
                res = getDataframeParametri(engine, type, UID)


            elif choice == '5':
                type = 'F'
                res = getDataframeParametri(engine, type, UID)


            elif choice == '6':
                type = 'EEG'
                res = getDataframeParametri(engine, type, UID)


            else:
                print(Bcolors.FAIL + f"\n[ERROR] Invalid input..." + Bcolors.ENDC)


            return res, type


def getEmergencies(engine):
    with engine.connect() as conn:
        query = text("select ID, count(VALORE) AS WARNINGS from parametri_vitali WHERE ((TIPO = 'T' AND VALORE >= 39.5) OR (TIPO = 'PS' AND VALORE >= 175)) GROUP BY ID")
        res = pd.read_sql_query(query, conn)

    return res

def getFullEmergenciesData(engine, ID):
    query = text(f"SELECT pa.IDP, pa.NOME, pa.COGNOME, cu.PATOLOGIA, cu.MMSE, cu.BRASS, pv.TIMESTAMP, pv.TIPO, pv.VALORE FROM pazienti AS pa JOIN cure AS cu ON pa.IDP = cu.ID_PAZIENTE JOIN parametri_vitali AS pv ON pa.IDP = pv.ID WHERE ((pv.TIPO = 'T' AND pv.VALORE >= 39.5) OR (pv.TIPO = 'PS' AND pv.VALORE >= 175)) AND (pa.IDP = '{ID}')")
    with engine.connect() as conn:
        res = pd.read_sql_query(query, conn)

    return res


def checkUser(user):
    global users
    if user not in users:
        return 0

